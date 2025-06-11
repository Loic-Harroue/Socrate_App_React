import requests
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import pandas as pd
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, FileResponse
from django.views.decorators.http import require_POST
from app.utils.decorators import user_in_groups_or_superuser
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from functools import lru_cache
from io import BytesIO
from app.utils.cluster_download import generate_pdf_summary, generate_docx_summary
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from app.utils.api_logger import log_api_call, api_log_store
from app.constants.colors import COLORS
from . import settings_constants

API_TOKEN_URL = settings_constants.SETTINGS_CONSTANT['API_TOKEN_URL']
API_VERSION_URL = settings_constants.SETTINGS_CONSTANT['API_VERSION_URL']
API_CATEGORIES_URL = settings_constants.SETTINGS_CONSTANT['API_CATEGORIES_URL']
API_MODELS_URL     = settings_constants.SETTINGS_CONSTANT['API_MODELS_URL']
API_SUBMODELS_URL  = settings_constants.SETTINGS_CONSTANT['API_SUBMODELS_URL']
API_MODES_URL = settings_constants.SETTINGS_CONSTANT['API_MODES_URL']
API_CHAT_URL = settings_constants.SETTINGS_CONSTANT['API_CHAT_URL']
API_KEYWORDS_URL = settings_constants.SETTINGS_CONSTANT['API_KEYWORDS_URL']
API_SYNONYMES_URL = settings_constants.SETTINGS_CONSTANT['API_SYNONYMES_URL']
API_CLUSTER_URL = settings_constants.SETTINGS_CONSTANT['API_CLUSTER_URL']
API_CLUSTER_ZERO_URL = settings_constants.SETTINGS_CONSTANT['API_CLUSTER_ZERO_URL']
API_TRANSLATE_URL = settings_constants.SETTINGS_CONSTANT['API_TRANSLATE_URL']
API_LEVELS_URL = settings_constants.SETTINGS_CONSTANT['API_LEVELS_URL']
API_PROMPTS_URL = settings_constants.SETTINGS_CONSTANT['API_PROMPTS_URL']

#############################################################################################
                                    #Partie connexion
#############################################################################################
@csrf_protect
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ai_chat')
        else:
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")

    return render(request, 'login.html')

@csrf_protect
@user_in_groups_or_superuser(['Market', 'SuperAdmin'])
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ai_chat')
    else:
        form = SignUpForm(user=request.user)

    return render(request, 'register.html', {'form': form})

#############################################################################################
                                    #Partie Sidebar
#############################################################################################
@lru_cache(maxsize=1)
def get_models_and_submodels():
    headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}

    resp_models = requests.get(API_MODELS_URL, headers=headers, timeout=5)
    resp_models.raise_for_status()
    resp_subs = requests.get(API_SUBMODELS_URL, headers=headers, timeout=5)
    resp_subs.raise_for_status()

    df_models = pd.DataFrame(resp_models.json())\
        .rename(columns={'id': 'model_id', 'name': 'model_name'})
    df_subs = pd.DataFrame(resp_subs.json())\
        .rename(columns={'name': 'submodel_name', 'model_ai': 'model_id'})

    df_model_subs = pd.merge(
        df_subs, 
        df_models[['model_id', 'model_name']],
        on='model_id',
        how='left'
    )

    return (
        df_models[['model_id', 'model_name']].to_dict(orient='records'),
        df_model_subs[['model_id', 'submodel_name']].to_dict(orient='records')
    )

@csrf_protect
def ajax_load_submodels(request):
    """
    Vue Ajax légère : filtre dans la liste en Python pur, sans DataFrame.
    """
    model_id = request.GET.get('model_id')
    _, all_subs = get_models_and_submodels()

    if model_id:
        try:
            mid = int(model_id)
        except ValueError:
            return JsonResponse({'submodels': []})
        filtered = [sub['submodel_name'] 
                    for sub in all_subs 
                    if sub['model_id'] == mid]
    else:
        filtered = []

    return JsonResponse({'submodels': filtered})
@csrf_protect  
def ajax_load_categories(request):
    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}
        resp_cat = requests.get(API_CATEGORIES_URL, headers=headers, timeout=5)
        resp_cat.raise_for_status()
        df_categories = pd.DataFrame(resp_cat.json())

        return JsonResponse(df_categories[['ref', 'name']].to_dict(orient='records'), safe=False)

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API', 'details': str(e)}, status=500)

@csrf_protect
def ajax_load_modes(request):
    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}
        resp_modes = requests.get(API_MODES_URL, headers=headers, timeout=5)
        resp_modes.raise_for_status()
        df_modes = pd.DataFrame(resp_modes.json())

        return JsonResponse(df_modes[['ref', 'name']].to_dict(orient='records'), safe=False)

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API', 'details': str(e)}, status=500)
    
@csrf_protect    
def ajax_get_version(request):
    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if getattr(settings, "API_TOKEN", None) else {}
        payload = {
            "details": False
        }

        resp_ver = requests.post(API_VERSION_URL, headers=headers, json=payload)
        resp_ver.raise_for_status()

        data = resp_ver.json()
        version = data.get('version', 'non spécifiée')
        return JsonResponse({'version': version})

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API', 'details': str(e)}, status=500)

@csrf_protect
def ajax_select_categories(request):
    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}
        resp_cate = requests.get(API_CATEGORIES_URL, headers=headers, timeout=5)
        resp_cate.raise_for_status()

        df = pd.DataFrame(resp_cate.json())

        return JsonResponse(df[['ref', 'name']].to_dict(orient='records'), safe=False)

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API (catégories)', 'details': str(e)}, status=500)


@csrf_protect
def ajax_load_levels(request):
    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}
        resp = requests.get(API_LEVELS_URL, headers=headers, timeout=5)
        resp.raise_for_status()

        df = pd.DataFrame(resp.json())

        return JsonResponse(df[['ref', 'name']].to_dict(orient='records'), safe=False)

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API (niveaux)', 'details': str(e)}, status=500)

#############################################################################################
                                    #Partie Chat
#############################################################################################
def chat_view(request):
    models_list, all_subs = get_models_and_submodels()
    return render(request, 'chat.html', {
        'df_models': models_list,
        'active_page': 'chat',
    })

@csrf_protect
@log_api_call("CHAT")
def ajax_send_chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            model = data.get('model')
            sous_model = data.get('sous_model')
            user_artirev = data.get('user_artirev')
            question = data.get('question')
            if not all([model, sous_model, user_artirev, question]):
                return HttpResponseBadRequest("Données manquantes.")

            payload = {
                "model": model,
                "sous_model": sous_model,
                "user_artirev": user_artirev,
                "question": question
            }

            headers = {'Authorization': f"Token {settings.API_TOKEN}"}
            response = requests.post(API_CHAT_URL, headers=headers, json=payload)
            print(response.text)
            if response.status_code == 200:
                json_data = response.json()
                django_response = JsonResponse(json_data)
                django_response.json_data = json_data

                return django_response
            else:
                print("Erreur")
                return JsonResponse({'error': 'Erreur de l\'API externe.'}, status=500)
                

        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON invalide.")
    else:
        return HttpResponseBadRequest("Méthode non autorisée.")

#############################################################################################
                                    #Partie Keywords
#############################################################################################
def keywords_view(request):
    models_list, all_subs = get_models_and_submodels()

    return render(request, 'keywords.html', {
        'df_models': models_list,
        'all_subs': all_subs,
        'active_page': 'keywords',
    })

@csrf_protect
@log_api_call("KEYWORDS")
def ajax_keywords_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_artirev = data.get('user_artirev')
            model = data.get('model')
            sous_model = data.get('sous_model')
            science = data.get('dataset_type')
            source_text = data.get('question')
            

            if not all([model, science, source_text]):
                return JsonResponse({'error': 'Champs manquants.'}, status=400)
            
            payload = {
                "model": model,
                "sous_model": sous_model,
                "user_artirev": user_artirev,  
                "nbr_max": 10,
                "source_text": source_text,
                "science": science,
            }
            headers = {'Authorization': f"Token {settings.API_TOKEN}"}
            response = requests.post(API_KEYWORDS_URL, headers=headers, json=payload)
            if response.status_code == 200:
                json_data = response.json()
                django_response = JsonResponse(json_data)
                django_response.json_data = json_data

                return django_response
            else:
                return JsonResponse({'error': 'Erreur de l\'API.'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalide.'}, status=400)
    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)


#############################################################################################
                                    #Partie Synonymes
#############################################################################################
def synonymes_view(request):
    models_list, all_subs = get_models_and_submodels()

    return render(request, 'synonymes.html', {
        'df_models': models_list,
        'all_subs': all_subs,
        'active_page': 'synonymes',
    })

@csrf_protect
@log_api_call("SYNONYMES")
def ajax_synonymes_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_artirev = data.get('user_artirev')
            model = data.get('model')
            sous_model = data.get('sous_model')
            science = data.get('dataset_type')
            words = data.get('words')
            

            if not all([model, science, words]):
                return JsonResponse({'error': 'Champs manquants.'}, status=400)
            
            payload = {
                "model": model,
                "sous_model": sous_model,
                "user_artirev": user_artirev,  
                "nbr_max": 10,
                "word": words,
                "science": science,
            }
            headers = {'Authorization': f"Token {settings.API_TOKEN}"}
            response = requests.post(API_SYNONYMES_URL, headers=headers, json=payload)
            if response.status_code == 200:
                json_data = response.json()
                django_response = JsonResponse(json_data)
                django_response.json_data = json_data

                return django_response
            else:
                return JsonResponse({'error': 'Erreur de l\'API.'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalide.'}, status=400)
    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

#############################################################################################
                                    #Partie Cluster
#############################################################################################
def cluster_view(request):
    models_list, all_subs = get_models_and_submodels()

    context = {
        'df_models': models_list,
        'all_subs': all_subs,
        'active_page': 'cluster',
        'colors_json': json.dumps(COLORS),
    }

    return render(request, 'cluster.html', context)

@csrf_protect
@log_api_call("CLUSTER")
def ajax_cluster_api(request):
    if request.method == 'POST':
        if request.FILES.get('file'):
            file = request.FILES['file']
            try:
                df = pd.read_excel(file)
                user_artirev = "API"
                model = request.POST.get('model')
                sous_model = request.POST.get('sous_model')
                science = request.POST.get('dataset_type')
                if not all([model, science]):
                    return JsonResponse({'error': 'Champs manquants.'}, status=400)
                if df.empty:
                    return JsonResponse({'error': 'Le fichier est vide.'}, status=400)
                df.columns = df.columns.str.replace(' ', '_')
                clusters_json = df.to_dict(orient='records')
                content = 'map_themes'
                payload = {
                    "model": model,
                    "sous_model": sous_model,
                    "user_artirev": user_artirev,
                    "content": content,
                    "clusters": clusters_json,
                    "science": science,
                }
                headers = {'Authorization': f"Token {settings.API_TOKEN}"}
                response = requests.post(API_CLUSTER_URL, headers=headers, json=payload) 
                if response.status_code == 200:
                    json_data = response.json()
                    django_response = JsonResponse(json_data)
                    django_response.json_data = json_data

                    return django_response
                else:
                    return JsonResponse({'error': 'Erreur de l\'API.'}, status=500)

            except Exception as e:
                return JsonResponse({'error': f'Erreur lecture fichier : {str(e)}'}, status=400)

        return JsonResponse({'error': 'Aucun fichier reçu.'}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

#############################################################################################
                                    #Partie Cluster Zero
#############################################################################################
def cluster_zero_view(request):
    models_list, all_subs = get_models_and_submodels()

    return render(request, 'cluster_zero.html', {
        'df_models': models_list,
        'all_subs': all_subs,
        'active_page': 'cluster_zero',
    })

@csrf_protect
@log_api_call("CLUSTER ZERO")
def ajax_cluster_zero_api(request):
    if request.method == 'POST':
        if request.FILES.get('file'):
            file = request.FILES['file']
            try:
                df = pd.read_excel(file)
                user_artirev = "API"
                model = request.POST.get('model')
                sous_model = request.POST.get('sous_model')
                science = request.POST.get('dataset_type')
                if not all([model, science]):
                    return JsonResponse({'error': 'Champs manquants.'}, status=400)
                if df.empty:
                    return JsonResponse({'error': 'Le fichier est vide.'}, status=400)
                
                df.columns = df.columns.str.replace(' ', '_')
                df = df.drop(columns=['Index_Keywords'])
                clusters_zero_json = df.to_dict(orient='records')
                content = 'map_themes'
                payload = {
                    "model": model,
                    "sous_model": sous_model,
                    "user_artirev": user_artirev,
                    "content": content,
                    "clusters": clusters_zero_json,
                    "science": science,
                }
                headers = {'Authorization': f"Token {settings.API_TOKEN}"}
                response = requests.post(API_CLUSTER_ZERO_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    json_data = response.json()
                    django_response = JsonResponse(json_data)
                    django_response.json_data = json_data

                    return django_response
                else:
                    return JsonResponse({'error': 'Erreur de l\'API.'}, status=500)

            except Exception as e:
                return JsonResponse({'error': f'Erreur lecture fichier : {str(e)}'}, status=400)

        return JsonResponse({'error': 'Aucun fichier reçu.'}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

#############################################################################################
                                    #Partie download
#############################################################################################
@csrf_protect
def generate_pdf_view(request):
    if request.method == 'POST':
        try:
            json_string = request.body.decode('utf-8')

            buffer = BytesIO()
            generate_pdf_summary(json_string, buffer)

            buffer.seek(0)
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="summary.pdf"'
            return response

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

@csrf_protect
def generate_docx_view(request):
    if request.method == 'POST':
        try:
            json_string = request.body.decode('utf-8')
            filename_docx = "summary.docx"
            generate_docx_summary(json_string, filename_docx)
            
            # Renvoie directe du fichier DOCX
            return FileResponse(open(filename_docx, 'rb'), as_attachment=True, filename=filename_docx)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

#############################################################################################
                                    #Partie traduction
#############################################################################################
@csrf_protect
@log_api_call("TRADUCTION")
def ajax_translate_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_artirev = "API"
            model = data.get('model')
            sous_model = data.get('sous_model')
            raw_data = data.get('data')

            if not raw_data:
                return JsonResponse({'error': 'Données manquantes.'}, status=400)
            
            content = 'map_themes'
            lang = "fr"
            payload = {
                "model": model,
                "sous_model": sous_model,
                "user_artirev": user_artirev,
                "lang": lang,
                "content": content,
                "clusters": raw_data
            }

            headers = {'Authorization': f"Token {settings.API_TOKEN}"}
            response = requests.post(API_TRANSLATE_URL, headers=headers, json=payload)
            if response.status_code == 200:
                json_data = response.json()
                django_response = JsonResponse(json_data)
                django_response.json_data = json_data

                return django_response
            else:
                return JsonResponse({'error': 'Erreur API de traduction.'}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)

#############################################################################################
                                    #Partie logs
#############################################################################################
def logs_view(request):
    df = api_log_store.get_logs()
    df_html = df.to_html(classes="display", index=False, table_id="log-table")
    return render(request, "logs.html", {"df_html": df_html})

#############################################################################################
                                    #Partie Prompts
#############################################################################################

def prompts_view(request):

    return render(request, "prompts.html", {'active_page': 'prompts',})

def ajax_get_prompt(request):
    category_ref = request.GET.get('category_ref')
    level_ref = request.GET.get('level_ref')
    
    if not category_ref  or not level_ref:
        return JsonResponse({'error': 'Paramètres manquants'}, status=400)

    try:
        headers = {'Authorization': f"Token {settings.API_TOKEN}"} if settings.API_TOKEN else {}
        url = f"{API_PROMPTS_URL}{category_ref}/{level_ref}"
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        return JsonResponse({'prompt_text': data.get('prompt_text', '')})

    except requests.RequestException as e:
        return JsonResponse({'error': 'Erreur API', 'details': str(e)}, status=500)
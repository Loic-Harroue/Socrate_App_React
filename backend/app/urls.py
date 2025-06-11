"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.custom_login_view, name='login'),  
    path('login/', views.custom_login_view, name='login'),
    path('register/', staff_member_required(views.register), name='register'),
    path('logs/', views.logs_view, name='logs'),
    path('ai_chat/', views.chat_view, name='ai_chat'),
    path('process_clusters/', views.cluster_view, name='process_clusters'),
    path('process_clusters_zero/', views.cluster_zero_view, name='process_clusters_zero'),
    path('process_keywords/', views.keywords_view, name='process_keywords'),
    path('process_synonyms/', views.synonymes_view, name='process_synonyms'),
    path('ajax/submodels/', views.ajax_load_submodels,name='ajax_load_submodels'),
    path('ajax/send-chat/', views.ajax_send_chat, name='ajax_send_chat'),
    path('ajax/keywords/', views.ajax_keywords_api, name='ajax_keywords_api'),
    path('ajax/synonymes/', views.ajax_synonymes_api, name='ajax_synonymes_api'),
    path('ajax/load-categories/', views.ajax_load_categories, name='ajax_load_categories'),
    path('ajax/load-modes/', views.ajax_load_modes, name='ajax_load_modes'),
    path('ajax/load-ver/', views.ajax_get_version, name='ajax_get_version'),
    path('ajax/cluster/', views.ajax_cluster_api, name='ajax_cluster_api'),
    path('ajax/clusters_zero/', views.ajax_cluster_zero_api, name='ajax_cluster_zero_api'),
    path('process_clusters/ajax/generate_pdf/', views.generate_pdf_view, name='generate_pdf_view'),
    path('process_clusters/ajax/generate_docx/', views.generate_docx_view, name='generate_docx_view'),
    path('process_clusters/ajax/translate/', views.ajax_translate_api, name='ajax_translate_api'),
    path('process_clusters_zero/ajax/generate_pdf/', views.generate_pdf_view, name='generate_pdf_view'),
    path('process_clusters_zero/ajax/generate_docx/', views.generate_docx_view, name='generate_docx_view'),
    path('ajax/select-categories/', views.ajax_select_categories, name='ajax_select_categories'),
    path('ajax/load-levels/', views.ajax_load_levels, name='ajax_load_levels'),
    path('prompts/', staff_member_required(views.prompts_view), name='prompts'),
    path('ajax/get-prompt/', views.ajax_get_prompt, name='ajax_get_prompt'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

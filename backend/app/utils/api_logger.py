import time
from functools import wraps
from datetime import datetime
import pandas as pd

class ApiLogStore:
    def __init__(self):
        self.df = pd.DataFrame(columns=[
            'Date', 'Sous Model', 'Couts', 'Prompt Tokens', 'Completion Tokens',
            'Duree', 'Module', 'User', 'Mois'
        ])

    def log(self, *, model, cost, prompt_tokens, completion_tokens, duration, module, user):
        now = datetime.now()
        log_entry = {
            'Date': now.strftime('%Y-%m-%d %H:%M:%S'),
            'Sous Model': model,
            'Couts': cost,
            'Prompt Tokens': prompt_tokens,
            'Completion Tokens': completion_tokens,
            'Duree': round(duration, 4),
            'Module': module,
            'User': user.username if hasattr(user, 'username') else str(user),
            'Mois': now.strftime('%Y-%m'),
        }
        self.df = pd.concat([self.df, pd.DataFrame([log_entry])], ignore_index=True)

    def get_logs(self):
        return self.df


# Singleton du log store
api_log_store = ApiLogStore()

def log_api_call(module_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            start = time.time()
            response = view_func(request, *args, **kwargs)
            end = time.time()
            duration = end - start

            try:
                json_data = getattr(response, 'json_data', None)
                if not json_data and hasattr(response, 'data'):
                    json_data = response.data

                api_log_store.log(
                    model=json_data.get('result_model', 'N/A'),
                    cost=json_data.get('couts', 0),
                    prompt_tokens=json_data.get('prompt_token', 0),
                    completion_tokens=json_data.get('completion_token', 0),
                    duration=duration,
                    module=module_name,
                    user=request.user
                )
            except Exception as e:
                print(f"[Logger Warning] Failed to log API call: {e}")

            return response
        return wrapper
    return decorator

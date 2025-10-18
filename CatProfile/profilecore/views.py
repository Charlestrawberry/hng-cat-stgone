import requests
from django.http import JsonResponse
from datetime import datetime, timezone

def me(request):
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact", "No fact available right now.")
        else:
            cat_fact = "Could not fetch a cat fact at the moment."
    except requests.RequestException:
        cat_fact = "External API error: Unable to fetch cat fact."
    
    data = {
        "status": "success",
        "user": {
            "email": "charlestrawb_odus@yahoo.com",
            "name": "Odukoya Charles",
            "stack": "python/django",
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JsonResponse(data, content_type="application/json")
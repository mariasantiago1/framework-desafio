from flask import current_app
from typing import List, Dict, Optional
import requests


def _fetch_todos() -> Optional[List[Dict[int, str]]]:   
    try:
        response = requests.get(current_app.config['TODOS_URL'])
        
        if response.status_code != 200:
            raise()
    except:
        return None
    
    todos = []
    
    for todo in response.json()[:5]:
        todos.append({
            'id': todo['id'],
            'title': todo['title']
        })
    
    return todos
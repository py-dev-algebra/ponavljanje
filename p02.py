import json
from typing import List, Dict, Any


def convert_to_json(object: Dict[str, Any]={}) -> str:
    if len(object.keys()) > 0:
        return json.dumps(object)
    
    return ''

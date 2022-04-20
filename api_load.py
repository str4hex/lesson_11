import json

from requests import get


def api():
    response = get("https://pastebin.com/raw/aTGck4L2").text
    json_load = json.loads(response)
    return json_load

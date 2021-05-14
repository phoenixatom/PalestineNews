import requests
from requests.exceptions import ConnectionError
from sites import aljazeera, palinfo, ei

url_patterns = {
    "hamas.ps/en": "hamas",
    "aljazeera.com": "aljazeera",
    "english.palinfo.com": "palinfo",
    "electronicintifada.net": "ei"
}


def scrape(url: str):
    is_reachable = get_content(url)
    if is_reachable:
        site = identify_site(url)
        scraped = globals()[site](url)
        return scraped
    else:
        return None


def get_content(url: str):
    try:
        req = requests.get(url)
    except ConnectionError:
        return False
    if req.status_code == 200:
        return True
    else:
        return False


def identify_site(url: str):
    for pattern in url_patterns:
        if pattern in url:
            return url_patterns[pattern]

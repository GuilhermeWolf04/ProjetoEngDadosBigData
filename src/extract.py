from typing import Any, Dict, List

import requests


class Extract:
    def extract_country(self, country: str) -> List[Dict[str, Any]]:
        url = "http://universities.hipolabs.com/search"
        response = requests.get(url, params={"country": country}, timeout=30)
        response.raise_for_status()
        universities = response.json()
        return universities

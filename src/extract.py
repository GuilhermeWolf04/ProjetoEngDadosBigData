from typing import Any, Dict, List

import requests


class Extract:
    def extract_country(self, country: str) -> List[Dict[str, Any]]:
        """Consulta a Universities API para retornar universidades de um pais.

        Args:
            country: Nome do pais usado no filtro da API.

        Returns:
            Lista de universidades em formato de dicionario.
        """
        url = "http://universities.hipolabs.com/search"
        response = requests.get(url, params={"country": country}, timeout=30)
        response.raise_for_status()
        universities = response.json()
        return universities

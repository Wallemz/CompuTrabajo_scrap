from typing import Any, Dict, Optional, Union
import requests


class RequestHandler:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url

    def _send_request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Optional[Union[Dict[str, Any], str]]:
        """Método para enviar una petición HTTP a una URL

        Args:
            method (str): El método HTTP a usar, eg. POST GET PUT DELETE
            endpoint (str): Es la parte final del link, luego del dominio de la página WEB
            headers (Optional[Dict[str, str]], optional): Headers de la petición. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Información a enviar dentro de la petición. Defaults to None.
            params (Optional[Dict[str, Any]], optional): Parámetros de la petición. Defaults to None.

        Returns:
            Optional[Union[Dict[str, Any], str]]: Retorna la respuesta de la petición, en caso de no
            haber respuesta retorna None
        """
        url = self.base_url + endpoint
        response = requests.request(
            method, url, headers=headers, data=data, params=params
        )

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return response.text
        else:
            print(f"Error al obtener la página: {response.status_code}")
            return None


    def get(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP GET

        Args:
            endpoint (str): Es la parte final del link, luego del dominio de la página WEB
            headers (Optional[Dict[str, str]], optional): Headers de la petición. Defaults to None.
            params (Optional[Dict[str, Any]], optional): Parámetros de la petición. Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        return self._send_request("GET", endpoint, headers=headers, params=params)

    def post(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP POST

        Args:
            endpoint (str):  Es la parte final del link, luego del dominio de la página WEB
            headers (Optional[Dict[str, str]], optional): Headers de la petición. Defaults to None. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Información a enviar dentro de la petición. Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        return self._send_request("POST", endpoint, headers=headers, data=data)

    def put(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP PUT

        Args:
            endpoint (str): Es la parte final del link, luego del dominio de la página WEB
            headers (Optional[Dict[str, str]], optional): Headers de la petición. Defaults to None. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Información a enviar dentro de la petición. Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        return self._send_request("PUT", endpoint, headers=headers, data=data)

    def delete(
        self, endpoint: str, headers: Optional[Dict[str, str]] = None
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP DELETE

        Args:
            endpoint (str): Es la parte final del link, luego del dominio de la página WEB
            headers (Optional[Dict[str, str]], optional): Headers de la petición. Defaults to None. Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        return self._send_request("DELETE", endpoint, headers=headers)

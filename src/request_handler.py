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
        return self._send_request("GET", endpoint, headers=headers, params=params)

    def post(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        return self._send_request("POST", endpoint, headers=headers, data=data)

    def put(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        return self._send_request("PUT", endpoint, headers=headers, data=data)

    def delete(
        self, endpoint: str, headers: Optional[Dict[str, str]] = None
    ) -> Optional[Dict[str, Any] | str]:
        return self._send_request("DELETE", endpoint, headers=headers)

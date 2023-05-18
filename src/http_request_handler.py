import requests

from typing import Any, Dict, Optional, Union


class HTTPRequestHandler:
    """Class to make HTTP Request: POST, GET, PUT, DELETE
    """
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        if not headers:
            self.headers = None
        self.headers = headers

    def _send_request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Optional[Union[Dict[str, Any], str]]:
        """General Method to send a HTTP Request

        Args:
            method (str): HTTP method, eg. POST GET PUT DELETE
            endpoint (str): Final part of the web link
            headers (Optional[Dict[str, str]], optional): Headers. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Data . Defaults to None.
            params (Optional[Dict[str, Any]], optional): Params . Defaults to None.

        Returns:
            Optional[Union[Dict[str, Any], str]]: HTTP Response, if no response then None is returned
        """
        if headers == None:
            headers = self.headers

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
            endpoint (str): Final part of the web link
            headers (Optional[Dict[str, str]], optional): Headers. Defaults to None.
            params (Optional[Dict[str, Any]], optional): Params . Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        if headers == None:
            headers = self.headers
        return self._send_request("GET", endpoint, headers=headers, params=params)

    def post(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP POST

        Args:
            endpoint (str):  Final part of the web link
            headers (Optional[Dict[str, str]], optional): Headers. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Data . Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        if headers == None:
            headers = self.headers
        return self._send_request("POST", endpoint, headers=headers, data=data)

    def put(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Union[str, Dict[str, Any]]] = None,
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP PUT

        Args:
            endpoint (str): Final part of the web link
            headers (Optional[Dict[str, str]], optional): Headers. Defaults to None.
            data (Optional[Union[str, Dict[str, Any]]], optional): Data . Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        if headers == None:
            headers = self.headers
        return self._send_request("PUT", endpoint, headers=headers, data=data)

    def delete(
        self, endpoint: str, headers: Optional[Dict[str, str]] = None
    ) -> Optional[Dict[str, Any] | str]:
        """Método HTTP DELETE

        Args:
            endpoint (str): Final part of the web link
            headers (Optional[Dict[str, str]], optional): Headers. Defaults to None.

        Returns:
            Optional[Dict[str, Any] | str]: _description_
        """
        if headers == None:
            headers = self.headers
        return self._send_request("DELETE", endpoint, headers=headers)

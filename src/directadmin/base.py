"""
Module Base classes
"""

import json
from urllib.parse import parse_qs, urljoin, urlencode, urlparse, urlunparse
from abc import ABC

import requests
from requests.auth import HTTPBasicAuth


class BaseDirectAdminAPIClient(ABC):
    """
    A base class for interacting with the DirectAdmin API.

    This class provides methods for making HTTP requests to the DirectAdmin
    API, handling authentication, and processing responses.

    Attributes:
        server (str): The base URL of the DirectAdmin server.
        ssl (bool): Whether to verify SSL certificates. Defaults to False.
        __auth (HTTPBasicAuth): HTTP basic authentication credentials.
        user_agent (str): The User-Agent header to be sent with requests.
        Defaults to "DirectAdmin Client/0.1.0".

    Methods:
        _make_request(endpoint, params=None, method="GET", data=None):
            Makes an HTTP request to the DirectAdmin API with the
            specified parameters.

        _build_url(endpoint, params=None):
            Constructs a full URL by combining the server base URL with the
            endpoint and optional query parameters.

        _parse_response(response):
            Parses the response from the DirectAdmin API, handling both JSON
            and query string formats.

    Args:
        server (str): The base URL of the DirectAdmin server.
        username (str): The username for HTTP basic authentication.
        password (str): The password for HTTP basic authentication.
        ssl (bool, optional): Whether to use SSL verification for requests.
            Defaults to False.
        user_agent (str, optional): The User-Agent string to be used in
            requests. Defaults to "DirectAdmin Client/0.1.0".
    """

    def __init__(self, server, username, password, ssl=False, user_agent=None):
        """
        Initializes the BaseDirectAdminAPIClient with the provided parameters.

        Args:
            server (str): The base URL of the DirectAdmin server.
            username (str): The username for HTTP basic authentication.
            password (str): The password for HTTP basic authentication.
            ssl (bool, optional): Whether to use SSL verification for requests.
                Defaults to False.
            user_agent (str): The User-Agent string to be used in requests.
                Defaults to "DirectAdmin Client/0.1.0".
        """
        self.server = server
        self.ssl = ssl
        self.__auth = HTTPBasicAuth(username, password)
        self.user_agent = user_agent or "DirectAdmin Client/0.1.0"

    def _make_request(self, endpoint, params=None, method="GET", data=None):
        """
        Makes an HTTP request to the DirectAdmin API
        with the specified parameters.

        Args:
            endpoint (str): The API endpoint to request.
            params (dict): A dictionary of query parameters to
                include in the request URL.
            method (str): The HTTP method to use for the request.
                Defaults to "GET". Can be "GET" or "POST".
            data (dict): Data to be sent in the body of a POST request.
                Ignored for GET requests.

        Returns:
            dict: The parsed response from the DirectAdmin API,
                as a dictionary.

        Raises:
            ValueError: If the provided method is not "GET" or "POST".
        """
        url = self._build_url(endpoint, params)
        headers = {"User-Agent": self.user_agent}
        if method == "GET":
            response = requests.get(
                url,
                auth=self.__auth,
                verify=self.ssl,
                headers=headers,
                timeout=60,
            )
        elif method == "POST":
            response = requests.post(
                url,
                auth=self.__auth,
                verify=self.ssl,
                headers=headers,
                data=data,
                timeout=60,
            )
        else:
            raise ValueError("Method must be GET or POST")
        return self._parse_response(response)

    def _build_url(self, endpoint, params=None):
        """
        Constructs a full URL by combining the server base URL with the
            endpoint and optional query parameters.

        Args:
            endpoint (str): The API endpoint to append to the base URL.
            params: A dictionary of query parameters to include in the URL.

        Returns:
            str: The full URL constructed from the base URL,
                endpoint, and query parameters.
        """
        base_url = self.server.rstrip("/")
        url = urljoin(base_url, endpoint.lstrip("/"))

        if params:
            query_string = urlencode(params)
            url_parts = list(urlparse(url))
            url_parts[4] = query_string
            url = urlunparse(url_parts)
        return url

    @staticmethod
    def _parse_response(response):
        """
        Parses the response from the DirectAdmin API,
            handling both JSON and query string formats.

        Args:
            response (requests.Response): The HTTP response object to parse.

        Returns:
            dict:
                The parsed response data,
                either from JSON or query string format.
                Returns an empty dictionary if parsing fails.
        """
        response_text = response.text.strip()

        try:
            parsed_data = json.loads(response_text)
        except json.JSONDecodeError:
            parsed_data = parse_qs(response_text)

        if isinstance(parsed_data, dict):
            if "list[]" in parsed_data:
                return parsed_data["list[]"]
            return parsed_data
        print("Unexpected response format")
        return {}

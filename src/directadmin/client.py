"""
DirectAdmin API Client Module
"""

from typing import Dict, Any

from .base import BaseDirectAdminAPIClient
from .endpoints import (
    GET_ALL_USERS,
    GET_ALL_ADMINS,
    GET_ALL_RESELLERS,
    GET_ADMIN_STATS,
    CREATE_ADMIN_ACCOUNT,
    GET_RESELLER_PACKAGES,
    GET_RESELLER_IP_LIST,
    CREATE_RESELLER_ACCOUNT,
    GET_USER_PACKAGES,
    GET_USER_CONFIG,
    GET_USER_USAGE,
    GET_USER_DOMAIN,
    CREATE_USER_ACCOUNT,
    ACTIVE_DEACTIVE_USER,
)


class DirectAdminAPIClient(BaseDirectAdminAPIClient):
    """
    A client for interacting with the DirectAdmin API.

    This class provides methods to interact with the DirectAdmin API endpoints,
    allowing you to manage resellers, admins, users,
    and their related configurations and statistics.

    Properties:
        get_all_resellers (list): Fetches a list of all resellers.
        get_all_admins (list): Fetches a list of all admins.
        get_all_users (list): Fetches a list of all users.
        get_all_reseller_packages (list):
            Fetches a list of all reseller packages.
        get_all_user_packages (list): Fetches a list of all user packages.
        get_reseller_ip_list (list):
            Fetches a list of IP addresses associated with resellers.
        get_admin_stats (Dict[str, Any]): Fetches statistics about the admin.

    Methods:
        get_reseller_package(package_name: str) -> Dict[str, Any]:
            Fetches details about a specific reseller package.

        get_user_package(package_name: str) -> Dict[str, Any]:
            Fetches details about a specific user package.

        get_user_config(username: str) -> Dict[str, Any]:
            Fetches configuration details for a specific user.

        get_user_usage(username: str) -> Dict[str, Any]:
            Fetches usage statistics for a specific user.

        get_user_domain(username: str) -> Dict[str, Any]:
            Fetches domain information for a specific user.

        create_admin_account(username: str, email: str,
            passwd: str, notify: str) -> Dict[str, Any]:
            Creates a new admin account with the specified details.

        create_reseller_account(username: str, email: str,
            passwd: str, notify: str, ip: str, package: str,
            domain: str) -> Dict[str, Any]:
            Creates a new reseller account with the specified details.

        create_user_account(username: str, email: str, passwd: str,
            notify: str, ip: str,
            package: str, domain: str) -> Dict[str, Any]:
            Creates a new user account with the specified details.
    """

    @property
    def get_all_resellers(self) -> list:
        """
        Fetches a list of all resellers.

        Returns:
            list: A list of all resellers.
        """
        return self._make_request(GET_ALL_RESELLERS)

    @property
    def get_all_admins(self) -> list:
        """
        Fetches a list of all admins.

        Returns:
            list: A list of all admins.
        """
        return self._make_request(GET_ALL_ADMINS)

    @property
    def get_all_users(self) -> list:
        """
        Fetches a list of all admins.

        Returns:
            list: A list of all admins.
        """
        return self._make_request(GET_ALL_USERS)

    @property
    def get_all_reseller_packages(self) -> list:
        """
        Fetches a list of all reseller packages.

        Returns:
            list: A list of all reseller packages.
        """
        return self._make_request(GET_RESELLER_PACKAGES)

    @property
    def get_all_user_packages(self) -> list:
        """
        Fetches a list of all user packages.

        Returns:
            list: A list of all user packages.
        """
        return self._make_request(GET_USER_PACKAGES)

    @property
    def get_reseller_ip_list(self) -> list:
        """
        Fetches a list of IP addresses associated with resellers.

        Returns:
            list: A list of IP addresses associated with resellers.
        """
        return self._make_request(GET_RESELLER_IP_LIST)

    @property
    def get_admin_stats(self) -> Dict[str, Any]:
        """
        Fetches statistics about the admin.

        Returns:
            Dict[str, Any]: A dictionary containing admin statistics.
        """
        return self._make_request(GET_ADMIN_STATS)

    def get_reseller_package(self, package_name: str) -> Dict[str, Any]:
        """
        Fetches details about a specific reseller package.

        Args:
            package_name (str): The name of the reseller package.

        Returns:
            Dict[str, Any]:
                A dictionary containing details of the reseller package.
        """
        params = {"package": package_name}
        return self._make_request(endpoint=GET_RESELLER_PACKAGES, params=params)

    def get_user_package(self, package_name: str) -> Dict[str, Any]:
        """
        Fetches details about a specific user package.

        Args:
            package_name (str): The name of the user package.

        Returns:
            Dict[str, Any]:
            A dictionary containing details of the user package.
        """
        params = {"package": package_name}
        return self._make_request(endpoint=GET_USER_PACKAGES, params=params)

    def get_user_config(self, username: str) -> Dict[str, Any]:
        """
        Fetches configuration details for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            Dict[str, Any]:
                A dictionary containing configuration details of the user.
        """
        params = {"user": username}
        return self._make_request(endpoint=GET_USER_CONFIG, params=params)

    def get_user_usage(self, username: str) -> Dict[str, Any]:
        """
        Fetches usage statistics for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            Dict[str, Any]:
                A dictionary containing usage statistics of the user.
        """
        params = {"user": username}
        return self._make_request(endpoint=GET_USER_USAGE, params=params)

    def get_user_domain(self, username: str) -> Dict[str, Any]:
        """
        Fetches domain information for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            Dict[str, Any]:
                A dictionary containing domain information of the user.
        """

        params = {"user": username}
        return self._make_request(endpoint=GET_USER_DOMAIN, params=params)

    def create_admin_account(
        self, username: str, email: str, passwd: str, notify: str
    ) -> Dict[str, Any]:
        """
        Creates a new admin account with the specified details.

        Args:
            username (str): The username for the new admin account.
            email (str):
                The email address associated with the new admin account.
            passwd (str): The password for the new admin account.
            notify (str): Notification preferences.

        Returns:
            Dict[str, Any]:
                A dictionary containing the result of the account creation.
        """
        params = {
            "action": "create",
            "username": username,
            "email": email,
            "passwd": passwd,
            "passwd2": passwd,
            "notify": notify,
        }
        return self._make_request(endpoint=CREATE_ADMIN_ACCOUNT, params=params)

    def create_reseller_account(
        self,
        username: str,
        email: str,
        passwd: str,
        notify: str,
        ip: str,
        package: str,
        domain: str,
    ) -> Dict[str, Any]:
        """
        Creates a new reseller account with the specified details.

        Args:
            username (str): The username for the new reseller account.
            email (str):
                The email address associated with the new reseller account.
            passwd (str): The password for the new reseller account.
            notify (str): Notification preferences.
            ip (str): IP address assignment options. Must be one of "shared",
                "sharedreseller", or "assign".
            package (str): The package to assign to the new reseller account.
            domain (str): The domain for the new reseller account.

        Returns:
            Dict[str, Any]:
                A dictionary containing the result of the account creation.

        Raises:
            ValueError: If the provided IP address option is invalid.
        """
        ip_allowed_options = ["shared", "sharedreseller", "assign"]
        if ip not in ip_allowed_options:
            raise ValueError(
                f"Invalid IP address. IP should be one of {ip_allowed_options}"
            )

        params = {
            "action": "create",
            "add": "submit",
            "username": username,
            "email": email,
            "passwd": passwd,
            "passwd2": passwd,
            "domain": domain,
            "package": package,
            "ip": ip,
            "notify": notify,
        }
        return self._make_request(endpoint=CREATE_RESELLER_ACCOUNT, params=params)

    def create_user_account(
        self,
        username: str,
        email: str,
        passwd: str,
        notify: str,
        ip: str,
        package: str,
        domain: str,
    ) -> Dict[str, Any]:
        """
        Creates a new user account with the specified details.

        Args:
            username (str): The username for the new user account.
            email (str):
                The email address associated with the new user account.
            passwd (str): The password for the new user account.
            notify (str): Notification preferences.
            ip (str): IP address for the new user account.
            package (str): The package to assign to the new user account.
            domain (str): The domain for the new user account.

        Returns:
            Dict[str, Any]:
                A dictionary containing the result of the account creation.
        """
        params = {
            "action": "create",
            "add": "submit",
            "username": username,
            "email": email,
            "passwd": passwd,
            "passwd2": passwd,
            "domain": domain,
            "package": package,
            "ip": ip,
            "notify": notify,
        }
        return self._make_request(endpoint=CREATE_USER_ACCOUNT, params=params)

    def suspend_account(self, *args) -> Dict[str, Any]:
        """Suspend one or more user accounts.

        Sends a request to the DirectAdmin ACTIVE_DEACTIVE_USER endpoint to suspend the
        specified user accounts. The request will include the parameter "dosuspend" set
        to "1" and each provided username will be added as a "select{index}" parameter,
        where index starts at 0.

        Args:
            *args: One or more username strings to suspend.

        Returns:
            Dict[str, Any]: The response returned by self._make_request (format depends on the API).

        Raises:
            Exception: Propagates any exception raised by self._make_request (e.g., network errors or API errors).

        Example:
            suspend_account('alice', 'bob')
        """
        params = {
            "dosuspend": "1",
        }

        for index, user in enumerate(args):
            params[f"select{index}"] = user

        return self._make_request(endpoint=ACTIVE_DEACTIVE_USER, params=params)

    def active_account(self, *args) -> Dict[str, Any]:
        """
        Reactivate one or more user accounts via the DirectAdmin API.

        This method prepares parameters to "undo suspend" (i.e., activate) the specified
        user accounts and sends a request to the ACTIVE_DEACTIVE_USER endpoint.

        Args:
            *args: Variable length argument list of usernames (str). Each username will
                be added to the request parameters as "select{index}" (e.g., "select0",
                "select1", ...). At least one username should be provided.

        Returns:
            Dict[str, Any]: The parsed response from the API call as returned by
            self._make_request.

        Raises:
            Any exceptions raised by self._make_request (e.g., network or API errors)
            are propagated to the caller.

        Example:
            client.active_account('alice', 'bob')
            # sends parameters: {"dounsuspend": "1", "select0": "alice", "select1": "bob"}
        """
        params = {
            "dounsuspend": "1",
        }

        for index, user in enumerate(args):
            params[f"select{index}"] = user

        return self._make_request(endpoint=ACTIVE_DEACTIVE_USER, params=params)

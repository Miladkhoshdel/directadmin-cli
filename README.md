# DirectAdminAPIClient

A lightweight Python client for the DirectAdmin HTTP API. DirectAdminAPIClient (which extends BaseDirectAdminAPIClient) provides convenience methods for managing admins, resellers, users, packages and account actions.

Highlights:
- Simple programmatic access to common DirectAdmin endpoints
- Thin wrapper around requests for easy customization
- Small, focused surface for account and package management

## Requirements
- Python 3.8+
- requests

## Installation

```bash
pip install directadmin-cli
```

## Quick start

```python
from directadmin.client import DirectAdminAPIClient

client = DirectAdminAPIClient(
    server="https://your-directadmin-server.com",
    username="your-username",
    password="your-password",
    ssl=True,
    user_agent="YourCustomUserAgent/1.0"
)
```

## Basic usage

Retrieve all users:

```python
users = client.get_all_users()  # call the method
print("Users:", users)
```

Create a new user:

```python
resp = client.create_user_account(
    username="newuser",
    email="newuser@example.com",
    passwd="securepassword",
    notify="no",
    ip="shared",           # one of: "shared", "sharedreseller", "assign"
    package="default",
    domain="newuserdomain.com"
)
print("Create user response:", resp)
```

## Methods (summary)

- get_all_resellers() -> List[Dict]: List all resellers.
- get_all_admins() -> List[Dict]: List all admins.
- get_all_users() -> List[Dict]: List all users.
- get_all_reseller_packages() -> List[Dict]
- get_all_user_packages() -> List[Dict]
- get_reseller_ip_list() -> List[str]
- get_admin_stats() -> Dict
- suspend_account(username: str) -> Dict
- activate_account(username: str) -> Dict

Utility methods:
- get_reseller_package(package_name: str) -> Dict
- get_user_package(package_name: str) -> Dict
- get_user_config(username: str) -> Dict
- get_user_usage(username: str) -> Dict
- get_user_domain(username: str) -> Dict
- create_admin_account(username: str, email: str, passwd: str, notify: str) -> Dict
- create_reseller_account(username: str, email: str, passwd: str, notify: str, ip: str, package: str, domain: str) -> Dict
- create_user_account(username: str, email: str, passwd: str, notify: str, ip: str, package: str, domain: str) -> Dict

Return types are approximations — check responses for the exact structure. Methods raise exceptions on network or HTTP errors (requests exceptions or custom client exceptions).

## Notes & best practices
- Use HTTPS (ssl=True) and a dedicated API account.
- Validate package and ip values before calling create_* methods.
- Wrap calls in try/except to handle network/HTTP errors.

## Contributing
Contributions welcome. Fork the repo, create a branch, add tests and submit a pull request.

## License
Apache License (see LICENSE file).

## Contact
For questions or support: miladkhoshdel@gmail.com
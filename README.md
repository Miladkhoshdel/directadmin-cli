# DirectAdminAPIClient

The `directadmin-cli` package provides a convenient interface for interacting with the DirectAdmin API. `BaseDirectAdminAPIClient` extends the `BaseDirectAdminAPIClient` class to offer specific methods for managing and retrieving information about resellers, admins, users, and various account types.

## Installation

To use this client, you'll need to have Python installed along with the `requests` library. You can install the required library using pip:

```bash
pip install directadmin-cli
```

## Usage

### Initialization

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

### Properties

- get_all_resellers: Retrieves a list of all resellers.
- get_all_admins: Retrieves a list of all admins.
- get_all_users: Retrieves a list of all users.
- get_all_reseller_packages: Retrieves a list of all reseller packages.
- get_all_user_packages: Retrieves a list of all user packages.
- get_reseller_ip_list: Retrieves a list of IP addresses associated with resellers.
- get_admin_stats: Retrieves statistics for the admin.

### Methods

- get_reseller_package(package_name: str) -> Dict[str, Any]: Retrieves information about a specific reseller package by name.
- get_user_package(package_name: str) -> Dict[str, Any]: Retrieves information about a specific user package by name.
- get_user_config(username: str) -> Dict[str, Any]: Retrieves configuration details for a specific user.
- get_user_usage(username: str) -> Dict[str, Any]: Retrieves usage statistics for a specific user.
- get_user_domain(username: str) -> Dict[str, Any]: Retrieves domain information for a specific user.
- create_admin_account(username: str, email: str, passwd: str, notify: str) -> Dict[str, Any]: Creates a new admin account with the specified details.
- create_reseller_account(username: str, email: str, passwd: str, notify: str, ip: str, package: str, domain: str) -> Dict[str, Any]: Creates a new reseller account with the specified details. The ip parameter must be one of "shared", "sharedreseller", or "assign".
- create_user_account(username: str, email: str, passwd: str, notify: str, ip: str, package: str, domain: str) -> Dict[str, Any]: Creates a new user account with the specified details.

## Example

```python
from directadmin.client import DirectAdminAPIClient

# Initialize the client
client = DirectAdminAPIClient(
    server="https://your-directadmin-server.com",
    username="your-username",
    password="your-password"
)

# Retrieve all users
users = client.get_all_users
print("Users:", users)

# Create a new user account
response = client.create_user_account(
    username="newuser",
    email="newuser@example.com",
    passwd="securepassword",
    notify="no",
    ip="shared",
    package="default",
    domain="newuserdomain.com"
)
print("Create User Response:", response)
```

## License
This project is licensed under the Apache License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

C## ontact
For any questions or support, please contact miladkhoshdel@gmail.com.
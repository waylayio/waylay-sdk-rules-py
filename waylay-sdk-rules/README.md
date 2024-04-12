# Waylay Rules Service
The REST api to manage rule tasks and rule templates in the Waylay platform.

This Python package is automatically generated based on the 
Waylay Rules OpenAPI specification (API version: 6.5.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/rules.html).

It consists of a plugin for the waylay-sdk-core package, and contains the Rules api methods.
Note that the typed model classes for all path params, query params, body params and responses for each of the api methods are contained in a separate package called waylay-sdk-rules-types.

## Requirements.
This package requires Python 3.9+.

## Installation
Typically this package is installed when installing the [waylay-sdk-core](https://pypi.org/project/waylay-sdk/) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-rules is included in:
- ```pip install waylay-sdk-core[rules]``` to install `waylay-sdk-core` along with only this service, or
- ```pip install waylay-sdk-core[services]``` to install `waylay-sdk-core` along with all services.
When the typed models are required, both waylay-sdk-rules and waylay-sdk-rules-types are included in:
- ```pip install waylay-sdk-core[rules,rules-types]``` to install `waylay-sdk-core` along with only this service including the typed models, or
- ```pip install waylay-sdk-core[services,services-types]``` to install `waylay-sdk-core` along with all services along with the typed models.

## Usage

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.version_response import VersionResponse
try:
    # Get Service Information
    # calls `GET /rules/v1`
    api_response = await waylay_client.rules.about.get(
    )
    print("The response of rules.about.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).
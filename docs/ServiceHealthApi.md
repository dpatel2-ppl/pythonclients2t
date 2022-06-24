# swagger_client.ServiceHealthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_status**](ServiceHealthApi.md#get_health_status) | **GET** /healthstatus | Returns the overall health of the service and optionally of the different subcomponents.


# **get_health_status**
> ServiceHealth get_health_status()

Returns the overall health of the service and optionally of the different subcomponents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ServiceHealthApi(swagger_client.ApiClient(configuration))

try:
    # Returns the overall health of the service and optionally of the different subcomponents.
    api_response = api_instance.get_health_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceHealthApi->get_health_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceHealth**](ServiceHealth.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


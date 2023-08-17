# swagger_client.SdrCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_sdr_categories_get**](SdrCategoriesApi.md#esa_api_v20_config_sdr_categories_get) | **GET** /esa/api/v2.0/config/sdr_categories | get sdr categories

# **esa_api_v20_config_sdr_categories_get**
> ConfigSdrCategories esa_api_v20_config_sdr_categories_get(device_type=device_type)

get sdr categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: UserSecurity
configuration = swagger_client.Configuration()
configuration.api_key['jwtToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwtToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SdrCategoriesApi(swagger_client.ApiClient(configuration))
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # get sdr categories
    api_response = api_instance.esa_api_v20_config_sdr_categories_get(device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SdrCategoriesApi->esa_api_v20_config_sdr_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ConfigSdrCategories**](ConfigSdrCategories.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


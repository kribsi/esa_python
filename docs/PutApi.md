# swagger_client.PutApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_local_quarantines_quarantine_name_put**](PutApi.md#esa_api_v20_config_local_quarantines_quarantine_name_put) | **PUT** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | edit pvo quarantine

# **esa_api_v20_config_local_quarantines_quarantine_name_put**
> ConfigLocalQuarantinesEditMessage esa_api_v20_config_local_quarantines_quarantine_name_put(body, quarantine_name, device_type=device_type)

edit pvo quarantine

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
api_instance = swagger_client.PutApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocalQuarantinesQuarantineNameBody() # LocalQuarantinesQuarantineNameBody | Edit pvo quarantine request body
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # edit pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_put(body, quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PutApi->esa_api_v20_config_local_quarantines_quarantine_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocalQuarantinesQuarantineNameBody**](LocalQuarantinesQuarantineNameBody.md)| Edit pvo quarantine request body | 
 **quarantine_name** | **str**|  | 
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesEditMessage**](ConfigLocalQuarantinesEditMessage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.QuarantineApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_local_quarantines_post**](QuarantineApi.md#esa_api_v20_config_local_quarantines_post) | **POST** /esa/api/v2.0/config/local_quarantines | add pvo quarantine
[**esa_api_v20_config_local_quarantines_quarantine_name_delete**](QuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_delete) | **DELETE** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | delete pvo quarantine
[**esa_api_v20_config_local_quarantines_quarantine_name_get**](QuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_get) | **GET** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | get pvo quarantine details
[**esa_api_v20_config_local_quarantines_quarantine_name_put**](QuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_put) | **PUT** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | edit pvo quarantine
[**esa_api_v20_config_quarantine_filters_quarantine_name_get**](QuarantineApi.md#esa_api_v20_config_quarantine_filters_quarantine_name_get) | **GET** /esa/api/v2.0/config/quarantine_filters/{quarantine_name} | get quarantine users
[**esa_api_v20_config_quarantine_users_get**](QuarantineApi.md#esa_api_v20_config_quarantine_users_get) | **GET** /esa/api/v2.0/config/quarantine_users | get quarantine users

# **esa_api_v20_config_local_quarantines_post**
> ConfigLocalQuarantinesAddMessage esa_api_v20_config_local_quarantines_post(body, device_type=device_type)

add pvo quarantine

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfigLocalQuarantinesBody() # ConfigLocalQuarantinesBody | Add pvo quarantine request body
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # add pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_post(body, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_local_quarantines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigLocalQuarantinesBody**](ConfigLocalQuarantinesBody.md)| Add pvo quarantine request body | 
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesAddMessage**](ConfigLocalQuarantinesAddMessage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_config_local_quarantines_quarantine_name_delete**
> ConfigLocalQuarantinesDelete esa_api_v20_config_local_quarantines_quarantine_name_delete(quarantine_name, device_type=device_type)

delete pvo quarantine

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # delete pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_delete(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_name** | **str**|  | 
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesDelete**](ConfigLocalQuarantinesDelete.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_config_local_quarantines_quarantine_name_get**
> ConfigLocalQuarantinesGet esa_api_v20_config_local_quarantines_quarantine_name_get(quarantine_name, device_type=device_type)

get pvo quarantine details

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get pvo quarantine details
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_get(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_name** | **str**|  | 
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesGet**](ConfigLocalQuarantinesGet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocalQuarantinesQuarantineNameBody() # LocalQuarantinesQuarantineNameBody | Edit pvo quarantine request body
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # edit pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_put(body, quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_put: %s\n" % e)
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

# **esa_api_v20_config_quarantine_filters_quarantine_name_get**
> ConfigLocalQuarantinesFilters esa_api_v20_config_quarantine_filters_quarantine_name_get(quarantine_name, device_type=device_type)

get quarantine users

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get quarantine users
    api_response = api_instance.esa_api_v20_config_quarantine_filters_quarantine_name_get(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_quarantine_filters_quarantine_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_name** | **str**|  | 
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesFilters**](ConfigLocalQuarantinesFilters.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_config_quarantine_users_get**
> ConfigLocalQuarantinesUsers esa_api_v20_config_quarantine_users_get(device_type=device_type)

get quarantine users

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
api_instance = swagger_client.QuarantineApi(swagger_client.ApiClient(configuration))
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get quarantine users
    api_response = api_instance.esa_api_v20_config_quarantine_users_get(device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuarantineApi->esa_api_v20_config_quarantine_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**|  | [optional] [default to sma]

### Return type

[**ConfigLocalQuarantinesUsers**](ConfigLocalQuarantinesUsers.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.SafelistApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_quarantine_safelist_delete**](SafelistApi.md#esa_api_v20_quarantine_safelist_delete) | **DELETE** /esa/api/v2.0/quarantine/safelist | Delete safelist entries
[**esa_api_v20_quarantine_safelist_get**](SafelistApi.md#esa_api_v20_quarantine_safelist_get) | **GET** /esa/api/v2.0/quarantine/safelist | Retrieve Safelist entries
[**esa_api_v20_quarantine_safelist_post**](SafelistApi.md#esa_api_v20_quarantine_safelist_post) | **POST** /esa/api/v2.0/quarantine/safelist | Add, edit and append Safelist entries

# **esa_api_v20_quarantine_safelist_delete**
> InlineResponse2004 esa_api_v20_quarantine_safelist_delete(body)

Delete safelist entries

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
api_instance = swagger_client.SafelistApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistBody() # QuarantineSafelistBody | Quarantine safelist delete request body

try:
    # Delete safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafelistApi->esa_api_v20_quarantine_safelist_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineSafelistBody**](QuarantineSafelistBody.md)| Quarantine safelist delete request body | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_quarantine_safelist_get**
> QuarantineSafelist esa_api_v20_quarantine_safelist_get(action=action, view_by=view_by, search=search, quarantine_type=quarantine_type, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)

Retrieve Safelist entries

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
api_instance = swagger_client.SafelistApi(swagger_client.ApiClient(configuration))
action = 'action_example' # str |  (optional)
view_by = 'view_by_example' # str |  (optional)
search = 'search_example' # str |  (optional)
quarantine_type = 'quarantine_type_example' # str |  (optional)
order_dir = 'order_dir_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)

try:
    # Retrieve Safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_get(action=action, view_by=view_by, search=search, quarantine_type=quarantine_type, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafelistApi->esa_api_v20_quarantine_safelist_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **view_by** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **quarantine_type** | **str**|  | [optional] 
 **order_dir** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 

### Return type

[**QuarantineSafelist**](QuarantineSafelist.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_quarantine_safelist_post**
> QuarantineSafelistPost esa_api_v20_quarantine_safelist_post(body)

Add, edit and append Safelist entries

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
api_instance = swagger_client.SafelistApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistPostRequestBody() # QuarantineSafelistPostRequestBody | Add, edit and append Safelist entries request body

try:
    # Add, edit and append Safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafelistApi->esa_api_v20_quarantine_safelist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineSafelistPostRequestBody**](QuarantineSafelistPostRequestBody.md)| Add, edit and append Safelist entries request body | 

### Return type

[**QuarantineSafelistPost**](QuarantineSafelistPost.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


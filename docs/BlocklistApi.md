# swagger_client.BlocklistApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_quarantine_blocklist_delete**](BlocklistApi.md#esa_api_v20_quarantine_blocklist_delete) | **DELETE** /esa/api/v2.0/quarantine/blocklist | Delete blocklist entries
[**esa_api_v20_quarantine_blocklist_get**](BlocklistApi.md#esa_api_v20_quarantine_blocklist_get) | **GET** /esa/api/v2.0/quarantine/blocklist | Retrieve Blocklist entries
[**esa_api_v20_quarantine_blocklist_post**](BlocklistApi.md#esa_api_v20_quarantine_blocklist_post) | **POST** /esa/api/v2.0/quarantine/blocklist | Add, edit and append Blocklist entries

# **esa_api_v20_quarantine_blocklist_delete**
> InlineResponse200 esa_api_v20_quarantine_blocklist_delete(body)

Delete blocklist entries

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
api_instance = swagger_client.BlocklistApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistBody() # QuarantineBlocklistBody | Quarantine blocklist delete request body

try:
    # Delete blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocklistApi->esa_api_v20_quarantine_blocklist_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineBlocklistBody**](QuarantineBlocklistBody.md)| Quarantine blocklist delete request body | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_quarantine_blocklist_get**
> QuarantineSafelist esa_api_v20_quarantine_blocklist_get(action=action, view_by=view_by, search=search, quarantine_type=quarantine_type, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)

Retrieve Blocklist entries

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
api_instance = swagger_client.BlocklistApi(swagger_client.ApiClient(configuration))
action = 'action_example' # str |  (optional)
view_by = 'view_by_example' # str |  (optional)
search = 'search_example' # str |  (optional)
quarantine_type = 'quarantine_type_example' # str |  (optional)
order_dir = 'order_dir_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)

try:
    # Retrieve Blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_get(action=action, view_by=view_by, search=search, quarantine_type=quarantine_type, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocklistApi->esa_api_v20_quarantine_blocklist_get: %s\n" % e)
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

# **esa_api_v20_quarantine_blocklist_post**
> QuarantineBlocklistPost esa_api_v20_quarantine_blocklist_post(body)

Add, edit and append Blocklist entries

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
api_instance = swagger_client.BlocklistApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistPostRequestBody() # QuarantineBlocklistPostRequestBody | Add, edit and append Blocklist entries request body

try:
    # Add, edit and append Blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocklistApi->esa_api_v20_quarantine_blocklist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineBlocklistPostRequestBody**](QuarantineBlocklistPostRequestBody.md)| Add, edit and append Blocklist entries request body | 

### Return type

[**QuarantineBlocklistPost**](QuarantineBlocklistPost.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


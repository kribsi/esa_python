# swagger_client.DeleteApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_local_quarantines_quarantine_name_delete**](DeleteApi.md#esa_api_v20_config_local_quarantines_quarantine_name_delete) | **DELETE** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | delete pvo quarantine
[**esa_api_v20_quarantine_blocklist_delete**](DeleteApi.md#esa_api_v20_quarantine_blocklist_delete) | **DELETE** /esa/api/v2.0/quarantine/blocklist | Delete blocklist entries
[**esa_api_v20_quarantine_messages_delete**](DeleteApi.md#esa_api_v20_quarantine_messages_delete) | **DELETE** /esa/api/v2.0/quarantine/messages | Delete messages that match various attribute
[**esa_api_v20_quarantine_messages_rules_delete**](DeleteApi.md#esa_api_v20_quarantine_messages_rules_delete) | **DELETE** /esa/api/v2.0/quarantine/messages/rules | Delete messages from the rule summary that match multiple attributes
[**esa_api_v20_quarantine_safelist_delete**](DeleteApi.md#esa_api_v20_quarantine_safelist_delete) | **DELETE** /esa/api/v2.0/quarantine/safelist | Delete safelist entries

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
api_instance = swagger_client.DeleteApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # delete pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_delete(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeleteApi->esa_api_v20_config_local_quarantines_quarantine_name_delete: %s\n" % e)
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
api_instance = swagger_client.DeleteApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistBody() # QuarantineBlocklistBody | Quarantine blocklist delete request body

try:
    # Delete blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeleteApi->esa_api_v20_quarantine_blocklist_delete: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_delete**
> QuarantineMessagesDelete esa_api_v20_quarantine_messages_delete(body)

Delete messages that match various attribute

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
api_instance = swagger_client.DeleteApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody1() # QuarantineMessagesBody1 | Quarantine message delete request body

try:
    # Delete messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeleteApi->esa_api_v20_quarantine_messages_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineMessagesBody1**](QuarantineMessagesBody1.md)| Quarantine message delete request body | 

### Return type

[**QuarantineMessagesDelete**](QuarantineMessagesDelete.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_quarantine_messages_rules_delete**
> QuarantineMessagesDelete esa_api_v20_quarantine_messages_rules_delete(body)

Delete messages from the rule summary that match multiple attributes

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
api_instance = swagger_client.DeleteApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantinePvoRulesDeleteRequestBody() # QuarantinePvoRulesDeleteRequestBody | Delete messages from the rule summary that match multiple attributes

try:
    # Delete messages from the rule summary that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_rules_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeleteApi->esa_api_v20_quarantine_messages_rules_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantinePvoRulesDeleteRequestBody**](QuarantinePvoRulesDeleteRequestBody.md)| Delete messages from the rule summary that match multiple attributes | 

### Return type

[**QuarantineMessagesDelete**](QuarantineMessagesDelete.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.DeleteApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistBody() # QuarantineSafelistBody | Quarantine safelist delete request body

try:
    # Delete safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeleteApi->esa_api_v20_quarantine_safelist_delete: %s\n" % e)
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


# swagger_client.PostApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_local_quarantines_post**](PostApi.md#esa_api_v20_config_local_quarantines_post) | **POST** /esa/api/v2.0/config/local_quarantines | add pvo quarantine
[**esa_api_v20_quarantine_blocklist_post**](PostApi.md#esa_api_v20_quarantine_blocklist_post) | **POST** /esa/api/v2.0/quarantine/blocklist | Add, edit and append Blocklist entries
[**esa_api_v20_quarantine_messages_post**](PostApi.md#esa_api_v20_quarantine_messages_post) | **POST** /esa/api/v2.0/quarantine/messages | Release messages that match various attribute
[**esa_api_v20_quarantine_messages_rules_post**](PostApi.md#esa_api_v20_quarantine_messages_rules_post) | **POST** /esa/api/v2.0/quarantine/messages/rules | Release messages from the rule summary that match multiple attributes
[**esa_api_v20_quarantine_safelist_post**](PostApi.md#esa_api_v20_quarantine_safelist_post) | **POST** /esa/api/v2.0/quarantine/safelist | Add, edit and append Safelist entries

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
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfigLocalQuarantinesBody() # ConfigLocalQuarantinesBody | Add pvo quarantine request body
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # add pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_post(body, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->esa_api_v20_config_local_quarantines_post: %s\n" % e)
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
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistPostRequestBody() # QuarantineBlocklistPostRequestBody | Add, edit and append Blocklist entries request body

try:
    # Add, edit and append Blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->esa_api_v20_quarantine_blocklist_post: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_post**
> InlineResponse2002 esa_api_v20_quarantine_messages_post(body)

Release messages that match various attribute

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
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody() # QuarantineMessagesBody | Quarantine message release request body

try:
    # Release messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->esa_api_v20_quarantine_messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantineMessagesBody**](QuarantineMessagesBody.md)| Quarantine message release request body | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_quarantine_messages_rules_post**
> QuarantineMessagesRelease esa_api_v20_quarantine_messages_rules_post(body)

Release messages from the rule summary that match multiple attributes

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
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantinePvoRulesReleaseRequestBody() # QuarantinePvoRulesReleaseRequestBody | Release messages from the rule summary that match multiple attributes

try:
    # Release messages from the rule summary that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_rules_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->esa_api_v20_quarantine_messages_rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuarantinePvoRulesReleaseRequestBody**](QuarantinePvoRulesReleaseRequestBody.md)| Release messages from the rule summary that match multiple attributes | 

### Return type

[**QuarantineMessagesRelease**](QuarantineMessagesRelease.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistPostRequestBody() # QuarantineSafelistPostRequestBody | Add, edit and append Safelist entries request body

try:
    # Add, edit and append Safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->esa_api_v20_quarantine_safelist_post: %s\n" % e)
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


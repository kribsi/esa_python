# swagger_client.PvoQuarantineApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_local_quarantines_post**](PvoQuarantineApi.md#esa_api_v20_config_local_quarantines_post) | **POST** /esa/api/v2.0/config/local_quarantines | add pvo quarantine
[**esa_api_v20_config_local_quarantines_quarantine_name_delete**](PvoQuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_delete) | **DELETE** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | delete pvo quarantine
[**esa_api_v20_config_local_quarantines_quarantine_name_get**](PvoQuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_get) | **GET** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | get pvo quarantine details
[**esa_api_v20_config_local_quarantines_quarantine_name_put**](PvoQuarantineApi.md#esa_api_v20_config_local_quarantines_quarantine_name_put) | **PUT** /esa/api/v2.0/config/local_quarantines/{quarantine_name} | edit pvo quarantine
[**esa_api_v20_config_quarantine_filters_quarantine_name_get**](PvoQuarantineApi.md#esa_api_v20_config_quarantine_filters_quarantine_name_get) | **GET** /esa/api/v2.0/config/quarantine_filters/{quarantine_name} | get quarantine users
[**esa_api_v20_config_quarantine_users_get**](PvoQuarantineApi.md#esa_api_v20_config_quarantine_users_get) | **GET** /esa/api/v2.0/config/quarantine_users | get quarantine users
[**esa_api_v20_quarantine_messages_attachment_get**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_attachment_get) | **GET** /esa/api/v2.0/quarantine/messages/attachment | Download an attachment accompanying a message in a quarantine
[**esa_api_v20_quarantine_messages_delete**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_delete) | **DELETE** /esa/api/v2.0/quarantine/messages | Delete messages that match various attribute
[**esa_api_v20_quarantine_messages_get**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_get) | **GET** /esa/api/v2.0/quarantine/messages | Search for messages in the spam quarantine that match multiple attributes
[**esa_api_v20_quarantine_messages_post**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_post) | **POST** /esa/api/v2.0/quarantine/messages | Release messages that match various attribute
[**esa_api_v20_quarantine_messages_rules_delete**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_rules_delete) | **DELETE** /esa/api/v2.0/quarantine/messages/rules | Delete messages from the rule summary that match multiple attributes
[**esa_api_v20_quarantine_messages_rules_get**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_rules_get) | **GET** /esa/api/v2.0/quarantine/messages/rules | Retrieve the rule summary
[**esa_api_v20_quarantine_messages_rules_post**](PvoQuarantineApi.md#esa_api_v20_quarantine_messages_rules_post) | **POST** /esa/api/v2.0/quarantine/messages/rules | Release messages from the rule summary that match multiple attributes
[**esa_api_v20_quarantine_rules_search_get**](PvoQuarantineApi.md#esa_api_v20_quarantine_rules_search_get) | **GET** /esa/api/v2.0/quarantine/rules_search | Search for messages in quarantine that match a specific rule ID

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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfigLocalQuarantinesBody() # ConfigLocalQuarantinesBody | Add pvo quarantine request body
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # add pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_post(body, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_local_quarantines_post: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # delete pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_delete(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_delete: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get pvo quarantine details
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_get(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_get: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocalQuarantinesQuarantineNameBody() # LocalQuarantinesQuarantineNameBody | Edit pvo quarantine request body
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # edit pvo quarantine
    api_response = api_instance.esa_api_v20_config_local_quarantines_quarantine_name_put(body, quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_local_quarantines_quarantine_name_put: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
quarantine_name = 'quarantine_name_example' # str | 
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get quarantine users
    api_response = api_instance.esa_api_v20_config_quarantine_filters_quarantine_name_get(quarantine_name, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_quarantine_filters_quarantine_name_get: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
device_type = 'sma' # str |  (optional) (default to sma)

try:
    # get quarantine users
    api_response = api_instance.esa_api_v20_config_quarantine_users_get(device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_config_quarantine_users_get: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_attachment_get**
> QuarantineMessagesPvoAttachment esa_api_v20_quarantine_messages_attachment_get(mid=mid, attachment_id=attachment_id, quarantine_type=quarantine_type)

Download an attachment accompanying a message in a quarantine

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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
mid = 'mid_example' # str |  (optional)
attachment_id = 'attachment_id_example' # str |  (optional)
quarantine_type = 'quarantine_type_example' # str |  (optional)

try:
    # Download an attachment accompanying a message in a quarantine
    api_response = api_instance.esa_api_v20_quarantine_messages_attachment_get(mid=mid, attachment_id=attachment_id, quarantine_type=quarantine_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_attachment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mid** | **str**|  | [optional] 
 **attachment_id** | **str**|  | [optional] 
 **quarantine_type** | **str**|  | [optional] 

### Return type

[**QuarantineMessagesPvoAttachment**](QuarantineMessagesPvoAttachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody1() # QuarantineMessagesBody1 | Quarantine message delete request body

try:
    # Delete messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_delete: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_get**
> InlineResponse2001 esa_api_v20_quarantine_messages_get(start_date=start_date, end_date=end_date, quarantine_type=quarantine_type, quarantines=quarantines, originating_esa_ip=originating_esa_ip, subject_filter_by=subject_filter_by, subject_filter_value=subject_filter_value, attachment_name=attachment_name, attachment_size_filter_by=attachment_size_filter_by, attachment_size_from_value=attachment_size_from_value, attachment_size_to_value=attachment_size_to_value, envelope_recipient_filter_by=envelope_recipient_filter_by, envelope_recipient_filter_value=envelope_recipient_filter_value, envelope_sender_filter_by=envelope_sender_filter_by, envelope_sender_filter_value=envelope_sender_filter_value, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)

Search for messages in the spam quarantine that match multiple attributes

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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
quarantine_type = 'quarantine_type_example' # str |  (optional)
quarantines = 'quarantines_example' # str |  (optional)
originating_esa_ip = 'originating_esa_ip_example' # str |  (optional)
subject_filter_by = 'subject_filter_by_example' # str |  (optional)
subject_filter_value = 'subject_filter_value_example' # str |  (optional)
attachment_name = 'attachment_name_example' # str |  (optional)
attachment_size_filter_by = 'attachment_size_filter_by_example' # str |  (optional)
attachment_size_from_value = 'attachment_size_from_value_example' # str |  (optional)
attachment_size_to_value = 'attachment_size_to_value_example' # str |  (optional)
envelope_recipient_filter_by = 'envelope_recipient_filter_by_example' # str |  (optional)
envelope_recipient_filter_value = 'envelope_recipient_filter_value_example' # str |  (optional)
envelope_sender_filter_by = 'envelope_sender_filter_by_example' # str |  (optional)
envelope_sender_filter_value = 'envelope_sender_filter_value_example' # str |  (optional)
order_dir = 'order_dir_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)

try:
    # Search for messages in the spam quarantine that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_get(start_date=start_date, end_date=end_date, quarantine_type=quarantine_type, quarantines=quarantines, originating_esa_ip=originating_esa_ip, subject_filter_by=subject_filter_by, subject_filter_value=subject_filter_value, attachment_name=attachment_name, attachment_size_filter_by=attachment_size_filter_by, attachment_size_from_value=attachment_size_from_value, attachment_size_to_value=attachment_size_to_value, envelope_recipient_filter_by=envelope_recipient_filter_by, envelope_recipient_filter_value=envelope_recipient_filter_value, envelope_sender_filter_by=envelope_sender_filter_by, envelope_sender_filter_value=envelope_sender_filter_value, order_dir=order_dir, order_by=order_by, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **quarantine_type** | **str**|  | [optional] 
 **quarantines** | **str**|  | [optional] 
 **originating_esa_ip** | **str**|  | [optional] 
 **subject_filter_by** | **str**|  | [optional] 
 **subject_filter_value** | **str**|  | [optional] 
 **attachment_name** | **str**|  | [optional] 
 **attachment_size_filter_by** | **str**|  | [optional] 
 **attachment_size_from_value** | **str**|  | [optional] 
 **attachment_size_to_value** | **str**|  | [optional] 
 **envelope_recipient_filter_by** | **str**|  | [optional] 
 **envelope_recipient_filter_value** | **str**|  | [optional] 
 **envelope_sender_filter_by** | **str**|  | [optional] 
 **envelope_sender_filter_value** | **str**|  | [optional] 
 **order_dir** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody() # QuarantineMessagesBody | Quarantine message release request body

try:
    # Release messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_post: %s\n" % e)
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantinePvoRulesDeleteRequestBody() # QuarantinePvoRulesDeleteRequestBody | Delete messages from the rule summary that match multiple attributes

try:
    # Delete messages from the rule summary that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_rules_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_rules_delete: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_rules_get**
> QuarantinePvoRules esa_api_v20_quarantine_messages_rules_get(quarantine_type=quarantine_type)

Retrieve the rule summary

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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
quarantine_type = 'quarantine_type_example' # str |  (optional)

try:
    # Retrieve the rule summary
    api_response = api_instance.esa_api_v20_quarantine_messages_rules_get(quarantine_type=quarantine_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_rules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_type** | **str**|  | [optional] 

### Return type

[**QuarantinePvoRules**](QuarantinePvoRules.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantinePvoRulesReleaseRequestBody() # QuarantinePvoRulesReleaseRequestBody | Release messages from the rule summary that match multiple attributes

try:
    # Release messages from the rule summary that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_rules_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_messages_rules_post: %s\n" % e)
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

# **esa_api_v20_quarantine_rules_search_get**
> QuarantineMessagesPvoRulesSearch esa_api_v20_quarantine_rules_search_get(quarantine_type=quarantine_type, rule_id=rule_id, order_by=order_by, order_dir=order_dir, offset=offset, limit=limit)

Search for messages in quarantine that match a specific rule ID

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
api_instance = swagger_client.PvoQuarantineApi(swagger_client.ApiClient(configuration))
quarantine_type = 'quarantine_type_example' # str |  (optional)
rule_id = 'rule_id_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
order_dir = 'order_dir_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)

try:
    # Search for messages in quarantine that match a specific rule ID
    api_response = api_instance.esa_api_v20_quarantine_rules_search_get(quarantine_type=quarantine_type, rule_id=rule_id, order_by=order_by, order_dir=order_dir, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PvoQuarantineApi->esa_api_v20_quarantine_rules_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantine_type** | **str**|  | [optional] 
 **rule_id** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order_dir** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 

### Return type

[**QuarantineMessagesPvoRulesSearch**](QuarantineMessagesPvoRulesSearch.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


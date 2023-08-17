# swagger_client.SpamQuarantineApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_quarantine_blocklist_delete**](SpamQuarantineApi.md#esa_api_v20_quarantine_blocklist_delete) | **DELETE** /esa/api/v2.0/quarantine/blocklist | Delete blocklist entries
[**esa_api_v20_quarantine_blocklist_get**](SpamQuarantineApi.md#esa_api_v20_quarantine_blocklist_get) | **GET** /esa/api/v2.0/quarantine/blocklist | Retrieve Blocklist entries
[**esa_api_v20_quarantine_blocklist_post**](SpamQuarantineApi.md#esa_api_v20_quarantine_blocklist_post) | **POST** /esa/api/v2.0/quarantine/blocklist | Add, edit and append Blocklist entries
[**esa_api_v20_quarantine_messages_delete**](SpamQuarantineApi.md#esa_api_v20_quarantine_messages_delete) | **DELETE** /esa/api/v2.0/quarantine/messages | Delete messages that match various attribute
[**esa_api_v20_quarantine_messages_details_get**](SpamQuarantineApi.md#esa_api_v20_quarantine_messages_details_get) | **GET** /esa/api/v2.0/quarantine/messages/details | Retrieve details of a message that match multiple attributes
[**esa_api_v20_quarantine_messages_get**](SpamQuarantineApi.md#esa_api_v20_quarantine_messages_get) | **GET** /esa/api/v2.0/quarantine/messages | Search for messages in the spam quarantine that match multiple attributes
[**esa_api_v20_quarantine_messages_post**](SpamQuarantineApi.md#esa_api_v20_quarantine_messages_post) | **POST** /esa/api/v2.0/quarantine/messages | Release messages that match various attribute
[**esa_api_v20_quarantine_safelist_delete**](SpamQuarantineApi.md#esa_api_v20_quarantine_safelist_delete) | **DELETE** /esa/api/v2.0/quarantine/safelist | Delete safelist entries
[**esa_api_v20_quarantine_safelist_get**](SpamQuarantineApi.md#esa_api_v20_quarantine_safelist_get) | **GET** /esa/api/v2.0/quarantine/safelist | Retrieve Safelist entries
[**esa_api_v20_quarantine_safelist_post**](SpamQuarantineApi.md#esa_api_v20_quarantine_safelist_post) | **POST** /esa/api/v2.0/quarantine/safelist | Add, edit and append Safelist entries

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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistBody() # QuarantineBlocklistBody | Quarantine blocklist delete request body

try:
    # Delete blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_blocklist_delete: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_blocklist_get: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineBlocklistPostRequestBody() # QuarantineBlocklistPostRequestBody | Add, edit and append Blocklist entries request body

try:
    # Add, edit and append Blocklist entries
    api_response = api_instance.esa_api_v20_quarantine_blocklist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_blocklist_post: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody1() # QuarantineMessagesBody1 | Quarantine message delete request body

try:
    # Delete messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_messages_delete: %s\n" % e)
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

# **esa_api_v20_quarantine_messages_details_get**
> InlineResponse2003 esa_api_v20_quarantine_messages_details_get(mid=mid, quarantine_type=quarantine_type)

Retrieve details of a message that match multiple attributes

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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
mid = 'mid_example' # str |  (optional)
quarantine_type = 'quarantine_type_example' # str |  (optional)

try:
    # Retrieve details of a message that match multiple attributes
    api_response = api_instance.esa_api_v20_quarantine_messages_details_get(mid=mid, quarantine_type=quarantine_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_messages_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mid** | **str**|  | [optional] 
 **quarantine_type** | **str**|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_messages_get: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineMessagesBody() # QuarantineMessagesBody | Quarantine message release request body

try:
    # Release messages that match various attribute
    api_response = api_instance.esa_api_v20_quarantine_messages_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_messages_post: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistBody() # QuarantineSafelistBody | Quarantine safelist delete request body

try:
    # Delete safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_delete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_safelist_delete: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_safelist_get: %s\n" % e)
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
api_instance = swagger_client.SpamQuarantineApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuarantineSafelistPostRequestBody() # QuarantineSafelistPostRequestBody | Add, edit and append Safelist entries request body

try:
    # Add, edit and append Safelist entries
    api_response = api_instance.esa_api_v20_quarantine_safelist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamQuarantineApi->esa_api_v20_quarantine_safelist_post: %s\n" % e)
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


# swagger_client.MailIncomingWebInteractionTrackUrlsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get**](MailIncomingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_web_interaction_track_urls/allowed | mail incoming web interaction track urls allowed
[**esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get**](MailIncomingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_web_interaction_track_urls/blocked | mail incoming web interaction track urls blocked
[**esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get**](MailIncomingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_web_interaction_track_urls | mail incoming web interaction track urls allowed
[**esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get**](MailIncomingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_web_interaction_track_urls/msg_count | mail incoming web interaction track urls msg count
[**esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get**](MailIncomingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_web_interaction_track_urls/unknown | mail incoming web interaction track urls unknown

# **esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get**
> ReportingMailIncomingWebInteractionTrackUrlsAllowed esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming web interaction track urls allowed

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
api_instance = swagger_client.MailIncomingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming web interaction track urls allowed
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_allowed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingWebInteractionTrackUrlsAllowed**](ReportingMailIncomingWebInteractionTrackUrlsAllowed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get**
> ReportingMailIncomingWebInteractionTrackUrlsBlocked esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming web interaction track urls blocked

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
api_instance = swagger_client.MailIncomingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming web interaction track urls blocked
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_blocked_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingWebInteractionTrackUrlsBlocked**](ReportingMailIncomingWebInteractionTrackUrlsBlocked.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get**
> ReportingMailIncomingWebInteractionTrackUrlsAllowed esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming web interaction track urls allowed

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
api_instance = swagger_client.MailIncomingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming web interaction track urls allowed
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingWebInteractionTrackUrlsAllowed**](ReportingMailIncomingWebInteractionTrackUrlsAllowed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get**
> ReportingMailIncomingWebInteractionTrackUrlsMsgCount esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming web interaction track urls msg count

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
api_instance = swagger_client.MailIncomingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming web interaction track urls msg count
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_msg_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingWebInteractionTrackUrlsMsgCount**](ReportingMailIncomingWebInteractionTrackUrlsMsgCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get**
> ReportingMailIncomingWebInteractionTrackUrlsUnknown esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming web interaction track urls unknown

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
api_instance = swagger_client.MailIncomingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming web interaction track urls unknown
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_incoming_web_interaction_track_urls_unknown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingWebInteractionTrackUrlsUnknown**](ReportingMailIncomingWebInteractionTrackUrlsUnknown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


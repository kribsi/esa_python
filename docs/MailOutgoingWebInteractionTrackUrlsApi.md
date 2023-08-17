# swagger_client.MailOutgoingWebInteractionTrackUrlsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get**](MailOutgoingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_urls/allowed | mail outgoing web interaction track urls allowed
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get**](MailOutgoingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_urls/blocked | mail outgoing web interaction track urls blocked
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get**](MailOutgoingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_urls | mail outgoing web interaction track urls allowed
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get**](MailOutgoingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_urls/msg_count | mail outgoing web interaction track urls msg count
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get**](MailOutgoingWebInteractionTrackUrlsApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_urls/unknown | mail outgoing web interaction track urls unknown

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get**
> ReportingMailOutgoingWebInteractionTrackUrlsAllowed esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track urls allowed

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track urls allowed
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_allowed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackUrlsAllowed**](ReportingMailOutgoingWebInteractionTrackUrlsAllowed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get**
> ReportingMailOutgoingWebInteractionTrackUrlsBlocked esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track urls blocked

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track urls blocked
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_blocked_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackUrlsBlocked**](ReportingMailOutgoingWebInteractionTrackUrlsBlocked.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get**
> ReportingMailOutgoingWebInteractionTrackUrlsAllowed esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track urls allowed

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track urls allowed
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackUrlsAllowed**](ReportingMailOutgoingWebInteractionTrackUrlsAllowed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get**
> ReportingMailOutgoingWebInteractionTrackUrlsMsgCount esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track urls msg count

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track urls msg count
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_msg_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackUrlsMsgCount**](ReportingMailOutgoingWebInteractionTrackUrlsMsgCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get**
> ReportingMailOutgoingWebInteractionTrackUrlsUnknown esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track urls unknown

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackUrlsApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track urls unknown
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackUrlsApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_urls_unknown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackUrlsUnknown**](ReportingMailOutgoingWebInteractionTrackUrlsUnknown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


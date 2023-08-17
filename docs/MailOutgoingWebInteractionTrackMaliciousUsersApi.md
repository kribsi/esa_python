# swagger_client.MailOutgoingWebInteractionTrackMaliciousUsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get**](MailOutgoingWebInteractionTrackMaliciousUsersApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_malicious_users | mail outgoing web interaction track malicious users users count
[**esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get**](MailOutgoingWebInteractionTrackMaliciousUsersApi.md#esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_web_interaction_track_malicious_users/users_count | mail outgoing web interaction track malicious users users count

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get**
> ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track malicious users users count

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackMaliciousUsersApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track malicious users users count
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackMaliciousUsersApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount**](ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get**
> ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing web interaction track malicious users users count

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
api_instance = swagger_client.MailOutgoingWebInteractionTrackMaliciousUsersApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing web interaction track malicious users users count
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingWebInteractionTrackMaliciousUsersApi->esa_api_v20_reporting_mail_outgoing_web_interaction_track_malicious_users_users_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount**](ReportingMailOutgoingWebInteractionTrackMaliciousUsersUsersCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


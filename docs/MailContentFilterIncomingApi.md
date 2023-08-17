# swagger_client.MailContentFilterIncomingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_content_filter_incoming_get**](MailContentFilterIncomingApi.md#esa_api_v20_reporting_mail_content_filter_incoming_get) | **GET** /esa/api/v2.0/reporting/mail_content_filter_incoming | mail content filter incoming recipients matched
[**esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get**](MailContentFilterIncomingApi.md#esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get) | **GET** /esa/api/v2.0/reporting/mail_content_filter_incoming/recipients_matched | mail content filter incoming recipients matched

# **esa_api_v20_reporting_mail_content_filter_incoming_get**
> ReportingMailContentFilterIncomingRecipientsMatched esa_api_v20_reporting_mail_content_filter_incoming_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail content filter incoming recipients matched

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
api_instance = swagger_client.MailContentFilterIncomingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail content filter incoming recipients matched
    api_response = api_instance.esa_api_v20_reporting_mail_content_filter_incoming_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailContentFilterIncomingApi->esa_api_v20_reporting_mail_content_filter_incoming_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailContentFilterIncomingRecipientsMatched**](ReportingMailContentFilterIncomingRecipientsMatched.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get**
> ReportingMailContentFilterIncomingRecipientsMatched esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail content filter incoming recipients matched

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
api_instance = swagger_client.MailContentFilterIncomingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail content filter incoming recipients matched
    api_response = api_instance.esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailContentFilterIncomingApi->esa_api_v20_reporting_mail_content_filter_incoming_recipients_matched_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailContentFilterIncomingRecipientsMatched**](ReportingMailContentFilterIncomingRecipientsMatched.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


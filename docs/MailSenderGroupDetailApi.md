# swagger_client.MailSenderGroupDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_group_detail_get**](MailSenderGroupDetailApi.md#esa_api_v20_reporting_mail_sender_group_detail_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_detail | mail sender group detail total connections
[**esa_api_v20_reporting_mail_sender_group_detail_total_connections_get**](MailSenderGroupDetailApi.md#esa_api_v20_reporting_mail_sender_group_detail_total_connections_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_detail/total_connections | mail sender group detail total connections

# **esa_api_v20_reporting_mail_sender_group_detail_get**
> ReportingMailSenderGroupDetailTotalConnections esa_api_v20_reporting_mail_sender_group_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group detail total connections

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
api_instance = swagger_client.MailSenderGroupDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group detail total connections
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupDetailApi->esa_api_v20_reporting_mail_sender_group_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupDetailTotalConnections**](ReportingMailSenderGroupDetailTotalConnections.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_group_detail_total_connections_get**
> ReportingMailSenderGroupDetailTotalConnections esa_api_v20_reporting_mail_sender_group_detail_total_connections_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group detail total connections

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
api_instance = swagger_client.MailSenderGroupDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group detail total connections
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_detail_total_connections_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupDetailApi->esa_api_v20_reporting_mail_sender_group_detail_total_connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupDetailTotalConnections**](ReportingMailSenderGroupDetailTotalConnections.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


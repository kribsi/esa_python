# swagger_client.MailSenderGroupSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get**](MailSenderGroupSummaryApi.md#esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_summary/connections_accept | mail sender group summary connections accept
[**esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get**](MailSenderGroupSummaryApi.md#esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_summary/connections_reject | mail sender group summary connections reject
[**esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get**](MailSenderGroupSummaryApi.md#esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_summary/connections_relay | mail sender group summary connections relay
[**esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get**](MailSenderGroupSummaryApi.md#esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_summary/connections_tcp_refuse | mail sender group summary connections tcp refuse
[**esa_api_v20_reporting_mail_sender_group_summary_get**](MailSenderGroupSummaryApi.md#esa_api_v20_reporting_mail_sender_group_summary_get) | **GET** /esa/api/v2.0/reporting/mail_sender_group_summary | mail sender group summary connections accept

# **esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get**
> ReportingMailSenderGroupSummaryConnectionsAccept esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group summary connections accept

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
api_instance = swagger_client.MailSenderGroupSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group summary connections accept
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupSummaryApi->esa_api_v20_reporting_mail_sender_group_summary_connections_accept_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupSummaryConnectionsAccept**](ReportingMailSenderGroupSummaryConnectionsAccept.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get**
> ReportingMailSenderGroupSummaryConnectionsReject esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group summary connections reject

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
api_instance = swagger_client.MailSenderGroupSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group summary connections reject
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupSummaryApi->esa_api_v20_reporting_mail_sender_group_summary_connections_reject_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupSummaryConnectionsReject**](ReportingMailSenderGroupSummaryConnectionsReject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get**
> ReportingMailSenderGroupSummaryConnectionsRelay esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group summary connections relay

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
api_instance = swagger_client.MailSenderGroupSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group summary connections relay
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupSummaryApi->esa_api_v20_reporting_mail_sender_group_summary_connections_relay_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupSummaryConnectionsRelay**](ReportingMailSenderGroupSummaryConnectionsRelay.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get**
> ReportingMailSenderGroupSummaryConnectionsTcpRefuse esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group summary connections tcp refuse

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
api_instance = swagger_client.MailSenderGroupSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group summary connections tcp refuse
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupSummaryApi->esa_api_v20_reporting_mail_sender_group_summary_connections_tcp_refuse_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupSummaryConnectionsTcpRefuse**](ReportingMailSenderGroupSummaryConnectionsTcpRefuse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_group_summary_get**
> ReportingMailSenderGroupSummaryConnectionsAccept esa_api_v20_reporting_mail_sender_group_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender group summary connections accept

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
api_instance = swagger_client.MailSenderGroupSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender group summary connections accept
    api_response = api_instance.esa_api_v20_reporting_mail_sender_group_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderGroupSummaryApi->esa_api_v20_reporting_mail_sender_group_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderGroupSummaryConnectionsAccept**](ReportingMailSenderGroupSummaryConnectionsAccept.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


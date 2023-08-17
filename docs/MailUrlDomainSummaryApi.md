# swagger_client.MailUrlDomainSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_url_domain_summary_get**](MailUrlDomainSummaryApi.md#esa_api_v20_reporting_mail_url_domain_summary_get) | **GET** /esa/api/v2.0/reporting/mail_url_domain_summary | mail url domain summary incoming count
[**esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get**](MailUrlDomainSummaryApi.md#esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get) | **GET** /esa/api/v2.0/reporting/mail_url_domain_summary/incoming_count | mail url domain summary incoming count
[**esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get**](MailUrlDomainSummaryApi.md#esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get) | **GET** /esa/api/v2.0/reporting/mail_url_domain_summary/outgoing_count | mail url domain summary outgoing count

# **esa_api_v20_reporting_mail_url_domain_summary_get**
> ReportingMailUrlDomainSummaryIncomingCount esa_api_v20_reporting_mail_url_domain_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail url domain summary incoming count

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
api_instance = swagger_client.MailUrlDomainSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail url domain summary incoming count
    api_response = api_instance.esa_api_v20_reporting_mail_url_domain_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailUrlDomainSummaryApi->esa_api_v20_reporting_mail_url_domain_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailUrlDomainSummaryIncomingCount**](ReportingMailUrlDomainSummaryIncomingCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get**
> ReportingMailUrlDomainSummaryIncomingCount esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail url domain summary incoming count

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
api_instance = swagger_client.MailUrlDomainSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail url domain summary incoming count
    api_response = api_instance.esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailUrlDomainSummaryApi->esa_api_v20_reporting_mail_url_domain_summary_incoming_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailUrlDomainSummaryIncomingCount**](ReportingMailUrlDomainSummaryIncomingCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get**
> ReportingMailUrlDomainSummaryOutgoingCount esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail url domain summary outgoing count

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
api_instance = swagger_client.MailUrlDomainSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail url domain summary outgoing count
    api_response = api_instance.esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailUrlDomainSummaryApi->esa_api_v20_reporting_mail_url_domain_summary_outgoing_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailUrlDomainSummaryOutgoingCount**](ReportingMailUrlDomainSummaryOutgoingCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.MailThreatfeedsIndicatorSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get**](MailThreatfeedsIndicatorSummaryApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_summary/domain | mail threatfeeds indicator summary domain
[**esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get**](MailThreatfeedsIndicatorSummaryApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_summary/file_hash | mail threatfeeds indicator summary file hash
[**esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get**](MailThreatfeedsIndicatorSummaryApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_summary | mail threatfeeds indicator summary domain
[**esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get**](MailThreatfeedsIndicatorSummaryApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_summary/url | mail threatfeeds indicator summary url

# **esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get**
> ReportingMailThreatfeedsIndicatorSummaryDomain esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator summary domain

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
api_instance = swagger_client.MailThreatfeedsIndicatorSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator summary domain
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorSummaryApi->esa_api_v20_reporting_mail_threatfeeds_indicator_summary_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorSummaryDomain**](ReportingMailThreatfeedsIndicatorSummaryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get**
> ReportingMailThreatfeedsIndicatorSummaryFileHash esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator summary file hash

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
api_instance = swagger_client.MailThreatfeedsIndicatorSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator summary file hash
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorSummaryApi->esa_api_v20_reporting_mail_threatfeeds_indicator_summary_file_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorSummaryFileHash**](ReportingMailThreatfeedsIndicatorSummaryFileHash.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get**
> ReportingMailThreatfeedsIndicatorSummaryDomain esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator summary domain

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
api_instance = swagger_client.MailThreatfeedsIndicatorSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator summary domain
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorSummaryApi->esa_api_v20_reporting_mail_threatfeeds_indicator_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorSummaryDomain**](ReportingMailThreatfeedsIndicatorSummaryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get**
> ReportingMailThreatfeedsIndicatorSummaryUrl esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator summary url

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
api_instance = swagger_client.MailThreatfeedsIndicatorSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator summary url
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorSummaryApi->esa_api_v20_reporting_mail_threatfeeds_indicator_summary_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorSummaryUrl**](ReportingMailThreatfeedsIndicatorSummaryUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


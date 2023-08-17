# swagger_client.MailThreatfeedsSourceDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail/domain_indicator | mail threatfeeds source detail domain indicator
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail/file_hash_indicator | mail threatfeeds source detail file hash indicator
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail | mail threatfeeds source detail ip indicator
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail/ip_indicator | mail threatfeeds source detail ip indicator
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail/total_messages_matched | mail threatfeeds source detail total messages matched
[**esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get**](MailThreatfeedsSourceDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_source_detail/url_indicator | mail threatfeeds source detail url indicator

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get**
> ReportingMailThreatfeedsSourceDetailDomainIndicator esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail domain indicator

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail domain indicator
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_domain_indicator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailDomainIndicator**](ReportingMailThreatfeedsSourceDetailDomainIndicator.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get**
> ReportingMailThreatfeedsSourceDetailFileHashIndicator esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail file hash indicator

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail file hash indicator
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_file_hash_indicator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailFileHashIndicator**](ReportingMailThreatfeedsSourceDetailFileHashIndicator.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_get**
> ReportingMailThreatfeedsSourceDetailIpIndicator esa_api_v20_reporting_mail_threatfeeds_source_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail ip indicator

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail ip indicator
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailIpIndicator**](ReportingMailThreatfeedsSourceDetailIpIndicator.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get**
> ReportingMailThreatfeedsSourceDetailIpIndicator esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail ip indicator

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail ip indicator
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_ip_indicator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailIpIndicator**](ReportingMailThreatfeedsSourceDetailIpIndicator.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get**
> ReportingMailThreatfeedsSourceDetailTotalMessagesMatched esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail total messages matched

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail total messages matched
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_total_messages_matched_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailTotalMessagesMatched**](ReportingMailThreatfeedsSourceDetailTotalMessagesMatched.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get**
> ReportingMailThreatfeedsSourceDetailUrlIndicator esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds source detail url indicator

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
api_instance = swagger_client.MailThreatfeedsSourceDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds source detail url indicator
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsSourceDetailApi->esa_api_v20_reporting_mail_threatfeeds_source_detail_url_indicator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsSourceDetailUrlIndicator**](ReportingMailThreatfeedsSourceDetailUrlIndicator.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


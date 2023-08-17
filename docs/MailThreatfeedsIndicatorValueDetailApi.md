# swagger_client.MailThreatfeedsIndicatorValueDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get**](MailThreatfeedsIndicatorValueDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_value_detail | mail threatfeeds indicator value detail ioc type
[**esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get**](MailThreatfeedsIndicatorValueDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_value_detail/ioc_consumed | mail threatfeeds indicator value detail ioc consumed
[**esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get**](MailThreatfeedsIndicatorValueDetailApi.md#esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get) | **GET** /esa/api/v2.0/reporting/mail_threatfeeds_indicator_value_detail/ioc_type | mail threatfeeds indicator value detail ioc type

# **esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get**
> ReportingMailThreatfeedsIndicatorValueDetailIocType esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator value detail ioc type

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
api_instance = swagger_client.MailThreatfeedsIndicatorValueDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator value detail ioc type
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorValueDetailApi->esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorValueDetailIocType**](ReportingMailThreatfeedsIndicatorValueDetailIocType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get**
> ReportingMailThreatfeedsIndicatorValueDetailIocConsumed esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator value detail ioc consumed

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
api_instance = swagger_client.MailThreatfeedsIndicatorValueDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator value detail ioc consumed
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorValueDetailApi->esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_consumed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorValueDetailIocConsumed**](ReportingMailThreatfeedsIndicatorValueDetailIocConsumed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get**
> ReportingMailThreatfeedsIndicatorValueDetailIocType esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail threatfeeds indicator value detail ioc type

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
api_instance = swagger_client.MailThreatfeedsIndicatorValueDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail threatfeeds indicator value detail ioc type
    api_response = api_instance.esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailThreatfeedsIndicatorValueDetailApi->esa_api_v20_reporting_mail_threatfeeds_indicator_value_detail_ioc_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailThreatfeedsIndicatorValueDetailIocType**](ReportingMailThreatfeedsIndicatorValueDetailIocType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


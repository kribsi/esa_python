# swagger_client.MailOutgoingAmpSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/blockedlist | mail outgoing amp summary blocked list
[**esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/clamav_lowrisk | mail outgoing amp summary clamav lowrisk
[**esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/clean | mail outgoing amp summary clean
[**esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/custom_threshold | mail outgoing amp summary custom threshold
[**esa_api_v20_reporting_mail_outgoing_amp_summary_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary | mail outgoing amp summary unscannable
[**esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/lowrisk | mail outgoing amp summary lowrisk
[**esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/malware | mail outgoing amp summary malware
[**esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/unknown | mail outgoing amp summary unknown
[**esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get**](MailOutgoingAmpSummaryApi.md#esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_amp_summary/unscannable | mail outgoing amp summary unscannable

# **esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get**
> ReportingMailOutgoingAmpSummaryBlockedlist esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary blocked list

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary blocked list
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_blockedlist_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryBlockedlist**](ReportingMailOutgoingAmpSummaryBlockedlist.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get**
> ReportingMailOutgoingAmpSummaryClamavLowrisk esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary clamav lowrisk

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary clamav lowrisk
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_clamav_lowrisk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryClamavLowrisk**](ReportingMailOutgoingAmpSummaryClamavLowrisk.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get**
> ReportingMailOutgoingAmpSummaryClean esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary clean

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary clean
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_clean_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryClean**](ReportingMailOutgoingAmpSummaryClean.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get**
> ReportingMailOutgoingAmpSummaryCustomThreshold esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary custom threshold

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary custom threshold
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_custom_threshold_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryCustomThreshold**](ReportingMailOutgoingAmpSummaryCustomThreshold.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_get**
> ReportingMailOutgoingAmpSummaryUnscannable esa_api_v20_reporting_mail_outgoing_amp_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary unscannable

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryUnscannable**](ReportingMailOutgoingAmpSummaryUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get**
> ReportingMailOutgoingAmpSummaryLowrisk esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary lowrisk

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary lowrisk
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_lowrisk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryLowrisk**](ReportingMailOutgoingAmpSummaryLowrisk.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get**
> ReportingMailOutgoingAmpSummaryMalware esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary malware

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary malware
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_malware_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryMalware**](ReportingMailOutgoingAmpSummaryMalware.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get**
> ReportingMailOutgoingAmpSummaryUnknown esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary unknown

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary unknown
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_unknown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryUnknown**](ReportingMailOutgoingAmpSummaryUnknown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get**
> ReportingMailOutgoingAmpSummaryUnscannable esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail outgoing amp summary unscannable

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
api_instance = swagger_client.MailOutgoingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail outgoing amp summary unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingAmpSummaryApi->esa_api_v20_reporting_mail_outgoing_amp_summary_unscannable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailOutgoingAmpSummaryUnscannable**](ReportingMailOutgoingAmpSummaryUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


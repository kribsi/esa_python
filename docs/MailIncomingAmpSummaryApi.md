# swagger_client.MailIncomingAmpSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/blockedlist | mail incoming amp summary blocked list
[**esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/clamav_lowrisk | mail incoming amp summary clamav lowrisk
[**esa_api_v20_reporting_mail_incoming_amp_summary_clean_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_clean_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/clean | mail incoming amp summary clean
[**esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/custom_threshold | mail incoming amp summary custom threshold
[**esa_api_v20_reporting_mail_incoming_amp_summary_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary | mail incoming amp summary unscannable
[**esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/lowrisk | mail incoming amp summary lowrisk
[**esa_api_v20_reporting_mail_incoming_amp_summary_malware_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_malware_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/malware | mail incoming amp summary malware
[**esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/unknown | mail incoming amp summary unknown
[**esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get**](MailIncomingAmpSummaryApi.md#esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get) | **GET** /esa/api/v2.0/reporting/mail_incoming_amp_summary/unscannable | mail incoming amp summary unscannable

# **esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get**
> ReportingMailIncomingAmpSummaryBlockedlist esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary blocked list

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary blocked list
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_blockedlist_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryBlockedlist**](ReportingMailIncomingAmpSummaryBlockedlist.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get**
> ReportingMailIncomingAmpSummaryClamavLowrisk esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary clamav lowrisk

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary clamav lowrisk
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_clamav_lowrisk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryClamavLowrisk**](ReportingMailIncomingAmpSummaryClamavLowrisk.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_clean_get**
> ReportingMailIncomingAmpSummaryClean esa_api_v20_reporting_mail_incoming_amp_summary_clean_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary clean

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary clean
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_clean_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_clean_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryClean**](ReportingMailIncomingAmpSummaryClean.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get**
> ReportingMailIncomingAmpSummaryCustomThreshold esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary custom threshold

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary custom threshold
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_custom_threshold_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryCustomThreshold**](ReportingMailIncomingAmpSummaryCustomThreshold.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_get**
> ReportingMailIncomingAmpSummaryUnscannable esa_api_v20_reporting_mail_incoming_amp_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary unscannable

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryUnscannable**](ReportingMailIncomingAmpSummaryUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get**
> ReportingMailIncomingAmpSummaryLowrisk esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary lowrisk

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary lowrisk
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_lowrisk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryLowrisk**](ReportingMailIncomingAmpSummaryLowrisk.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_malware_get**
> ReportingMailIncomingAmpSummaryMalware esa_api_v20_reporting_mail_incoming_amp_summary_malware_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary malware

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary malware
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_malware_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_malware_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryMalware**](ReportingMailIncomingAmpSummaryMalware.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get**
> ReportingMailIncomingAmpSummaryUnknown esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary unknown

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary unknown
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_unknown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryUnknown**](ReportingMailIncomingAmpSummaryUnknown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get**
> ReportingMailIncomingAmpSummaryUnscannable esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail incoming amp summary unscannable

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
api_instance = swagger_client.MailIncomingAmpSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail incoming amp summary unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailIncomingAmpSummaryApi->esa_api_v20_reporting_mail_incoming_amp_summary_unscannable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailIncomingAmpSummaryUnscannable**](ReportingMailIncomingAmpSummaryUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


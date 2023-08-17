# swagger_client.MailDmarcIncomingTrafficSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_failed_none | mail dmarc incoming traffic summary dmarc failed none
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_failed_quarantined | mail dmarc incoming traffic summary dmarc failed quarantined
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_failed_rejected | mail dmarc incoming traffic summary dmarc failed rejected
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_failed_total | mail dmarc incoming traffic summary dmarc failed total
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_passed | mail dmarc incoming traffic summary dmarc passed
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary/dmarc_total_attempted | mail dmarc incoming traffic summary dmarc total attempted
[**esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get**](MailDmarcIncomingTrafficSummaryApi.md#esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get) | **GET** /esa/api/v2.0/reporting/mail_dmarc_incoming_traffic_summary | mail dmarc incoming traffic summary dmarc passed

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcFailedNone esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc failed none

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc failed none
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_none_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcFailedNone**](ReportingMailDmarcIncomingTrafficSummaryDmarcFailedNone.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcFailedQuarantined esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc failed quarantined

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc failed quarantined
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_quarantined_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcFailedQuarantined**](ReportingMailDmarcIncomingTrafficSummaryDmarcFailedQuarantined.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcFailedRejected esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc failed rejected

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc failed rejected
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_rejected_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcFailedRejected**](ReportingMailDmarcIncomingTrafficSummaryDmarcFailedRejected.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcFailedTotal esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc failed total

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc failed total
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_failed_total_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcFailedTotal**](ReportingMailDmarcIncomingTrafficSummaryDmarcFailedTotal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcPassed esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc passed

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc passed
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_passed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcPassed**](ReportingMailDmarcIncomingTrafficSummaryDmarcPassed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcTotalAttempted esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc total attempted

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc total attempted
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_dmarc_total_attempted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcTotalAttempted**](ReportingMailDmarcIncomingTrafficSummaryDmarcTotalAttempted.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get**
> ReportingMailDmarcIncomingTrafficSummaryDmarcPassed esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dmarc incoming traffic summary dmarc passed

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
api_instance = swagger_client.MailDmarcIncomingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dmarc incoming traffic summary dmarc passed
    api_response = api_instance.esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDmarcIncomingTrafficSummaryApi->esa_api_v20_reporting_mail_dmarc_incoming_traffic_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDmarcIncomingTrafficSummaryDmarcPassed**](ReportingMailDmarcIncomingTrafficSummaryDmarcPassed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


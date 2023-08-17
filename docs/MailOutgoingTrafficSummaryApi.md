# swagger_client.MailOutgoingTrafficSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/detected_amp | mail outgoing traffic summary detected amp
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/detected_spam | mail outgoing traffic summary detected spam
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/detected_virus | mail outgoing traffic summary detected virus
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary | mail outgoing traffic summary total hard bounces
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/ims_spam_increment_over_case | mail outgoing traffic summary ims spam increment over case
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/malicious_url | mail outgoing traffic summary malicious url
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/threat_content_filter | mail outgoing traffic summary threat content filter
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_clean_recipients | mail outgoing traffic summary total clean recipients
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_dlp_incidents | mail outgoing traffic summary total dlp incidents
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_hard_bounces | mail outgoing traffic summary total hard bounces
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_recipients_delivered | mail outgoing traffic summary total recipients delivered
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_recipients | mail outgoing traffic summary total recipients
[**esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get**](MailOutgoingTrafficSummaryApi.md#esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get) | **GET** /esa/api/v2.0/reporting/mail_outgoing_traffic_summary/total_recipients_processed | mail outgoing traffic summary total recipients processed

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get**
> ReportingMailOutgoingTrafficSummaryDetectedAmp esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary detected amp

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary detected amp
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_amp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryDetectedAmp**](ReportingMailOutgoingTrafficSummaryDetectedAmp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get**
> ReportingMailOutgoingTrafficSummaryDetectedSpam esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary detected spam

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary detected spam
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_spam_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryDetectedSpam**](ReportingMailOutgoingTrafficSummaryDetectedSpam.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get**
> ReportingMailOutgoingTrafficSummaryDetectedVirus esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary detected virus

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary detected virus
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_detected_virus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryDetectedVirus**](ReportingMailOutgoingTrafficSummaryDetectedVirus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_get**
> ReportingMailOutgoingTrafficSummaryTotalHardBounces esa_api_v20_reporting_mail_outgoing_traffic_summary_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total hard bounces

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total hard bounces
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalHardBounces**](ReportingMailOutgoingTrafficSummaryTotalHardBounces.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get**
> ReportingMailOutgoingTrafficSummaryImsSpamIncrementOverCase esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary ims spam increment over case

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary ims spam increment over case
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_ims_spam_increment_over_case_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryImsSpamIncrementOverCase**](ReportingMailOutgoingTrafficSummaryImsSpamIncrementOverCase.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get**
> ReportingMailOutgoingTrafficSummaryMaliciousUrl esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary malicious url

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary malicious url
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_malicious_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryMaliciousUrl**](ReportingMailOutgoingTrafficSummaryMaliciousUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get**
> ReportingMailOutgoingTrafficSummaryThreatContentFilter esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary threat content filter

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary threat content filter
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_threat_content_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryThreatContentFilter**](ReportingMailOutgoingTrafficSummaryThreatContentFilter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get**
> ReportingMailOutgoingTrafficSummaryTotalCleanRecipients esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total clean recipients

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total clean recipients
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_clean_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalCleanRecipients**](ReportingMailOutgoingTrafficSummaryTotalCleanRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get**
> ReportingMailOutgoingTrafficSummaryTotalDlpIncidents esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total dlp incidents

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total dlp incidents
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_dlp_incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalDlpIncidents**](ReportingMailOutgoingTrafficSummaryTotalDlpIncidents.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get**
> ReportingMailOutgoingTrafficSummaryTotalHardBounces esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total hard bounces

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total hard bounces
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_hard_bounces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalHardBounces**](ReportingMailOutgoingTrafficSummaryTotalHardBounces.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get**
> ReportingMailOutgoingTrafficSummaryTotalRecipientsDelivered esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total recipients delivered

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total recipients delivered
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_delivered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalRecipientsDelivered**](ReportingMailOutgoingTrafficSummaryTotalRecipientsDelivered.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get**
> ReportingMailOutgoingTrafficSummaryTotalRecipients esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total recipients

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total recipients
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalRecipients**](ReportingMailOutgoingTrafficSummaryTotalRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get**
> ReportingMailOutgoingTrafficSummaryTotalRecipientsProcessed esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type)

mail outgoing traffic summary total recipients processed

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
api_instance = swagger_client.MailOutgoingTrafficSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)

try:
    # mail outgoing traffic summary total recipients processed
    api_response = api_instance.esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailOutgoingTrafficSummaryApi->esa_api_v20_reporting_mail_outgoing_traffic_summary_total_recipients_processed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]

### Return type

[**ReportingMailOutgoingTrafficSummaryTotalRecipientsProcessed**](ReportingMailOutgoingTrafficSummaryTotalRecipientsProcessed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


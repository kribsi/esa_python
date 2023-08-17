# swagger_client.MailSenderIpHostnameDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/detected_amp | mail sender ip hostname detail detected amp
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/detected_spam | mail sender ip hostname detail detected spam
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/detected_virus | mail sender ip hostname detail detected virus
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail | mail sender ip hostname detail detected amp
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/threat_content_filter | mail sender ip hostname detail threat content filter
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/total_clean_recipients | mail sender ip hostname detail total clean recipients
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/total_dlp_incidents | mail sender ip hostname detail total dlp incidents
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/total_recipients_processed | mail sender ip hostname detail total recipients processed
[**esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get**](MailSenderIpHostnameDetailApi.md#esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_sender_ip_hostname_detail/total_threat_recipients | mail sender ip hostname detail total threat recipients

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get**
> ReportingMailSenderIpHostnameDetailDetectedAmp esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail detected amp

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail detected amp
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_amp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailDetectedAmp**](ReportingMailSenderIpHostnameDetailDetectedAmp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get**
> ReportingMailSenderIpHostnameDetailDetectedSpam esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail detected spam

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail detected spam
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_spam_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailDetectedSpam**](ReportingMailSenderIpHostnameDetailDetectedSpam.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get**
> ReportingMailSenderIpHostnameDetailDetectedVirus esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail detected virus

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail detected virus
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_detected_virus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailDetectedVirus**](ReportingMailSenderIpHostnameDetailDetectedVirus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_get**
> ReportingMailSenderIpHostnameDetailDetectedAmp esa_api_v20_reporting_mail_sender_ip_hostname_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail detected amp

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail detected amp
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailDetectedAmp**](ReportingMailSenderIpHostnameDetailDetectedAmp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get**
> ReportingMailSenderIpHostnameDetailThreatContentFilter esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail threat content filter

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail threat content filter
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_threat_content_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailThreatContentFilter**](ReportingMailSenderIpHostnameDetailThreatContentFilter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get**
> ReportingMailSenderIpHostnameDetailTotalCleanRecipients esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail total clean recipients

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail total clean recipients
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_clean_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailTotalCleanRecipients**](ReportingMailSenderIpHostnameDetailTotalCleanRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get**
> ReportingMailSenderIpHostnameDetailTotalDlpIncidents esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail total dlp incidents

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail total dlp incidents
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_dlp_incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailTotalDlpIncidents**](ReportingMailSenderIpHostnameDetailTotalDlpIncidents.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get**
> ReportingMailSenderIpHostnameDetailTotalRecipientsProcessed esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail total recipients processed

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail total recipients processed
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_recipients_processed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailTotalRecipientsProcessed**](ReportingMailSenderIpHostnameDetailTotalRecipientsProcessed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get**
> ReportingMailSenderIpHostnameDetailTotalThreatRecipients esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender ip hostname detail total threat recipients

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
api_instance = swagger_client.MailSenderIpHostnameDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender ip hostname detail total threat recipients
    api_response = api_instance.esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderIpHostnameDetailApi->esa_api_v20_reporting_mail_sender_ip_hostname_detail_total_threat_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderIpHostnameDetailTotalThreatRecipients**](ReportingMailSenderIpHostnameDetailTotalThreatRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


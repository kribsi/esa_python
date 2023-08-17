# swagger_client.MailSenderDomainDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/detected_amp | mail sender domain detail detected amp
[**esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/detected_spam | mail sender domain detail detected spam
[**esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/detected_virus | mail sender domain detail detected virus
[**esa_api_v20_reporting_mail_sender_domain_detail_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail | mail sender domain detail detected amp
[**esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/threat_content_filter | mail sender domain detail threat content filter
[**esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/total_clean_recipients | mail sender domain detail total clean recipients
[**esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/total_dlp_incidents | mail sender domain detail total dlp incidents
[**esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/total_recipients_processed | mail sender domain detail total recipients processed
[**esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get**](MailSenderDomainDetailApi.md#esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_detail/total_threat_recipients | mail sender domain detail total threat recipients

# **esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get**
> ReportingMailSenderDomainDetailDetectedAmp esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail detected amp

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail detected amp
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailDetectedAmp**](ReportingMailSenderDomainDetailDetectedAmp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get**
> ReportingMailSenderDomainDetailDetectedSpam esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail detected spam

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail detected spam
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailDetectedSpam**](ReportingMailSenderDomainDetailDetectedSpam.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get**
> ReportingMailSenderDomainDetailDetectedVirus esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail detected virus

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail detected virus
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailDetectedVirus**](ReportingMailSenderDomainDetailDetectedVirus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_get**
> ReportingMailSenderDomainDetailDetectedAmp esa_api_v20_reporting_mail_sender_domain_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail detected amp

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail detected amp
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailDetectedAmp**](ReportingMailSenderDomainDetailDetectedAmp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get**
> ReportingMailSenderDomainDetailThreatContentFilter esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail threat content filter

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail threat content filter
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailThreatContentFilter**](ReportingMailSenderDomainDetailThreatContentFilter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get**
> ReportingMailSenderDomainDetailTotalCleanRecipients esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail total clean recipients

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail total clean recipients
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailTotalCleanRecipients**](ReportingMailSenderDomainDetailTotalCleanRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get**
> ReportingMailSenderDomainDetailTotalDlpIncidents esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail total dlp incidents

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail total dlp incidents
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailTotalDlpIncidents**](ReportingMailSenderDomainDetailTotalDlpIncidents.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get**
> ReportingMailSenderDomainDetailTotalRecipientsProcessed esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail total recipients processed

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail total recipients processed
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailTotalRecipientsProcessed**](ReportingMailSenderDomainDetailTotalRecipientsProcessed.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get**
> ReportingMailSenderDomainDetailTotalThreatRecipients esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain detail total threat recipients

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
api_instance = swagger_client.MailSenderDomainDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain detail total threat recipients
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainDetailApi->esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainDetailTotalThreatRecipients**](ReportingMailSenderDomainDetailTotalThreatRecipients.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


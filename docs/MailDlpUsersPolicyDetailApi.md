# swagger_client.MailDlpUsersPolicyDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail | mail dlp users policy detail outgoing dlp incidents critical
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_action_delivered | mail dlp users policy detail outgoing dlp action delivered
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_action_dropped | mail dlp users policy detail outgoing dlp action dropped
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_action_encrypted | mail dlp users policy detail outgoing dlp action encrypted
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_action_quarantined | mail dlp users policy detail outgoing dlp action quarantined
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_incidents_critical | mail dlp users policy detail outgoing dlp incidents critical
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_incidents_high | mail dlp users policy detail outgoing dlp incidents high
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_incidents_low | mail dlp users policy detail outgoing dlp incidents low
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/outgoing_dlp_incidents_medium | mail dlp users policy detail outgoing dlp incidents medium
[**esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get**](MailDlpUsersPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_users_policy_detail/total_dlp_incidents | mail dlp users policy detail total dlp incidents

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical esa_api_v20_reporting_mail_dlp_users_policy_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp incidents critical

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp incidents critical
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical**](ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDelivered esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp action delivered

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp action delivered
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_delivered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDelivered**](ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDelivered.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDropped esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp action dropped

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp action dropped
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_dropped_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDropped**](ReportingMailDlpUsersPolicyDetailOutgoingDlpActionDropped.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpActionEncrypted esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp action encrypted

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp action encrypted
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_encrypted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpActionEncrypted**](ReportingMailDlpUsersPolicyDetailOutgoingDlpActionEncrypted.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpActionQuarantined esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp action quarantined

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp action quarantined
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_action_quarantined_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpActionQuarantined**](ReportingMailDlpUsersPolicyDetailOutgoingDlpActionQuarantined.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp incidents critical

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp incidents critical
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_critical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical**](ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsCritical.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsHigh esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp incidents high

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp incidents high
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_high_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsHigh**](ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsHigh.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsLow esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp incidents low

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp incidents low
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_low_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsLow**](ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsLow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get**
> ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsMedium esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail outgoing dlp incidents medium

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail outgoing dlp incidents medium
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_outgoing_dlp_incidents_medium_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsMedium**](ReportingMailDlpUsersPolicyDetailOutgoingDlpIncidentsMedium.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get**
> ReportingMailDlpUsersPolicyDetailTotalDlpIncidents esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp users policy detail total dlp incidents

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
api_instance = swagger_client.MailDlpUsersPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp users policy detail total dlp incidents
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpUsersPolicyDetailApi->esa_api_v20_reporting_mail_dlp_users_policy_detail_total_dlp_incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpUsersPolicyDetailTotalDlpIncidents**](ReportingMailDlpUsersPolicyDetailTotalDlpIncidents.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


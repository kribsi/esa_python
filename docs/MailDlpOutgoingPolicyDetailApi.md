# swagger_client.MailDlpOutgoingPolicyDetailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_action_delivered | mail dlp outgoing policy detail dlp action delivered
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_action_dropped | mail dlp outgoing policy detail dlp action dropped
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_action_encrypted | mail dlp outgoing policy detail dlp action encrypted
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_incidents_critical | mail dlp outgoing policy detail dlp incidents critical
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_incidents_high | mail dlp outgoing policy detail dlp incidents high
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_incidents_low | mail dlp outgoing policy detail dlp incidents low
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/dlp_incidents_medium | mail dlp outgoing policy detail dlp incidents medium
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail | mail dlp outgoing policy detail dlp incidents low
[**esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get**](MailDlpOutgoingPolicyDetailApi.md#esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get) | **GET** /esa/api/v2.0/reporting/mail_dlp_outgoing_policy_detail/total_dlp_incidents | mail dlp outgoing policy detail total dlp incidents

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get**
> ReportingMailDlpOutgoingPolicyDetailDlpActionDelivered esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp action delivered

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp action delivered
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_delivered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpActionDelivered**](ReportingMailDlpOutgoingPolicyDetailDlpActionDelivered.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get**
> ReportingMailDlpOutgoingPolicyDetailDlpActionDropped esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp action dropped

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp action dropped
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_dropped_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpActionDropped**](ReportingMailDlpOutgoingPolicyDetailDlpActionDropped.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get**
> ReportingMailDlpOutgoingPolicyDetailDlpActionEncrypted esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp action encrypted

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp action encrypted
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_action_encrypted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpActionEncrypted**](ReportingMailDlpOutgoingPolicyDetailDlpActionEncrypted.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get**
> ReportingMailDlpOutgoingPolicyDetailDlpIncidentsCritical esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp incidents critical

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp incidents critical
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_critical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpIncidentsCritical**](ReportingMailDlpOutgoingPolicyDetailDlpIncidentsCritical.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get**
> ReportingMailDlpOutgoingPolicyDetailDlpIncidentsHigh esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp incidents high

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp incidents high
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_high_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpIncidentsHigh**](ReportingMailDlpOutgoingPolicyDetailDlpIncidentsHigh.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get**
> ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp incidents low

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp incidents low
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_low_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow**](ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get**
> ReportingMailDlpOutgoingPolicyDetailDlpIncidentsMedium esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp incidents medium

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp incidents medium
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_dlp_incidents_medium_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpIncidentsMedium**](ReportingMailDlpOutgoingPolicyDetailDlpIncidentsMedium.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get**
> ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail dlp incidents low

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail dlp incidents low
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow**](ReportingMailDlpOutgoingPolicyDetailDlpIncidentsLow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get**
> ReportingMailDlpOutgoingPolicyDetailTotalDlpIncidents esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail dlp outgoing policy detail total dlp incidents

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
api_instance = swagger_client.MailDlpOutgoingPolicyDetailApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail dlp outgoing policy detail total dlp incidents
    api_response = api_instance.esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailDlpOutgoingPolicyDetailApi->esa_api_v20_reporting_mail_dlp_outgoing_policy_detail_total_dlp_incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailDlpOutgoingPolicyDetailTotalDlpIncidents**](ReportingMailDlpOutgoingPolicyDetailTotalDlpIncidents.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


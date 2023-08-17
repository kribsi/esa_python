# swagger_client.MailMailboxAutoRemediationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation/action | mail mailbox auto remediation action
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation/completed_timestamp | mail mailbox auto remediation completed timestamp
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation/filenames | mail mailbox auto remediation filenames
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation | mail mailbox auto remediation
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation/rcpts_failure | mail mailbox auto remediation rcpts failure
[**esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get**](MailMailboxAutoRemediationApi.md#esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get) | **GET** /esa/api/v2.0/reporting/mail_mailbox_auto_remediation/rcpts_success | mail mailbox auto remediation rcpts success

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get**
> ReportingMailMailboxAutoRemediationAction esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation action

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation action
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_action_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediationAction**](ReportingMailMailboxAutoRemediationAction.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get**
> ReportingMailMailboxAutoRemediationCompletedTimestamp esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation completed timestamp

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation completed timestamp
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_completed_timestamp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediationCompletedTimestamp**](ReportingMailMailboxAutoRemediationCompletedTimestamp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get**
> ReportingMailMailboxAutoRemediationFilenames esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation filenames

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation filenames
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_filenames_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediationFilenames**](ReportingMailMailboxAutoRemediationFilenames.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_get**
> ReportingMailMailboxAutoRemediation esa_api_v20_reporting_mail_mailbox_auto_remediation_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediation**](ReportingMailMailboxAutoRemediation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get**
> ReportingMailMailboxAutoRemediationRcptsFailure esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation rcpts failure

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation rcpts failure
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_failure_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediationRcptsFailure**](ReportingMailMailboxAutoRemediationRcptsFailure.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get**
> ReportingMailMailboxAutoRemediationRcptsSuccess esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail mailbox auto remediation rcpts success

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
api_instance = swagger_client.MailMailboxAutoRemediationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail mailbox auto remediation rcpts success
    api_response = api_instance.esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailMailboxAutoRemediationApi->esa_api_v20_reporting_mail_mailbox_auto_remediation_rcpts_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailMailboxAutoRemediationRcptsSuccess**](ReportingMailMailboxAutoRemediationRcptsSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


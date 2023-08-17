# swagger_client.MailVofThreatsByTimeThresholdApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get**](MailVofThreatsByTimeThresholdApi.md#esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get) | **GET** /esa/api/v2.0/reporting/mail_vof_threats_by_time_threshold | mail vof threats by time threshold quarantine message exit
[**esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get**](MailVofThreatsByTimeThresholdApi.md#esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get) | **GET** /esa/api/v2.0/reporting/mail_vof_threats_by_time_threshold/local_store_quarantine_message_exit | mail vof threats by time threshold local store quarantine message exit
[**esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get**](MailVofThreatsByTimeThresholdApi.md#esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get) | **GET** /esa/api/v2.0/reporting/mail_vof_threats_by_time_threshold/quarantine_message_exit | mail vof threats by time threshold quarantine message exit

# **esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get**
> ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail vof threats by time threshold quarantine message exit

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
api_instance = swagger_client.MailVofThreatsByTimeThresholdApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail vof threats by time threshold quarantine message exit
    api_response = api_instance.esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailVofThreatsByTimeThresholdApi->esa_api_v20_reporting_mail_vof_threats_by_time_threshold_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit**](ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get**
> ReportingMailVofThreatsByTimeThresholdLocalStoreQuarantineMessageExit esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail vof threats by time threshold local store quarantine message exit

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
api_instance = swagger_client.MailVofThreatsByTimeThresholdApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail vof threats by time threshold local store quarantine message exit
    api_response = api_instance.esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailVofThreatsByTimeThresholdApi->esa_api_v20_reporting_mail_vof_threats_by_time_threshold_local_store_quarantine_message_exit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailVofThreatsByTimeThresholdLocalStoreQuarantineMessageExit**](ReportingMailVofThreatsByTimeThresholdLocalStoreQuarantineMessageExit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get**
> ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail vof threats by time threshold quarantine message exit

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
api_instance = swagger_client.MailVofThreatsByTimeThresholdApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail vof threats by time threshold quarantine message exit
    api_response = api_instance.esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailVofThreatsByTimeThresholdApi->esa_api_v20_reporting_mail_vof_threats_by_time_threshold_quarantine_message_exit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit**](ReportingMailVofThreatsByTimeThresholdQuarantineMessageExit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


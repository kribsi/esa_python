# swagger_client.MailVofThreatsByLevelApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_vof_threats_by_level_get**](MailVofThreatsByLevelApi.md#esa_api_v20_reporting_mail_vof_threats_by_level_get) | **GET** /esa/api/v2.0/reporting/mail_vof_threats_by_level | mail vof threats by level threat detected
[**esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get**](MailVofThreatsByLevelApi.md#esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get) | **GET** /esa/api/v2.0/reporting/mail_vof_threats_by_level/threat_detected | mail vof threats by level threat detected

# **esa_api_v20_reporting_mail_vof_threats_by_level_get**
> ReportingMailVofThreatsByLevelThreatDetected esa_api_v20_reporting_mail_vof_threats_by_level_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail vof threats by level threat detected

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
api_instance = swagger_client.MailVofThreatsByLevelApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail vof threats by level threat detected
    api_response = api_instance.esa_api_v20_reporting_mail_vof_threats_by_level_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailVofThreatsByLevelApi->esa_api_v20_reporting_mail_vof_threats_by_level_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailVofThreatsByLevelThreatDetected**](ReportingMailVofThreatsByLevelThreatDetected.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get**
> ReportingMailVofThreatsByLevelThreatDetected esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail vof threats by level threat detected

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
api_instance = swagger_client.MailVofThreatsByLevelApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail vof threats by level threat detected
    api_response = api_instance.esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailVofThreatsByLevelApi->esa_api_v20_reporting_mail_vof_threats_by_level_threat_detected_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailVofThreatsByLevelThreatDetected**](ReportingMailVofThreatsByLevelThreatDetected.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


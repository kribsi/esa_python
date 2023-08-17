# swagger_client.MailAmpReputationUpdateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_amp_reputation_update_console_url_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_console_url_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update/console_url | mail amp reputation update console url
[**esa_api_v20_reporting_mail_amp_reputation_update_filenames_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_filenames_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update/filenames | mail amp reputation update filenames
[**esa_api_v20_reporting_mail_amp_reputation_update_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update | mail amp reputation update timestamped tuple
[**esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update/msg_direction | mail amp reputation update msg direction
[**esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update/old_disposition | mail amp reputation update old disposition
[**esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get**](MailAmpReputationUpdateApi.md#esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get) | **GET** /esa/api/v2.0/reporting/mail_amp_reputation_update/timestamped_tuple | mail amp reputation update timestamped tuple

# **esa_api_v20_reporting_mail_amp_reputation_update_console_url_get**
> ReportingMailAmpReputationUpdateConsoleUrl esa_api_v20_reporting_mail_amp_reputation_update_console_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update console url

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update console url
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_console_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_console_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateConsoleUrl**](ReportingMailAmpReputationUpdateConsoleUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_reputation_update_filenames_get**
> ReportingMailAmpReputationUpdateFilenames esa_api_v20_reporting_mail_amp_reputation_update_filenames_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update filenames

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update filenames
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_filenames_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_filenames_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateFilenames**](ReportingMailAmpReputationUpdateFilenames.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_reputation_update_get**
> ReportingMailAmpReputationUpdateTimestampedTuple esa_api_v20_reporting_mail_amp_reputation_update_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update timestamped tuple

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update timestamped tuple
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateTimestampedTuple**](ReportingMailAmpReputationUpdateTimestampedTuple.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get**
> ReportingMailAmpReputationUpdateMsgDirection esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update msg direction

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update msg direction
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_msg_direction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateMsgDirection**](ReportingMailAmpReputationUpdateMsgDirection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get**
> ReportingMailAmpReputationUpdateOldDisposition esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update old disposition

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update old disposition
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_old_disposition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateOldDisposition**](ReportingMailAmpReputationUpdateOldDisposition.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get**
> ReportingMailAmpReputationUpdateTimestampedTuple esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp reputation update timestamped tuple

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
api_instance = swagger_client.MailAmpReputationUpdateApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp reputation update timestamped tuple
    api_response = api_instance.esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpReputationUpdateApi->esa_api_v20_reporting_mail_amp_reputation_update_timestamped_tuple_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpReputationUpdateTimestampedTuple**](ReportingMailAmpReputationUpdateTimestampedTuple.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


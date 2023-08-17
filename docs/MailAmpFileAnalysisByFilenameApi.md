# swagger_client.MailAmpFileAnalysisByFilenameApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/completed_timestamp | mail amp file analysis by filename completed timestamp
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/console_url | mail amp file analysis by filename console url
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename | mail amp file analysis by filename completed timestamp
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/interim_verdict | mail amp file analysis by filename interim verdict
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/msg_direction | mail amp file analysis by filename msg direction
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/run_id | mail amp file analysis by filename run id
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/score | mail amp file analysis by filename score
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/status | mail amp file analysis by filename status
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/submit_timestamp | mail amp file analysis by filename submit timestamp
[**esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get**](MailAmpFileAnalysisByFilenameApi.md#esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get) | **GET** /esa/api/v2.0/reporting/mail_amp_file_analysis_by_filename/url | mail amp file analysis by filename url

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get**
> ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename completed timestamp

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename completed timestamp
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_completed_timestamp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp**](ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get**
> ReportingMailAmpFileAnalysisByFilenameConsoleUrl esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename console url

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename console url
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_console_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameConsoleUrl**](ReportingMailAmpFileAnalysisByFilenameConsoleUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get**
> ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename completed timestamp

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename completed timestamp
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp**](ReportingMailAmpFileAnalysisByFilenameCompletedTimestamp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get**
> ReportingMailAmpFileAnalysisByFilenameInterimVerdict esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename interim verdict

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename interim verdict
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_interim_verdict_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameInterimVerdict**](ReportingMailAmpFileAnalysisByFilenameInterimVerdict.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get**
> ReportingMailAmpFileAnalysisByFilenameMsgDirection esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename msg direction

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename msg direction
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_msg_direction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameMsgDirection**](ReportingMailAmpFileAnalysisByFilenameMsgDirection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get**
> ReportingMailAmpFileAnalysisByFilenameRunId esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename run id

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename run id
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_run_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameRunId**](ReportingMailAmpFileAnalysisByFilenameRunId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get**
> ReportingMailAmpFileAnalysisByFilenameScore esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename score

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename score
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_score_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameScore**](ReportingMailAmpFileAnalysisByFilenameScore.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get**
> ReportingMailAmpFileAnalysisByFilenameStatus esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename status

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename status
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameStatus**](ReportingMailAmpFileAnalysisByFilenameStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get**
> ReportingMailAmpFileAnalysisByFilenameSubmitTimestamp esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename submit timestamp

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename submit timestamp
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_submit_timestamp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameSubmitTimestamp**](ReportingMailAmpFileAnalysisByFilenameSubmitTimestamp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get**
> ReportingMailAmpFileAnalysisByFilenameUrl esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail amp file analysis by filename url

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
api_instance = swagger_client.MailAmpFileAnalysisByFilenameApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail amp file analysis by filename url
    api_response = api_instance.esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAmpFileAnalysisByFilenameApi->esa_api_v20_reporting_mail_amp_file_analysis_by_filename_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAmpFileAnalysisByFilenameUrl**](ReportingMailAmpFileAnalysisByFilenameUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


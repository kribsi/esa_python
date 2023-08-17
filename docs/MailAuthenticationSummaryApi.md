# swagger_client.MailAuthenticationSummaryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_authentication_summary_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary | mail authentication summary received conn cert fail
[**esa_api_v20_reporting_mail_authentication_summary_received_auth_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_auth_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_auth | mail authentication summary received auth
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_auth_fail | mail authentication summary received conn auth fail
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_auth_success | mail authentication summary received conn auth success
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_cert_fail | mail authentication summary received conn cert fail
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_cert_success | mail authentication summary received conn cert success
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_noauth | mail authentication summary received conn noauth
[**esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_conn_total | mail authentication summary received conn total
[**esa_api_v20_reporting_mail_authentication_summary_received_noauth_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_noauth_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_noauth | mail authentication summary received noauth
[**esa_api_v20_reporting_mail_authentication_summary_received_total_get**](MailAuthenticationSummaryApi.md#esa_api_v20_reporting_mail_authentication_summary_received_total_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_summary/received_total | mail authentication summary received total

# **esa_api_v20_reporting_mail_authentication_summary_get**
> ReportingMailAuthenticationSummaryReceivedConnCertFail esa_api_v20_reporting_mail_authentication_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn cert fail

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn cert fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnCertFail**](ReportingMailAuthenticationSummaryReceivedConnCertFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_auth_get**
> ReportingMailAuthenticationSummaryReceivedAuth esa_api_v20_reporting_mail_authentication_summary_received_auth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received auth

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received auth
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_auth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_auth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedAuth**](ReportingMailAuthenticationSummaryReceivedAuth.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get**
> ReportingMailAuthenticationSummaryReceivedConnAuthFail esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn auth fail

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn auth fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnAuthFail**](ReportingMailAuthenticationSummaryReceivedConnAuthFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get**
> ReportingMailAuthenticationSummaryReceivedConnAuthSuccess esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn auth success

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn auth success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_auth_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnAuthSuccess**](ReportingMailAuthenticationSummaryReceivedConnAuthSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get**
> ReportingMailAuthenticationSummaryReceivedConnCertFail esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn cert fail

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn cert fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnCertFail**](ReportingMailAuthenticationSummaryReceivedConnCertFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get**
> ReportingMailAuthenticationSummaryReceivedConnCertSuccess esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn cert success

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn cert success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_cert_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnCertSuccess**](ReportingMailAuthenticationSummaryReceivedConnCertSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get**
> ReportingMailAuthenticationSummaryReceivedConnNoauth esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn noauth

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn noauth
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_noauth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnNoauth**](ReportingMailAuthenticationSummaryReceivedConnNoauth.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get**
> ReportingMailAuthenticationSummaryReceivedConnTotal esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received conn total

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received conn total
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_conn_total_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedConnTotal**](ReportingMailAuthenticationSummaryReceivedConnTotal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_noauth_get**
> ReportingMailAuthenticationSummaryReceivedNoauth esa_api_v20_reporting_mail_authentication_summary_received_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received noauth

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received noauth
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_noauth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedNoauth**](ReportingMailAuthenticationSummaryReceivedNoauth.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_summary_received_total_get**
> ReportingMailAuthenticationSummaryReceivedTotal esa_api_v20_reporting_mail_authentication_summary_received_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication summary received total

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
api_instance = swagger_client.MailAuthenticationSummaryApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication summary received total
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_summary_received_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationSummaryApi->esa_api_v20_reporting_mail_authentication_summary_received_total_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationSummaryReceivedTotal**](ReportingMailAuthenticationSummaryReceivedTotal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


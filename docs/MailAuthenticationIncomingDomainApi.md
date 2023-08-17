# swagger_client.MailAuthenticationIncomingDomainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/auth_disallow | mail authentication incoming domain auth disallow
[**esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/auth_fail | mail authentication incoming domain auth fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/auth_success | mail authentication incoming domain auth success
[**esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/cert_fail | mail authentication incoming domain cert fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/cert_fallback_fail | mail authentication incoming domain cert fallback fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/cert_fallback_success | mail authentication incoming domain cert fallback success
[**esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/cert_success | mail authentication incoming domain cert success
[**esa_api_v20_reporting_mail_authentication_incoming_domain_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain | mail authentication incoming domain noauth
[**esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/noauth | mail authentication incoming domain noauth
[**esa_api_v20_reporting_mail_authentication_incoming_domain_total_get**](MailAuthenticationIncomingDomainApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_total_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain/total | mail authentication incoming domain total

# **esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get**
> ReportingMailAuthenticationIncomingDomainAuthDisallow esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain auth disallow

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain auth disallow
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_auth_disallow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainAuthDisallow**](ReportingMailAuthenticationIncomingDomainAuthDisallow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get**
> ReportingMailAuthenticationIncomingDomainAuthFail esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain auth fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain auth fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_auth_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainAuthFail**](ReportingMailAuthenticationIncomingDomainAuthFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get**
> ReportingMailAuthenticationIncomingDomainAuthSuccess esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain auth success

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain auth success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_auth_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainAuthSuccess**](ReportingMailAuthenticationIncomingDomainAuthSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get**
> ReportingMailAuthenticationIncomingDomainCertFail esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain cert fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain cert fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainCertFail**](ReportingMailAuthenticationIncomingDomainCertFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get**
> ReportingMailAuthenticationIncomingDomainCertFallbackFail esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain cert fallback fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain cert fallback fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainCertFallbackFail**](ReportingMailAuthenticationIncomingDomainCertFallbackFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get**
> ReportingMailAuthenticationIncomingDomainCertFallbackSuccess esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain cert fallback success

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain cert fallback success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_cert_fallback_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainCertFallbackSuccess**](ReportingMailAuthenticationIncomingDomainCertFallbackSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get**
> ReportingMailAuthenticationIncomingDomainCertSuccess esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain cert success

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain cert success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_cert_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainCertSuccess**](ReportingMailAuthenticationIncomingDomainCertSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_get**
> ReportingMailAuthenticationIncomingDomainNoauth esa_api_v20_reporting_mail_authentication_incoming_domain_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain noauth

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain noauth
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainNoauth**](ReportingMailAuthenticationIncomingDomainNoauth.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get**
> ReportingMailAuthenticationIncomingDomainNoauth esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain noauth

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain noauth
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_noauth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainNoauth**](ReportingMailAuthenticationIncomingDomainNoauth.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_total_get**
> ReportingMailAuthenticationIncomingDomainTotal esa_api_v20_reporting_mail_authentication_incoming_domain_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain total

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
api_instance = swagger_client.MailAuthenticationIncomingDomainApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain total
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_total_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainApi->esa_api_v20_reporting_mail_authentication_incoming_domain_total_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainTotal**](ReportingMailAuthenticationIncomingDomainTotal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


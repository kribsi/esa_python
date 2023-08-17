# swagger_client.MailAuthenticationIncomingDomainIpApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip | mail authentication incoming domain ip last auth fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_auth_disallow | mail authentication incoming domain ip last auth disallow
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_auth_fail | mail authentication incoming domain ip last auth fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_auth_success | mail authentication incoming domain ip last auth success
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_cert_fail | mail authentication incoming domain ip last cert fail
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_cert_fallback | mail authentication incoming domain ip last cert fallback
[**esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get**](MailAuthenticationIncomingDomainIpApi.md#esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get) | **GET** /esa/api/v2.0/reporting/mail_authentication_incoming_domain_ip/last_cert_success | mail authentication incoming domain ip last cert success

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get**
> ReportingMailAuthenticationIncomingDomainIpLastAuthFail esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last auth fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last auth fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastAuthFail**](ReportingMailAuthenticationIncomingDomainIpLastAuthFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get**
> ReportingMailAuthenticationIncomingDomainIpLastAuthDisallow esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last auth disallow

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last auth disallow
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_disallow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastAuthDisallow**](ReportingMailAuthenticationIncomingDomainIpLastAuthDisallow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get**
> ReportingMailAuthenticationIncomingDomainIpLastAuthFail esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last auth fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last auth fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastAuthFail**](ReportingMailAuthenticationIncomingDomainIpLastAuthFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get**
> ReportingMailAuthenticationIncomingDomainIpLastAuthSuccess esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last auth success

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last auth success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_auth_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastAuthSuccess**](ReportingMailAuthenticationIncomingDomainIpLastAuthSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get**
> ReportingMailAuthenticationIncomingDomainIpLastCertFail esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last cert fail

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last cert fail
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastCertFail**](ReportingMailAuthenticationIncomingDomainIpLastCertFail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get**
> ReportingMailAuthenticationIncomingDomainIpLastCertFallback esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last cert fallback

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last cert fallback
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_fallback_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastCertFallback**](ReportingMailAuthenticationIncomingDomainIpLastCertFallback.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get**
> ReportingMailAuthenticationIncomingDomainIpLastCertSuccess esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail authentication incoming domain ip last cert success

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
api_instance = swagger_client.MailAuthenticationIncomingDomainIpApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail authentication incoming domain ip last cert success
    api_response = api_instance.esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailAuthenticationIncomingDomainIpApi->esa_api_v20_reporting_mail_authentication_incoming_domain_ip_last_cert_success_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailAuthenticationIncomingDomainIpLastCertSuccess**](ReportingMailAuthenticationIncomingDomainIpLastCertSuccess.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


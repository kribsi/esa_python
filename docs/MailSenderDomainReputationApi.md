# swagger_client.MailSenderDomainReputationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_domain_reputation_awful_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_awful_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/awful | mail sender domain reputation awful
[**esa_api_v20_reporting_mail_sender_domain_reputation_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation | mail sender domain reputation unscannable
[**esa_api_v20_reporting_mail_sender_domain_reputation_good_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_good_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/good | mail sender domain reputation good
[**esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/neutral | mail sender domain reputation neutral
[**esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/not_scanned | mail sender domain reputation not scanned
[**esa_api_v20_reporting_mail_sender_domain_reputation_poor_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_poor_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/poor | mail sender domain reputation poor
[**esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/tainted | mail sender domain reputation tainted
[**esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/unknown | mail sender domain reputation unknown
[**esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/unscannable | mail sender domain reputation unscannable
[**esa_api_v20_reporting_mail_sender_domain_reputation_weak_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_reputation_weak_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_reputation/weak | mail sender domain reputation weak
[**esa_api_v20_reporting_mail_sender_domain_threat_levels_get**](MailSenderDomainReputationApi.md#esa_api_v20_reporting_mail_sender_domain_threat_levels_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_threat_levels | mail sender domain reputation threat

# **esa_api_v20_reporting_mail_sender_domain_reputation_awful_get**
> ReportingMailSenderDomainReputationAwful esa_api_v20_reporting_mail_sender_domain_reputation_awful_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation awful

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation awful
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_awful_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_awful_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationAwful**](ReportingMailSenderDomainReputationAwful.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_get**
> ReportingMailSenderDomainReputationUnscannable esa_api_v20_reporting_mail_sender_domain_reputation_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation unscannable

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationUnscannable**](ReportingMailSenderDomainReputationUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_good_get**
> ReportingMailSenderDomainReputationGood esa_api_v20_reporting_mail_sender_domain_reputation_good_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation good

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation good
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_good_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_good_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationGood**](ReportingMailSenderDomainReputationGood.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get**
> ReportingMailSenderDomainReputationNeutral esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation neutral

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation neutral
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_neutral_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationNeutral**](ReportingMailSenderDomainReputationNeutral.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get**
> ReportingMailSenderDomainReputationNotScanned esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation not scanned

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation not scanned
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_not_scanned_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationNotScanned**](ReportingMailSenderDomainReputationNotScanned.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_poor_get**
> ReportingMailSenderDomainReputationPoor esa_api_v20_reporting_mail_sender_domain_reputation_poor_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation poor

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation poor
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_poor_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_poor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationPoor**](ReportingMailSenderDomainReputationPoor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get**
> ReportingMailSenderDomainReputationTainted esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation tainted

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation tainted
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_tainted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationTainted**](ReportingMailSenderDomainReputationTainted.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get**
> ReportingMailSenderDomainReputationUnknown esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation unknown

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation unknown
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_unknown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationUnknown**](ReportingMailSenderDomainReputationUnknown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get**
> ReportingMailSenderDomainReputationUnscannable esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation unscannable

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation unscannable
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_unscannable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationUnscannable**](ReportingMailSenderDomainReputationUnscannable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_reputation_weak_get**
> ReportingMailSenderDomainReputationWeak esa_api_v20_reporting_mail_sender_domain_reputation_weak_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain reputation weak

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain reputation weak
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_reputation_weak_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_reputation_weak_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainReputationWeak**](ReportingMailSenderDomainReputationWeak.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_threat_levels_get**
> ReportingMailSenderDomainThreatLevels esa_api_v20_reporting_mail_sender_domain_threat_levels_get(start_date=start_date, end_date=end_date, device_type=device_type, limit=limit, offset=offset, order_by=order_by, order_dir=order_dir)

mail sender domain reputation threat

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
api_instance = swagger_client.MailSenderDomainReputationApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str | The start date must be in ISO8601 format. (optional)
end_date = 'end_date_example' # str | The end date must be in ISO8601 format. (optional)
device_type = 'esa' # str |  (optional) (default to esa)
limit = '25' # str |  (optional) (default to 25)
offset = '0' # str |  (optional) (default to 0)
order_by = 'total_threats' # str |  (optional) (default to total_threats)
order_dir = 'desc' # str |  (optional) (default to desc)

try:
    # mail sender domain reputation threat
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_threat_levels_get(start_date=start_date, end_date=end_date, device_type=device_type, limit=limit, offset=offset, order_by=order_by, order_dir=order_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainReputationApi->esa_api_v20_reporting_mail_sender_domain_threat_levels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| The start date must be in ISO8601 format. | [optional] 
 **end_date** | **str**| The end date must be in ISO8601 format. | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **limit** | **str**|  | [optional] [default to 25]
 **offset** | **str**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to total_threats]
 **order_dir** | **str**|  | [optional] [default to desc]

### Return type

[**ReportingMailSenderDomainThreatLevels**](ReportingMailSenderDomainThreatLevels.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


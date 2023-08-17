# swagger_client.MailSenderDomainThreatCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_reporting_mail_sender_domain_threat_categories_get**](MailSenderDomainThreatCategoriesApi.md#esa_api_v20_reporting_mail_sender_domain_threat_categories_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_threat_categories | mail sender domain threat categories total threat messages
[**esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get**](MailSenderDomainThreatCategoriesApi.md#esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get) | **GET** /esa/api/v2.0/reporting/mail_sender_domain_threat_categories/total_threat_messages | mail sender domain threat categories total threat messages

# **esa_api_v20_reporting_mail_sender_domain_threat_categories_get**
> ReportingMailSenderDomainThreatCategoriesTotalThreatMessages esa_api_v20_reporting_mail_sender_domain_threat_categories_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top, limit=limit, offset=offset, order_by=order_by, order_dir=order_dir)

mail sender domain threat categories total threat messages

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
api_instance = swagger_client.MailSenderDomainThreatCategoriesApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str | The start date must be in ISO8601 format. (optional)
end_date = 'end_date_example' # str | The end date must be in ISO8601 format. (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)
limit = '25' # str |  (optional) (default to 25)
offset = '0' # str |  (optional) (default to 0)
order_by = 'total_threat_messages' # str |  (optional) (default to total_threat_messages)
order_dir = 'desc' # str |  (optional) (default to desc)

try:
    # mail sender domain threat categories total threat messages
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_threat_categories_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top, limit=limit, offset=offset, order_by=order_by, order_dir=order_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainThreatCategoriesApi->esa_api_v20_reporting_mail_sender_domain_threat_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| The start date must be in ISO8601 format. | [optional] 
 **end_date** | **str**| The end date must be in ISO8601 format. | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] [default to 25]
 **offset** | **str**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to total_threat_messages]
 **order_dir** | **str**|  | [optional] [default to desc]

### Return type

[**ReportingMailSenderDomainThreatCategoriesTotalThreatMessages**](ReportingMailSenderDomainThreatCategoriesTotalThreatMessages.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get**
> ReportingMailSenderDomainThreatCategoriesTotalThreatMessages esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)

mail sender domain threat categories total threat messages

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
api_instance = swagger_client.MailSenderDomainThreatCategoriesApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
device_type = 'esa' # str |  (optional) (default to esa)
top = 'top_example' # str |  (optional)

try:
    # mail sender domain threat categories total threat messages
    api_response = api_instance.esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get(start_date=start_date, end_date=end_date, device_type=device_type, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailSenderDomainThreatCategoriesApi->esa_api_v20_reporting_mail_sender_domain_threat_categories_total_threat_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **device_type** | **str**|  | [optional] [default to esa]
 **top** | **str**|  | [optional] 

### Return type

[**ReportingMailSenderDomainThreatCategoriesTotalThreatMessages**](ReportingMailSenderDomainThreatCategoriesTotalThreatMessages.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


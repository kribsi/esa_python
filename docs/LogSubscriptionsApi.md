# swagger_client.LogSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_config_logs_subscriptions_get**](LogSubscriptionsApi.md#esa_api_v20_config_logs_subscriptions_get) | **GET** /esa/api/v2.0/config/logs/subscriptions | Retrieve the details of all log subscriptions configured in your appliance
[**esa_api_v20_logs_subscription_name_get**](LogSubscriptionsApi.md#esa_api_v20_logs_subscription_name_get) | **GET** /esa/api/v2.0/logs/{subscription_name} | Retrieve the details of all log files for a specific log subscription
[**esa_api_v20_logs_subscription_name_log_file_name_get**](LogSubscriptionsApi.md#esa_api_v20_logs_subscription_name_log_file_name_get) | **GET** /esa/api/v2.0/logs/{subscription_name}/{log_file_name} | Retrieve the actual log file using the downloadUrl attribute of the response obtained from the API signature of the previous API

# **esa_api_v20_config_logs_subscriptions_get**
> ConfigLogSubscriptionsGet esa_api_v20_config_logs_subscriptions_get(retrieval_method=retrieval_method)

Retrieve the details of all log subscriptions configured in your appliance

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
api_instance = swagger_client.LogSubscriptionsApi(swagger_client.ApiClient(configuration))
retrieval_method = 'retrieval_method_example' # str |  (optional)

try:
    # Retrieve the details of all log subscriptions configured in your appliance
    api_response = api_instance.esa_api_v20_config_logs_subscriptions_get(retrieval_method=retrieval_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogSubscriptionsApi->esa_api_v20_config_logs_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieval_method** | **str**|  | [optional] 

### Return type

[**ConfigLogSubscriptionsGet**](ConfigLogSubscriptionsGet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_logs_subscription_name_get**
> ConfigLogSubscriptionDetailGet esa_api_v20_logs_subscription_name_get(subscription_name, start_date=start_date, end_date=end_date, compute_hash=compute_hash)

Retrieve the details of all log files for a specific log subscription

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
api_instance = swagger_client.LogSubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_name = 'subscription_name_example' # str | The name of the log subscription.
start_date = 'start_date_example' # str | The start date must be in ISO8601 format. (optional)
end_date = 'end_date_example' # str | The end date must be in ISO8601 format. (optional)
compute_hash = 'compute_hash_example' # str | To indicate whether to include the file SHA-256 value of the log file in the response. (optional)

try:
    # Retrieve the details of all log files for a specific log subscription
    api_response = api_instance.esa_api_v20_logs_subscription_name_get(subscription_name, start_date=start_date, end_date=end_date, compute_hash=compute_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogSubscriptionsApi->esa_api_v20_logs_subscription_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_name** | **str**| The name of the log subscription. | 
 **start_date** | **str**| The start date must be in ISO8601 format. | [optional] 
 **end_date** | **str**| The end date must be in ISO8601 format. | [optional] 
 **compute_hash** | **str**| To indicate whether to include the file SHA-256 value of the log file in the response. | [optional] 

### Return type

[**ConfigLogSubscriptionDetailGet**](ConfigLogSubscriptionDetailGet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_logs_subscription_name_log_file_name_get**
> str esa_api_v20_logs_subscription_name_log_file_name_get(subscription_name, log_file_name)

Retrieve the actual log file using the downloadUrl attribute of the response obtained from the API signature of the previous API

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
api_instance = swagger_client.LogSubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_name = 'subscription_name_example' # str | The name of the log subscription
log_file_name = 'log_file_name_example' # str | The name of the log file to be downloaded.

try:
    # Retrieve the actual log file using the downloadUrl attribute of the response obtained from the API signature of the previous API
    api_response = api_instance.esa_api_v20_logs_subscription_name_log_file_name_get(subscription_name, log_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogSubscriptionsApi->esa_api_v20_logs_subscription_name_log_file_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_name** | **str**| The name of the log subscription | 
 **log_file_name** | **str**| The name of the log file to be downloaded. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.DownloadApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_logs_subscription_name_log_file_name_get**](DownloadApi.md#esa_api_v20_logs_subscription_name_log_file_name_get) | **GET** /esa/api/v2.0/logs/{subscription_name}/{log_file_name} | Retrieve the actual log file using the downloadUrl attribute of the response obtained from the API signature of the previous API

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
api_instance = swagger_client.DownloadApi(swagger_client.ApiClient(configuration))
subscription_name = 'subscription_name_example' # str | The name of the log subscription
log_file_name = 'log_file_name_example' # str | The name of the log file to be downloaded.

try:
    # Retrieve the actual log file using the downloadUrl attribute of the response obtained from the API signature of the previous API
    api_response = api_instance.esa_api_v20_logs_subscription_name_log_file_name_get(subscription_name, log_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->esa_api_v20_logs_subscription_name_log_file_name_get: %s\n" % e)
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


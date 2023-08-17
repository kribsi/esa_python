# swagger_client.MessageTrackingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esa_api_v20_message_tracking_amp_details_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_amp_details_get) | **GET** /esa/api/v2.0/message-tracking/amp-details | Retrieve details of AMP action details of messages with different attributes
[**esa_api_v20_message_tracking_connection_details_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_connection_details_get) | **GET** /esa/api/v2.0/message-tracking/connection-details | Retrieve connection details of messages with different attributes
[**esa_api_v20_message_tracking_details_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_details_get) | **GET** /esa/api/v2.0/message-tracking/details | Retrieve details of messages with different attributes
[**esa_api_v20_message_tracking_dlp_details_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_dlp_details_get) | **GET** /esa/api/v2.0/message-tracking/dlp-details | Retrieve details of DLP of messages with different attributes
[**esa_api_v20_message_tracking_messages_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_messages_get) | **GET** /esa/api/v2.0/message-tracking/messages | Message-tracking messages
[**esa_api_v20_message_tracking_url_details_get**](MessageTrackingApi.md#esa_api_v20_message_tracking_url_details_get) | **GET** /esa/api/v2.0/message-tracking/url-details | Retrieve details of URL details of messages with different attributes

# **esa_api_v20_message_tracking_amp_details_get**
> MessageTrackingAmpDetails esa_api_v20_message_tracking_amp_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)

Retrieve details of AMP action details of messages with different attributes

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
icid = 'icid_example' # str |  (optional)
mid = 'mid_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # Retrieve details of AMP action details of messages with different attributes
    api_response = api_instance.esa_api_v20_message_tracking_amp_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_amp_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **icid** | **str**|  | [optional] 
 **mid** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

[**MessageTrackingAmpDetails**](MessageTrackingAmpDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_message_tracking_connection_details_get**
> MessageTrackingConnectionDetails esa_api_v20_message_tracking_connection_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)

Retrieve connection details of messages with different attributes

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
icid = 'icid_example' # str |  (optional)
mid = 'mid_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # Retrieve connection details of messages with different attributes
    api_response = api_instance.esa_api_v20_message_tracking_connection_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_connection_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **icid** | **str**|  | [optional] 
 **mid** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

[**MessageTrackingConnectionDetails**](MessageTrackingConnectionDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_message_tracking_details_get**
> MessageTrackingDetails esa_api_v20_message_tracking_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)

Retrieve details of messages with different attributes

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
icid = 'icid_example' # str |  (optional)
mid = 'mid_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # Retrieve details of messages with different attributes
    api_response = api_instance.esa_api_v20_message_tracking_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **icid** | **str**|  | [optional] 
 **mid** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

[**MessageTrackingDetails**](MessageTrackingDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_message_tracking_dlp_details_get**
> MessageTrackingDlpDetails esa_api_v20_message_tracking_dlp_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)

Retrieve details of DLP of messages with different attributes

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
icid = 'icid_example' # str |  (optional)
mid = 'mid_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # Retrieve details of DLP of messages with different attributes
    api_response = api_instance.esa_api_v20_message_tracking_dlp_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_dlp_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **icid** | **str**|  | [optional] 
 **mid** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

[**MessageTrackingDlpDetails**](MessageTrackingDlpDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_message_tracking_messages_get**
> MessageTrackingMessages esa_api_v20_message_tracking_messages_get(start_date=start_date, end_date=end_date, cisco_host=cisco_host, search_option=search_option, offset=offset, limit=limit)

Message-tracking messages

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
cisco_host = 'cisco_host_example' # str |  (optional)
search_option = 'messages' # str |  (optional) (default to messages)
offset = 'offset_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)

try:
    # Message-tracking messages
    api_response = api_instance.esa_api_v20_message_tracking_messages_get(start_date=start_date, end_date=end_date, cisco_host=cisco_host, search_option=search_option, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **cisco_host** | **str**|  | [optional] 
 **search_option** | **str**|  | [optional] [default to messages]
 **offset** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 

### Return type

[**MessageTrackingMessages**](MessageTrackingMessages.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esa_api_v20_message_tracking_url_details_get**
> MessageTrackingUrlDetails esa_api_v20_message_tracking_url_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)

Retrieve details of URL details of messages with different attributes

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
api_instance = swagger_client.MessageTrackingApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
icid = 'icid_example' # str |  (optional)
mid = 'mid_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # Retrieve details of URL details of messages with different attributes
    api_response = api_instance.esa_api_v20_message_tracking_url_details_get(start_date=start_date, end_date=end_date, icid=icid, mid=mid, serial_number=serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTrackingApi->esa_api_v20_message_tracking_url_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **icid** | **str**|  | [optional] 
 **mid** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

[**MessageTrackingUrlDetails**](MessageTrackingUrlDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


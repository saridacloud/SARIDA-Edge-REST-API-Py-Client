# swagger_client.DeviceApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control_device_restart_post**](DeviceApi.md#control_device_restart_post) | **POST** /control/device/restart | 
[**control_device_shutdown_post**](DeviceApi.md#control_device_shutdown_post) | **POST** /control/device/shutdown | 
[**web_hook_delete**](DeviceApi.md#web_hook_delete) | **DELETE** /webHook | 
[**web_hook_detection_updates_post**](DeviceApi.md#web_hook_detection_updates_post) | **POST** /webHook/detectionUpdates | 
[**web_hook_get**](DeviceApi.md#web_hook_get) | **GET** /webHook | 

# **control_device_restart_post**
> control_device_restart_post()



Restart the edge device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()

try:
    api_instance.control_device_restart_post()
except ApiException as e:
    print("Exception when calling DeviceApi->control_device_restart_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_device_shutdown_post**
> control_device_shutdown_post()



Shut down the edge device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()

try:
    api_instance.control_device_shutdown_post()
except ApiException as e:
    print("Exception when calling DeviceApi->control_device_shutdown_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_delete**
> web_hook_delete(webhook_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
webhook_id = 'webhook_id_example' # str | 'Web hook name created by requester (ID), to identify ' 'the registered web hook for later calls.' 

try:
    api_instance.web_hook_delete(webhook_id)
except ApiException as e:
    print("Exception when calling DeviceApi->web_hook_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| &#x27;Web hook name created by requester (ID), to identify &#x27; &#x27;the registered web hook for later calls.&#x27;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_detection_updates_post**
> web_hook_detection_updates_post(body, webhook_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
body = swagger_client.WebHookProperties() # WebHookProperties | 
webhook_id = 'webhook_id_example' # str | 'Web hook name created by requester (ID), to identify ' 'the registered web hook for later calls.' '(e.g.: Generate a new GUID and use it as web hook name)' 

try:
    api_instance.web_hook_detection_updates_post(body, webhook_id)
except ApiException as e:
    print("Exception when calling DeviceApi->web_hook_detection_updates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHookProperties**](WebHookProperties.md)|  | 
 **webhook_id** | **str**| &#x27;Web hook name created by requester (ID), to identify &#x27; &#x27;the registered web hook for later calls.&#x27; &#x27;(e.g.: Generate a new GUID and use it as web hook name)&#x27;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_get**
> WebHookProperties web_hook_get(webhook_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
webhook_id = 'webhook_id_example' # str | 'Web hook name created by requester (ID), to identify ' 'the registered web hook for later calls.' 

try:
    api_response = api_instance.web_hook_get(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->web_hook_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| &#x27;Web hook name created by requester (ID), to identify &#x27; &#x27;the registered web hook for later calls.&#x27;  | 

### Return type

[**WebHookProperties**](WebHookProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.CameraApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**camera_set_origin_orientation_put**](CameraApi.md#camera_set_origin_orientation_put) | **PUT** /camera/setOriginOrientation | 
[**camera_state_get**](CameraApi.md#camera_state_get) | **GET** /camera/state | 
[**camera_state_put**](CameraApi.md#camera_state_put) | **PUT** /camera/state | 

# **camera_set_origin_orientation_put**
> camera_set_origin_orientation_put(body)



Set given camera orientation as origin. (Physical camera orientation must be horizontal and straight)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CameraApi()
body = swagger_client.Orientation() # Orientation | 

try:
    api_instance.camera_set_origin_orientation_put(body)
except ApiException as e:
    print("Exception when calling CameraApi->camera_set_origin_orientation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Orientation**](Orientation.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **camera_state_get**
> CameraState camera_state_get()



Get last received camera state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CameraApi()

try:
    api_response = api_instance.camera_state_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CameraApi->camera_state_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CameraState**](CameraState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **camera_state_put**
> camera_state_put(body)



Update camera state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CameraApi()
body = swagger_client.CameraState() # CameraState | 

try:
    api_instance.camera_state_put(body)
except ApiException as e:
    print("Exception when calling CameraApi->camera_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CameraState**](CameraState.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


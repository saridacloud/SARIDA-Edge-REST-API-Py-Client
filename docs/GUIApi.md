# swagger_client.GUIApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control_gui_detection_area_visibility_get**](GUIApi.md#control_gui_detection_area_visibility_get) | **GET** /control/gui/detectionAreaVisibility | 
[**control_gui_detection_area_visibility_post**](GUIApi.md#control_gui_detection_area_visibility_post) | **POST** /control/gui/detectionAreaVisibility | 
[**control_gui_detection_bounding_box_visibility_get**](GUIApi.md#control_gui_detection_bounding_box_visibility_get) | **GET** /control/gui/detectionBoundingBoxVisibility | 
[**control_gui_detection_bounding_box_visibility_post**](GUIApi.md#control_gui_detection_bounding_box_visibility_post) | **POST** /control/gui/detectionBoundingBoxVisibility | 
[**control_gui_detection_color_get**](GUIApi.md#control_gui_detection_color_get) | **GET** /control/gui/detectionColor | 
[**control_gui_detection_color_post**](GUIApi.md#control_gui_detection_color_post) | **POST** /control/gui/detectionColor | 
[**control_gui_detection_polygon_visibility_get**](GUIApi.md#control_gui_detection_polygon_visibility_get) | **GET** /control/gui/detectionPolygonVisibility | 
[**control_gui_detection_polygon_visibility_post**](GUIApi.md#control_gui_detection_polygon_visibility_post) | **POST** /control/gui/detectionPolygonVisibility | 
[**control_gui_detection_text_visibility_get**](GUIApi.md#control_gui_detection_text_visibility_get) | **GET** /control/gui/detectionTextVisibility | 
[**control_gui_detection_text_visibility_post**](GUIApi.md#control_gui_detection_text_visibility_post) | **POST** /control/gui/detectionTextVisibility | 
[**control_gui_detections_visibility_get**](GUIApi.md#control_gui_detections_visibility_get) | **GET** /control/gui/detectionsVisibility | 
[**control_gui_detections_visibility_post**](GUIApi.md#control_gui_detections_visibility_post) | **POST** /control/gui/detectionsVisibility | 

# **control_gui_detection_area_visibility_get**
> bool control_gui_detection_area_visibility_get()



'Return if detection areas are currently visible in edge GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()

try:
    api_response = api_instance.control_gui_detection_area_visibility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_area_visibility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_area_visibility_post**
> control_gui_detection_area_visibility_post(set_visible)



Set visibility of detection areas in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
set_visible = true # bool | 

try:
    api_instance.control_gui_detection_area_visibility_post(set_visible)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_area_visibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_visible** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_bounding_box_visibility_get**
> bool control_gui_detection_bounding_box_visibility_get()



'Return if detection bounding boxes are currently visible in ' 'edge GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()

try:
    api_response = api_instance.control_gui_detection_bounding_box_visibility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_bounding_box_visibility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_bounding_box_visibility_post**
> control_gui_detection_bounding_box_visibility_post(set_visible)



'Set visibility of detection bounding boxes in edge GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
set_visible = true # bool | 

try:
    api_instance.control_gui_detection_bounding_box_visibility_post(set_visible)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_bounding_box_visibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_visible** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_color_get**
> Color control_gui_detection_color_get(detection_class)



Return color of detection class in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
detection_class = swagger_client.DetectionClasses() # DetectionClasses | 

try:
    api_response = api_instance.control_gui_detection_color_get(detection_class)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_color_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_class** | [**DetectionClasses**](.md)|  | 

### Return type

[**Color**](Color.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_color_post**
> control_gui_detection_color_post(body)



Set color of detection class in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
body = swagger_client.GuiDetectionColorBody() # GuiDetectionColorBody | 

try:
    api_instance.control_gui_detection_color_post(body)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_color_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GuiDetectionColorBody**](GuiDetectionColorBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_polygon_visibility_get**
> bool control_gui_detection_polygon_visibility_get()



'Return if detection polygons are currently visible in edge '  'GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()

try:
    api_response = api_instance.control_gui_detection_polygon_visibility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_polygon_visibility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_polygon_visibility_post**
> control_gui_detection_polygon_visibility_post(set_visible)



Set visibility of detection polygons in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
set_visible = true # bool | 

try:
    api_instance.control_gui_detection_polygon_visibility_post(set_visible)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_polygon_visibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_visible** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_text_visibility_get**
> bool control_gui_detection_text_visibility_get()



'Return if detection texts are currently visible in edge GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()

try:
    api_response = api_instance.control_gui_detection_text_visibility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_text_visibility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detection_text_visibility_post**
> control_gui_detection_text_visibility_post(set_visible)



Set visibility of detection texts in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
set_visible = true # bool | 

try:
    api_instance.control_gui_detection_text_visibility_post(set_visible)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detection_text_visibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_visible** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detections_visibility_get**
> bool control_gui_detections_visibility_get()



'Return if detections are currently visible in edge GUI' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()

try:
    api_response = api_instance.control_gui_detections_visibility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detections_visibility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_gui_detections_visibility_post**
> control_gui_detections_visibility_post(set_visible)



Set detections visibility in edge GUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GUIApi()
set_visible = true # bool | 

try:
    api_instance.control_gui_detections_visibility_post(set_visible)
except ApiException as e:
    print("Exception when calling GUIApi->control_gui_detections_visibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_visible** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


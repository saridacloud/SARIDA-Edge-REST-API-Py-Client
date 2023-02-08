# swagger_client.InspectionApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspection_damage_added_post**](InspectionApi.md#inspection_damage_added_post) | **POST** /inspection/damageAdded | 
[**inspection_run_begin_pause_put**](InspectionApi.md#inspection_run_begin_pause_put) | **PUT** /inspection/run/beginPause | 
[**inspection_run_end_pause_put**](InspectionApi.md#inspection_run_end_pause_put) | **PUT** /inspection/run/endPause | 
[**inspection_run_get**](InspectionApi.md#inspection_run_get) | **GET** /inspection/run | 
[**inspection_run_start_put**](InspectionApi.md#inspection_run_start_put) | **PUT** /inspection/run/start | 
[**inspection_run_stop_put**](InspectionApi.md#inspection_run_stop_put) | **PUT** /inspection/run/stop | 
[**inspection_section_data_get**](InspectionApi.md#inspection_section_data_get) | **GET** /inspection/sectionData | 
[**inspection_section_data_put**](InspectionApi.md#inspection_section_data_put) | **PUT** /inspection/sectionData | 

# **inspection_damage_added_post**
> inspection_damage_added_post(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()
body = swagger_client.DamageData() # DamageData | 

try:
    api_instance.inspection_damage_added_post(body)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_damage_added_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamageData**](DamageData.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_run_begin_pause_put**
> inspection_run_begin_pause_put(body)



Pause inspection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()
body = swagger_client.FrameTime() # FrameTime | 

try:
    api_instance.inspection_run_begin_pause_put(body)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_run_begin_pause_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FrameTime**](FrameTime.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_run_end_pause_put**
> inspection_run_end_pause_put(body)



Resume inspection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()
body = swagger_client.FrameTime() # FrameTime | 

try:
    api_instance.inspection_run_end_pause_put(body)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_run_end_pause_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FrameTime**](FrameTime.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_run_get**
> InspectionRunStatus inspection_run_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()

try:
    api_response = api_instance.inspection_run_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_run_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InspectionRunStatus**](InspectionRunStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_run_start_put**
> inspection_run_start_put(body)



Start inspection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()
body = swagger_client.FrameTime() # FrameTime | 

try:
    api_instance.inspection_run_start_put(body)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_run_start_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FrameTime**](FrameTime.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_run_stop_put**
> inspection_run_stop_put()



Stop inspection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()

try:
    api_instance.inspection_run_stop_put()
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_run_stop_put: %s\n" % e)
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

# **inspection_section_data_get**
> SectionBaseData inspection_section_data_get()



Get last received section data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()

try:
    api_response = api_instance.inspection_section_data_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_section_data_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectionBaseData**](SectionBaseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_section_data_put**
> inspection_section_data_put(body)



Update section data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InspectionApi()
body = swagger_client.SectionBaseData() # SectionBaseData | 

try:
    api_instance.inspection_section_data_put(body)
except ApiException as e:
    print("Exception when calling InspectionApi->inspection_section_data_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SectionBaseData**](SectionBaseData.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


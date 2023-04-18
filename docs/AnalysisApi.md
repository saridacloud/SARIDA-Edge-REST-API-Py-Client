# swagger_client.AnalysisApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysis_results_current_get**](AnalysisApi.md#analysis_results_current_get) | **GET** /analysis/results/current | 
[**analysis_results_details_current_get**](AnalysisApi.md#analysis_results_details_current_get) | **GET** /analysis/results/details/current | 
[**analysis_results_details_mask_get**](AnalysisApi.md#analysis_results_details_mask_get) | **GET** /analysis/results/details/mask | 
[**analysis_results_inspection_log_get**](AnalysisApi.md#analysis_results_inspection_log_get) | **GET** /analysis/results/inspectionLog | 
[**analysis_video_resolution_get**](AnalysisApi.md#analysis_video_resolution_get) | **GET** /analysis/video/resolution | 

# **analysis_results_current_get**
> AnalysisResult analysis_results_current_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    api_response = api_instance.analysis_results_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResult**](AnalysisResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_results_details_current_get**
> FrameAnalysisDetails analysis_results_details_current_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    api_response = api_instance.analysis_results_details_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_details_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FrameAnalysisDetails**](FrameAnalysisDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_results_details_mask_get**
> str analysis_results_details_mask_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    api_response = api_instance.analysis_results_details_mask_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_details_mask_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_results_inspection_log_get**
> AnalysisResults analysis_results_inspection_log_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    api_response = api_instance.analysis_results_inspection_log_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_inspection_log_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResults**](AnalysisResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_video_resolution_get**
> Size analysis_video_resolution_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi()

try:
    api_response = api_instance.analysis_video_resolution_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_video_resolution_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Size**](Size.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


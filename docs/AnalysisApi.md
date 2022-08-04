# swagger_client.AnalysisApi

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysis_results_current_get**](AnalysisApi.md#analysis_results_current_get) | **GET** /analysis/results/current | 
[**analysis_results_inspection_log_get**](AnalysisApi.md#analysis_results_inspection_log_get) | **GET** /analysis/results/inspectionLog | 

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


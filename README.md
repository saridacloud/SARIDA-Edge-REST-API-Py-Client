# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.4
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalysisApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.analysis_results_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_current_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AnalysisApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.analysis_results_details_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_details_current_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AnalysisApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.analysis_results_inspection_log_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->analysis_results_inspection_log_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/esicteam/SaridaEdgeAPI/1.4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalysisApi* | [**analysis_results_current_get**](docs/AnalysisApi.md#analysis_results_current_get) | **GET** /analysis/results/current | 
*AnalysisApi* | [**analysis_results_details_current_get**](docs/AnalysisApi.md#analysis_results_details_current_get) | **GET** /analysis/results/details/current | 
*AnalysisApi* | [**analysis_results_inspection_log_get**](docs/AnalysisApi.md#analysis_results_inspection_log_get) | **GET** /analysis/results/inspectionLog | 
*CameraApi* | [**camera_set_origin_orientation_put**](docs/CameraApi.md#camera_set_origin_orientation_put) | **PUT** /camera/setOriginOrientation | 
*CameraApi* | [**camera_state_get**](docs/CameraApi.md#camera_state_get) | **GET** /camera/state | 
*CameraApi* | [**camera_state_put**](docs/CameraApi.md#camera_state_put) | **PUT** /camera/state | 
*DeviceApi* | [**control_device_restart_post**](docs/DeviceApi.md#control_device_restart_post) | **POST** /control/device/restart | 
*DeviceApi* | [**control_device_shutdown_post**](docs/DeviceApi.md#control_device_shutdown_post) | **POST** /control/device/shutdown | 
*DeviceApi* | [**control_video_player_start_post**](docs/DeviceApi.md#control_video_player_start_post) | **POST** /control/videoPlayer/start | 
*DeviceApi* | [**control_video_player_stop_post**](docs/DeviceApi.md#control_video_player_stop_post) | **POST** /control/videoPlayer/stop | 
*DeviceApi* | [**web_hook_delete**](docs/DeviceApi.md#web_hook_delete) | **DELETE** /webHook | 
*DeviceApi* | [**web_hook_detection_updates_post**](docs/DeviceApi.md#web_hook_detection_updates_post) | **POST** /webHook/detectionUpdates | 
*DeviceApi* | [**web_hook_get**](docs/DeviceApi.md#web_hook_get) | **GET** /webHook | 
*GUIApi* | [**control_gui_detection_area_visibility_get**](docs/GUIApi.md#control_gui_detection_area_visibility_get) | **GET** /control/gui/detectionAreaVisibility | 
*GUIApi* | [**control_gui_detection_area_visibility_post**](docs/GUIApi.md#control_gui_detection_area_visibility_post) | **POST** /control/gui/detectionAreaVisibility | 
*GUIApi* | [**control_gui_detection_bounding_box_visibility_get**](docs/GUIApi.md#control_gui_detection_bounding_box_visibility_get) | **GET** /control/gui/detectionBoundingBoxVisibility | 
*GUIApi* | [**control_gui_detection_bounding_box_visibility_post**](docs/GUIApi.md#control_gui_detection_bounding_box_visibility_post) | **POST** /control/gui/detectionBoundingBoxVisibility | 
*GUIApi* | [**control_gui_detection_color_get**](docs/GUIApi.md#control_gui_detection_color_get) | **GET** /control/gui/detectionColor | 
*GUIApi* | [**control_gui_detection_color_post**](docs/GUIApi.md#control_gui_detection_color_post) | **POST** /control/gui/detectionColor | 
*GUIApi* | [**control_gui_detection_polygon_visibility_get**](docs/GUIApi.md#control_gui_detection_polygon_visibility_get) | **GET** /control/gui/detectionPolygonVisibility | 
*GUIApi* | [**control_gui_detection_polygon_visibility_post**](docs/GUIApi.md#control_gui_detection_polygon_visibility_post) | **POST** /control/gui/detectionPolygonVisibility | 
*GUIApi* | [**control_gui_detection_text_visibility_get**](docs/GUIApi.md#control_gui_detection_text_visibility_get) | **GET** /control/gui/detectionTextVisibility | 
*GUIApi* | [**control_gui_detection_text_visibility_post**](docs/GUIApi.md#control_gui_detection_text_visibility_post) | **POST** /control/gui/detectionTextVisibility | 
*GUIApi* | [**control_gui_detections_visibility_get**](docs/GUIApi.md#control_gui_detections_visibility_get) | **GET** /control/gui/detectionsVisibility | 
*GUIApi* | [**control_gui_detections_visibility_post**](docs/GUIApi.md#control_gui_detections_visibility_post) | **POST** /control/gui/detectionsVisibility | 
*InspectionApi* | [**inspection_damage_added_post**](docs/InspectionApi.md#inspection_damage_added_post) | **POST** /inspection/damageAdded | 
*InspectionApi* | [**inspection_run_begin_pause_put**](docs/InspectionApi.md#inspection_run_begin_pause_put) | **PUT** /inspection/run/beginPause | 
*InspectionApi* | [**inspection_run_end_pause_put**](docs/InspectionApi.md#inspection_run_end_pause_put) | **PUT** /inspection/run/endPause | 
*InspectionApi* | [**inspection_run_get**](docs/InspectionApi.md#inspection_run_get) | **GET** /inspection/run | 
*InspectionApi* | [**inspection_run_start_put**](docs/InspectionApi.md#inspection_run_start_put) | **PUT** /inspection/run/start | 
*InspectionApi* | [**inspection_run_stop_put**](docs/InspectionApi.md#inspection_run_stop_put) | **PUT** /inspection/run/stop | 
*InspectionApi* | [**inspection_section_data_get**](docs/InspectionApi.md#inspection_section_data_get) | **GET** /inspection/sectionData | 
*InspectionApi* | [**inspection_section_data_put**](docs/InspectionApi.md#inspection_section_data_put) | **PUT** /inspection/sectionData | 

## Documentation For Models

 - [AnalysisDetails](docs/AnalysisDetails.md)
 - [AnalysisResult](docs/AnalysisResult.md)
 - [AnalysisResults](docs/AnalysisResults.md)
 - [CameraState](docs/CameraState.md)
 - [Color](docs/Color.md)
 - [DamageData](docs/DamageData.md)
 - [DetectionClasses](docs/DetectionClasses.md)
 - [DetectionState](docs/DetectionState.md)
 - [FrameAnalysisDetails](docs/FrameAnalysisDetails.md)
 - [FrameTime](docs/FrameTime.md)
 - [GuiDetectionColorBody](docs/GuiDetectionColorBody.md)
 - [GuiDetectionColorBody1](docs/GuiDetectionColorBody1.md)
 - [InspectionNorm](docs/InspectionNorm.md)
 - [InspectionRunStatus](docs/InspectionRunStatus.md)
 - [Materials](docs/Materials.md)
 - [Orientation](docs/Orientation.md)
 - [PipeDiameter](docs/PipeDiameter.md)
 - [PipeProfiles](docs/PipeProfiles.md)
 - [Point](docs/Point.md)
 - [Polygon](docs/Polygon.md)
 - [RunningStates](docs/RunningStates.md)
 - [SectionBaseData](docs/SectionBaseData.md)
 - [WebHookProperties](docs/WebHookProperties.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author



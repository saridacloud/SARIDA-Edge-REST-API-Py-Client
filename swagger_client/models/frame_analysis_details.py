# coding: utf-8

"""
    SaridaEdgeAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FrameAnalysisDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'camera_state': 'CameraState',
        'analysis_details': 'list[AnalysisDetails]'
    }

    attribute_map = {
        'camera_state': 'cameraState',
        'analysis_details': 'analysisDetails'
    }

    def __init__(self, camera_state=None, analysis_details=None):  # noqa: E501
        """FrameAnalysisDetails - a model defined in Swagger"""  # noqa: E501
        self._camera_state = None
        self._analysis_details = None
        self.discriminator = None
        if camera_state is not None:
            self.camera_state = camera_state
        if analysis_details is not None:
            self.analysis_details = analysis_details

    @property
    def camera_state(self):
        """Gets the camera_state of this FrameAnalysisDetails.  # noqa: E501


        :return: The camera_state of this FrameAnalysisDetails.  # noqa: E501
        :rtype: CameraState
        """
        return self._camera_state

    @camera_state.setter
    def camera_state(self, camera_state):
        """Sets the camera_state of this FrameAnalysisDetails.


        :param camera_state: The camera_state of this FrameAnalysisDetails.  # noqa: E501
        :type: CameraState
        """

        self._camera_state = camera_state

    @property
    def analysis_details(self):
        """Gets the analysis_details of this FrameAnalysisDetails.  # noqa: E501


        :return: The analysis_details of this FrameAnalysisDetails.  # noqa: E501
        :rtype: list[AnalysisDetails]
        """
        return self._analysis_details

    @analysis_details.setter
    def analysis_details(self, analysis_details):
        """Sets the analysis_details of this FrameAnalysisDetails.


        :param analysis_details: The analysis_details of this FrameAnalysisDetails.  # noqa: E501
        :type: list[AnalysisDetails]
        """

        self._analysis_details = analysis_details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FrameAnalysisDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FrameAnalysisDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
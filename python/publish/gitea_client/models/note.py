# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.23.0+dev-531-g99d0510cb6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from publish.gitea_client.configuration import Configuration


class Note(object):
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
        'commit': 'Commit',
        'message': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'message': 'message'
    }

    def __init__(self, commit=None, message=None, _configuration=None):  # noqa: E501
        """Note - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._commit = None
        self._message = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if message is not None:
            self.message = message

    @property
    def commit(self):
        """Gets the commit of this Note.  # noqa: E501


        :return: The commit of this Note.  # noqa: E501
        :rtype: Commit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Note.


        :param commit: The commit of this Note.  # noqa: E501
        :type: Commit
        """

        self._commit = commit

    @property
    def message(self):
        """Gets the message of this Note.  # noqa: E501


        :return: The message of this Note.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Note.


        :param message: The message of this Note.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(Note, dict):
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
        if not isinstance(other, Note):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Note):
            return True

        return self.to_dict() != other.to_dict()

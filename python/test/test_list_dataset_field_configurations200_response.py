# coding: utf-8

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_dataset_field_configurations200_response import ListDatasetFieldConfigurations200Response

class TestListDatasetFieldConfigurations200Response(unittest.TestCase):
    """ListDatasetFieldConfigurations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatasetFieldConfigurations200Response:
        """Test ListDatasetFieldConfigurations200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatasetFieldConfigurations200Response`
        """
        model = ListDatasetFieldConfigurations200Response()
        if include_optional:
            return ListDatasetFieldConfigurations200Response(
                total_count = 56,
                next = '',
                previous = '',
                results = [
                    {"uid":"pr_qf2hyt","type":"annotate","label":"Making field_id as a facet","field":"field_id","annotation":"facet"}
                    ]
            )
        else:
            return ListDatasetFieldConfigurations200Response(
        )
        """

    def testListDatasetFieldConfigurations200Response(self):
        """Test ListDatasetFieldConfigurations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

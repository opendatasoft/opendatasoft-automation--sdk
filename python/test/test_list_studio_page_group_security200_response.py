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

from openapi_client.models.list_studio_page_group_security200_response import ListStudioPageGroupSecurity200Response

class TestListStudioPageGroupSecurity200Response(unittest.TestCase):
    """ListStudioPageGroupSecurity200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListStudioPageGroupSecurity200Response:
        """Test ListStudioPageGroupSecurity200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListStudioPageGroupSecurity200Response`
        """
        model = ListStudioPageGroupSecurity200Response()
        if include_optional:
            return ListStudioPageGroupSecurity200Response(
                total_count = 56,
                next = '',
                previous = '',
                results = [
                    openapi_client.models.group_ruleset.Group ruleset(
                        group = openapi_client.models.group_security_group.GroupSecurity_group(
                            uid = 'content_designers', ), 
                        permissions = [
                            'edit_page'
                            ], )
                    ]
            )
        else:
            return ListStudioPageGroupSecurity200Response(
        )
        """

    def testListStudioPageGroupSecurity200Response(self):
        """Test ListStudioPageGroupSecurity200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

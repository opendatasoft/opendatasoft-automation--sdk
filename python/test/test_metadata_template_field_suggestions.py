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

from openapi_client.models.metadata_template_field_suggestions import MetadataTemplateFieldSuggestions

class TestMetadataTemplateFieldSuggestions(unittest.TestCase):
    """MetadataTemplateFieldSuggestions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataTemplateFieldSuggestions:
        """Test MetadataTemplateFieldSuggestions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataTemplateFieldSuggestions`
        """
        model = MetadataTemplateFieldSuggestions()
        if include_optional:
            return MetadataTemplateFieldSuggestions(
                hits = [
                    ''
                    ],
                nb_hits = 1.337,
                page = 1.337,
                hits_per_page = 1.337,
                exhaustive_nb_hits = True,
                exhaustive_typo = True,
                exhaustive = openapi_client.models.metadata_template_field_suggestions_exhaustive.MetadataTemplateFieldSuggestions_exhaustive(
                    nb_hits = True, 
                    typo = True, ),
                query = '',
                params = '',
                processing_time_ms = 1.337
            )
        else:
            return MetadataTemplateFieldSuggestions(
        )
        """

    def testMetadataTemplateFieldSuggestions(self):
        """Test MetadataTemplateFieldSuggestions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

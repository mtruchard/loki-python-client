#
# Copyright (c) 2019 All Rights Reserved, SaplingData LLC, http://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

__author__ = "mtruchard"

import unittest
from loki import Loki

config_file = "~/loki-python-client/config.txt"


class TestList(unittest.TestCase):
    """ Unit tests to evaluate the behavior of loki.data(). """

    def test_list(self):
        print("=============== TEST LIST ===========================================================")
        loki = Loki(config_file)
        result = loki.data.list("urn:com:loki:core:model:types",None)
        print(result.get_response())
        self.assertEqual(result.is_success(), True)
        self.assertEqual(200, result.get_response().status_code)
        for r in result.to_array():
            print(r["urn"])
        
    def test_load_entity(self):
        print("=============== TEST LOAD ENTITY ===========================================================")
        loki = Loki(config_file)
        urn = "urn:com:loki:meta:model:types:error"
        view = "urn:com:loki:meta:model:types:entityView"
        result = loki.data.load_entity(urn, view, None)
        self.assertEqual(result.is_success(), True)
        self.assertEqual(200, result.get_response().status_code)
        print(result.get_data())

    def test_load_resource(self):
        print("=============== TEST LOAD RESOURCE ===========================================================")
        loki = Loki(config_file)
        urn = "urn:com:loki:core:model:api:list!listApi.html"
        result = loki.data.load_resource(urn, None)
        self.assertEqual(result.is_success(), True)
        self.assertEqual(200, result.get_response().status_code)
        print(result.get_data())

    def test_download_resource(self):
        print("=============== TEST DOWNLOAD RESOURCE ===========================================================")
        loki = Loki(config_file)
        urn = "urn:com:loki:core:model:api:list!listApi.html"
        result = loki.data.download_resource(urn,None, "~/listApi.html")
        self.assertEqual(result.is_success(), True)
        self.assertEqual(200, result.get_response().status_code)
        print(result.get_data())

    def test_query(self):
        print("=============== TEST QUERY ===========================================================")
        loki = Loki(config_file)
        query_urn = "urn:com:loki:examples:model:queries:listDocuments"
        result = loki.data.query(query_urn, None)
        print(result.get_response())
        self.assertEqual(result.is_success(), True)
        self.assertEqual(200, result.get_response().status_code)
        for r in result.to_array():
            for v in r:
                print(v)

    def test_query404(self):
        print("=============== TEST QUERY 404 ===========================================================")
        loki = Loki(config_file)
        result = loki.data.query("urn:com:loki:examples:model:queries:xxxlistDocumentsxx",None)
        self.assertEqual(result.is_success(), False)
        self.assertEqual(result.to_array(), [])
        print(result.get_error())

    def test_query403(self):
        print("=============== TEST QUERY 403 ===========================================================")
        loki = Loki(config_file)
        loki._password = "bogusxxxxx"
        result = loki.data.query("urn:com:loki:examples:model:queries:listDocuments",None)
        self.assertEqual(result.is_success(), False)
        self.assertEqual(result.to_array(), [])
        print(result.get_error())


if __name__ == "__main__":
    unittest.main()

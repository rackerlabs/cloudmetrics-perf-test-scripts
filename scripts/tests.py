
from __future__ import division

import sys
import time
import unittest
import random
import math

import ingest
import ingestenum
import query
import annotationsingest
import abstract_thread
import thread_manager as tm
from config import clean_configs

try:
    from com.xhaus.jyson import JysonCodec as json
except ImportError:
    import json
import pprint

pp = pprint.pprint
sleep_time = -1
get_url = None
post_url = None
post_payload = None


def mock_sleep(cls, x):
    global sleep_time
    sleep_time = x


class MockReq():
    def __init__(self):
        self.post_url = None
        self.post_payload = None
        self.get_url = None

    def POST(self, url, payload):
        global post_url, post_payload
        post_url = url
        post_payload = payload
        self.post_url = url
        self.post_payload = payload
        return url, payload

    def GET(self, url):
        global get_url
        get_url = url
        self.get_url = url
        return url

requests_by_type = {
    ingest.IngestThread:                        MockReq(),
    ingestenum.EnumIngestThread:                MockReq(),
    annotationsingest.AnnotationsIngestThread:  MockReq(),
    query.SinglePlotQuery:                      MockReq(),
    query.MultiPlotQuery:                       MockReq(),
    query.SearchQuery:                          MockReq(),
    query.EnumSearchQuery:                      MockReq(),
    query.EnumSinglePlotQuery:                  MockReq(),
    query.EnumMultiPlotQuery:                   MockReq(),
    query.AnnotationsQuery:                     MockReq(),
}


grinder_props = {
    'grinder.script': '../scripts/tests.py',
    'grinder.package_path': '/Library/Python/2.7/site-packages',
    'grinder.runs': '1',
    'grinder.threads': '45',
    'grinder.useConsole': 'false',
    'grinder.logDirectory': 'resources/logs',
    'grinder.bf.name_fmt': 'org.example.metric.%d',
    'grinder.bf.report_interval': '10000',
    'grinder.bf.annotations_num_tenants': '4',
    'grinder.bf.num_tenants': '4',
    'grinder.bf.enum_num_tenants': '4',
    'grinder.bf.metrics_per_tenant': '15',
    'grinder.bf.enum_metrics_per_tenant': '5',
    'grinder.bf.batch_size': '5',
    'grinder.bf.ingest_weight': '15',
    'grinder.bf.enum_ingest_weight': '15',
    'grinder.bf.annotations_per_tenant': '5',
    'grinder.bf.annotations_weight': '5',
    'grinder.bf.num_nodes': '1',
    'grinder.bf.url': 'http://metrics-ingest.example.org',
    'grinder.bf.query_url': 'http://metrics.example.org',
    'grinder.bf.query_concurrency': '10',
    'grinder.bf.max_multiplot_metrics': '10',
    'grinder.bf.search_query_weight': '2',
    'grinder.bf.enum_search_query_weight': '1',
    'grinder.bf.multiplot_query_weight': '2',
    'grinder.bf.singleplot_query_weight': '2',
    'grinder.bf.enum_single_plot_query_weight': '1',
    'grinder.bf.enum_multiplot_query_weight': '2',
    'grinder.bf.annotations_query_weight': '1',
}


class TestCaseBase(unittest.TestCase):
    def assertIs(self, expr1, expr2, msg=None):
        return self.assertTrue(expr1 is expr2, msg)

    def assertIsInstance(self, obj, cls, msg=None):
        return self.assertTrue(isinstance(obj, cls), msg)
    pass


class ThreadManagerTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        self.tm = tm.ThreadManager(grinder_props, requests_by_type)
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(clean_configs(grinder_props))

    def test_thread_type_assignment_0(self):
        th = self.tm.setup_thread(0, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_1(self):
        th = self.tm.setup_thread(1, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_2(self):
        th = self.tm.setup_thread(2, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_3(self):
        th = self.tm.setup_thread(3, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_4(self):
        th = self.tm.setup_thread(4, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_5(self):
        th = self.tm.setup_thread(5, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_6(self):
        th = self.tm.setup_thread(6, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_7(self):
        th = self.tm.setup_thread(7, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_8(self):
        th = self.tm.setup_thread(8, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_9(self):
        th = self.tm.setup_thread(9, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_10(self):
        th = self.tm.setup_thread(10, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_11(self):
        th = self.tm.setup_thread(11, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_12(self):
        th = self.tm.setup_thread(12, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_13(self):
        th = self.tm.setup_thread(13, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_14(self):
        th = self.tm.setup_thread(14, 0)
        self.assertEqual(type(th), ingest.IngestThread)

    def test_thread_type_assignment_15(self):
        th = self.tm.setup_thread(15, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_16(self):
        th = self.tm.setup_thread(16, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_17(self):
        th = self.tm.setup_thread(17, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_18(self):
        th = self.tm.setup_thread(18, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_19(self):
        th = self.tm.setup_thread(19, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_20(self):
        th = self.tm.setup_thread(20, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_21(self):
        th = self.tm.setup_thread(21, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_22(self):
        th = self.tm.setup_thread(22, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_23(self):
        th = self.tm.setup_thread(23, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_24(self):
        th = self.tm.setup_thread(24, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_25(self):
        th = self.tm.setup_thread(25, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_26(self):
        th = self.tm.setup_thread(26, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_27(self):
        th = self.tm.setup_thread(27, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_28(self):
        th = self.tm.setup_thread(28, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_29(self):
        th = self.tm.setup_thread(29, 0)
        self.assertEqual(type(th), ingestenum.EnumIngestThread)

    def test_thread_type_assignment_30(self):
        th = self.tm.setup_thread(30, 0)
        self.assertEqual(type(th), query.SinglePlotQuery)

    def test_thread_type_assignment_31(self):
        th = self.tm.setup_thread(31, 0)
        self.assertEqual(type(th), query.SinglePlotQuery)

    def test_thread_type_assignment_32(self):
        th = self.tm.setup_thread(32, 0)
        self.assertEqual(type(th), query.MultiPlotQuery)

    def test_thread_type_assignment_33(self):
        th = self.tm.setup_thread(33, 0)
        self.assertEqual(type(th), query.MultiPlotQuery)

    def test_thread_type_assignment_34(self):
        th = self.tm.setup_thread(34, 0)
        self.assertEqual(type(th), query.SearchQuery)

    def test_thread_type_assignment_35(self):
        th = self.tm.setup_thread(35, 0)
        self.assertEqual(type(th), query.SearchQuery)

    def test_thread_type_assignment_36(self):
        th = self.tm.setup_thread(36, 0)
        self.assertEqual(type(th), query.EnumSearchQuery)

    def test_thread_type_assignment_37(self):
        th = self.tm.setup_thread(37, 0)
        self.assertEqual(type(th), query.EnumSinglePlotQuery)

    def test_thread_type_assignment_38(self):
        th = self.tm.setup_thread(38, 0)
        self.assertEqual(type(th), query.AnnotationsQuery)

    def test_thread_type_assignment_39(self):
        th = self.tm.setup_thread(39, 0)
        self.assertEqual(type(th), query.EnumMultiPlotQuery)

    def test_thread_type_assignment_40(self):
        th = self.tm.setup_thread(40, 0)
        self.assertEqual(type(th), query.EnumMultiPlotQuery)

    def test_thread_type_assignment_41(self):
        th = self.tm.setup_thread(41, 0)
        self.assertEqual(type(th), annotationsingest.AnnotationsIngestThread)

    def test_thread_type_assignment_42(self):
        th = self.tm.setup_thread(42, 0)
        self.assertEqual(type(th), annotationsingest.AnnotationsIngestThread)

    def test_thread_type_assignment_43(self):
        th = self.tm.setup_thread(43, 0)
        self.assertEqual(type(th), annotationsingest.AnnotationsIngestThread)

    def test_thread_type_assignment_44(self):
        th = self.tm.setup_thread(44, 0)
        self.assertEqual(type(th), annotationsingest.AnnotationsIngestThread)

    def test_setup_thread_invalid_thread_type(self):
        self.assertRaises(Exception, self.tm.setup_thread, (45, 0))

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class InitProcessTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(clean_configs(grinder_props))
        self.test_config.update(
                           {'report_interval': (1000 * 6),
                            'num_tenants': 3,
                            'enum_num_tenants': 4,
                            'annotations_num_tenants': 3,
                            'metrics_per_tenant': 7,
                            'enum_metrics_per_tenant': 2,
                            'annotations_per_tenant': 2,
                            'batch_size': 3,
                            'ingest_weight': 2,
                            'enum_ingest_weight': 2,
                            'query_concurrency': 20,
                            'annotations_weight': 2,
                            'singleplot_query_weight': 11,
                            'multiplot_query_weight': 10,
                            'search_query_weight': 9,
                            'enum_search_query_weight': 9,
                            'enum_single_plot_query_weight': 10,
                            'enum_multiplot_query_weight': 10,
                            'annotations_query_weight': 8,
                            'name_fmt': "org.example.metric.%d",
                            'num_nodes': 2})

        self.num_query_nodes = self.test_config['num_nodes']
        self.single_plot_queries_agent0 = int(math.ceil(
            self.test_config['singleplot_query_weight'] /
            self.num_query_nodes))
        self.multi_plot_queries_agent0 = int(math.ceil(
            self.test_config['multiplot_query_weight'] /
            self.num_query_nodes))
        self.search_queries_agent0 = int(math.ceil(
            self.test_config[
                'search_query_weight'] / self.num_query_nodes))
        self.enum_search_queries_agent0 = int(math.ceil(
            self.test_config[
                'enum_search_query_weight'] / self.num_query_nodes))
        self.enum_single_plot_queries_agent0 = int(math.ceil(
            self.test_config[
                'enum_single_plot_query_weight'] /
            self.num_query_nodes))
        self.enum_multi_plot_queries_agent0 = int(math.ceil(
            self.test_config[
                'enum_multiplot_query_weight'] / self.num_query_nodes))
        self.annotation_queries_agent0 = int(math.ceil(
            self.test_config[
                'annotations_query_weight'] / self.num_query_nodes))

        self.single_plot_queries_agent1 = \
            self.test_config['singleplot_query_weight'] - \
            self.single_plot_queries_agent0
        self.multi_plot_queries_agent1 = \
            self.test_config['multiplot_query_weight'] - \
            self.multi_plot_queries_agent0
        self.search_queries_agent1 = \
            self.test_config['search_query_weight'] - \
            self.search_queries_agent0
        self.enum_search_queries_agent1 = \
            self.test_config['enum_search_query_weight'] - \
            self.enum_search_queries_agent0
        self.enum_single_plot_queries_agent1 = \
            self.test_config['enum_single_plot_query_weight'] - \
            self.enum_single_plot_queries_agent0
        self.annotation_queries_agent1 = \
            self.test_config['annotations_query_weight'] - \
            self.annotation_queries_agent0
        self.enum_multi_plot_queries_agent1 = \
            self.test_config['enum_multiplot_query_weight'] - \
            self.enum_multi_plot_queries_agent0

    def test_init_process_annotationsingest_agent_zero(self):

        # confirm that the correct batches of ingest metrics are created for
        # worker 0
        agent_num = 0
        # confirm annotationsingest
        annotationsingest.AnnotationsIngestThread.create_metrics(
            agent_num, self.test_config)

        self.assertEqual(annotationsingest.AnnotationsIngestThread.annotations,
                         [[0, 0], [0, 1], [1, 0], [1, 1]])

        thread = annotationsingest.AnnotationsIngestThread(
            0, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice, [[0, 0], [0, 1]])

        thread = annotationsingest.AnnotationsIngestThread(
            1, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice, [[1, 0], [1, 1]])

    def test_init_process_enumingest_agent_zero(self):
        agent_num = 0
        # confirm enum metrics ingest
        ingestenum.EnumIngestThread.create_metrics(agent_num, self.test_config)

        self.assertEqual(ingestenum.EnumIngestThread.metrics,
                         [
                             [[0, 0], [0, 1], [1, 0]],
                             [[1, 1]]
                         ])

        thread = ingestenum.EnumIngestThread(0, agent_num, MockReq(),
                                             self.test_config)
        self.assertEqual(thread.slice, [[[0, 0], [0, 1], [1, 0]]])

        thread = ingestenum.EnumIngestThread(1, agent_num, MockReq(),
                                             self.test_config)
        self.assertEqual(thread.slice, [[[1, 1]]])

    def test_init_process_ingest_agent_zero(self):

        agent_num = 0

        # confirm metrics ingest
        ingest.IngestThread.create_metrics(agent_num, self.test_config)

        self.assertEqual(ingest.IngestThread.metrics,
                         [[[0, 0], [0, 1], [0, 2]],
                          [[0, 3], [0, 4], [0, 5]],
                          [[0, 6], [1, 0], [1, 1]],
                          [[1, 2], [1, 3], [1, 4]],
                          [[1, 5], [1, 6]]])

        # confirm that the correct batch slices are created for individual
        # threads
        thread = ingest.IngestThread(0, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice,
                         [[[0, 0], [0, 1], [0, 2]],
                          [[0, 3], [0, 4], [0, 5]],
                          [[0, 6], [1, 0], [1, 1]]])
        thread = ingest.IngestThread(1, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice,
                         [[[1, 2], [1, 3], [1, 4]],
                          [[1, 5], [1, 6]]])

    def test_init_process_ingest_agent_one(self):

        agent_num = 1

        # confirm that the correct batches of ingest metrics are created for
        # worker 1
        ingest.IngestThread.create_metrics(agent_num, self.test_config)

        self.assertEqual(ingest.IngestThread.metrics,
                         [[[2, 0], [2, 1], [2, 2]],
                          [[2, 3], [2, 4], [2, 5]],
                          [[2, 6]]])

        thread = ingest.IngestThread(0, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice,
                         [[[2, 0], [2, 1], [2, 2]],
                          [[2, 3], [2, 4], [2, 5]]])
        thread = ingest.IngestThread(1, agent_num, MockReq(), self.test_config)
        self.assertEqual(thread.slice,
                         [[[2, 6]]])

    def test_init_process_annotationsingest_agent_one(self):
        agent_num = 1
        annotationsingest.AnnotationsIngestThread.create_metrics(
            agent_num, self.test_config)
        self.assertEqual(annotationsingest.AnnotationsIngestThread.annotations,
                         [[2, 0], [2, 1]])

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class GeneratePayloadTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(
                           {'report_interval': (1000 * 6),
                            'num_tenants': 3,
                            'enum_num_tenants': 4,
                            'annotations_num_tenants': 3,
                            'metrics_per_tenant': 7,
                            'enum_metrics_per_tenant': 2,
                            'annotations_per_tenant': 2,
                            'batch_size': 3,
                            'ingest_weight': 2,
                            'enum_ingest_weight': 2,
                            'query_concurrency': 20,
                            'annotations_weight': 2,
                            'singleplot_query_weight': 11,
                            'multiplot_query_weight': 10,
                            'search_query_weight': 9,
                            'enum_search_query_weight': 9,
                            'enum_single_plot_query_weight': 10,
                            'enum_multiplot_query_weight': 10,
                            'annotations_query_weight': 8,
                            'name_fmt': "org.example.metric.%d",
                            'num_nodes': 2})

    def test_generate_payload(self):
        agent_num = 1
        ingest.IngestThread.create_metrics(agent_num, self.test_config)
        thread = ingest.IngestThread(0, agent_num, MockReq(), self.test_config)
        payload = json.loads(
            thread.generate_payload(0, [[2, 3], [2, 4], [2, 5]]))
        valid_payload = [{u'collectionTime': 0,
                          u'metricName': u'org.example.metric.3',
                          u'metricValue': 0,
                          u'tenantId': u'2',
                          u'ttlInSeconds': 172800,
                          u'unit': u'days'},
                         {u'collectionTime': 0,
                          u'metricName': u'org.example.metric.4',
                          u'metricValue': 0,
                          u'tenantId': u'2',
                          u'ttlInSeconds': 172800,
                          u'unit': u'days'},
                         {u'collectionTime': 0,
                          u'metricName': u'org.example.metric.5',
                          u'metricValue': 0,
                          u'tenantId': u'2',
                          u'ttlInSeconds': 172800,
                          u'unit': u'days'}]
        self.assertEqual(payload, valid_payload)

    def test_generate_enum_payload(self):
        agent_num = 1
        ingestenum.EnumIngestThread.create_metrics(agent_num, self.test_config)
        thread = ingestenum.EnumIngestThread(0, agent_num, MockReq(),
                                             self.test_config)
        payload = json.loads(thread.generate_payload(1, [[2, 1], [2, 2]]))
        valid_payload = [{
            u'timestamp': 1,
            u'tenantId': u'2',
            u'enums': [{
                u'value': u'e_g_1_0',
                u'name': ingestenum.EnumIngestThread.
                         generate_enum_metric_name(1, self.test_config)
            }]},
            {
                u'timestamp': 1,
                u'tenantId': u'2',
                u'enums': [{
                    u'value': u'e_g_2_0',
                    u'name': ingestenum.EnumIngestThread.
                             generate_enum_metric_name(2, self.test_config)
                }]
            }
        ]
        self.assertEqual(payload, valid_payload)

    def test_generate_annotations_payload(self):
        agent_num = 1
        annotationsingest.AnnotationsIngestThread.create_metrics(
            agent_num, self.test_config)
        thread = annotationsingest.AnnotationsIngestThread(
            0, agent_num, MockReq(), self.test_config)
        payload = json.loads(thread.generate_payload(0, 3))
        valid_payload = {
            'what': 'annotation org.example.metric.3',
            'when': 0,
            'tags': 'tag',
            'data': 'data'}
        self.assertEqual(payload, valid_payload)

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class MakeAnnotationsIngestRequestsTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(
                           {'report_interval': (1000 * 6),
                            'num_tenants': 3,
                            'enum_num_tenants': 4,
                            'annotations_num_tenants': 3,
                            'metrics_per_tenant': 7,
                            'enum_metrics_per_tenant': 2,
                            'annotations_per_tenant': 2,
                            'batch_size': 3,
                            'ingest_weight': 2,
                            'enum_ingest_weight': 2,
                            'query_concurrency': 20,
                            'annotations_weight': 2,
                            'singleplot_query_weight': 11,
                            'multiplot_query_weight': 10,
                            'search_query_weight': 9,
                            'enum_search_query_weight': 9,
                            'enum_single_plot_query_weight': 10,
                            'enum_multiplot_query_weight': 10,
                            'annotations_query_weight': 8,
                            'name_fmt': "org.example.metric.%d",
                            'num_nodes': 2,
                            'query_url': 'http://metrics.example.org',
                            'url': 'http://metrics-ingest.example.org'})

    def test_annotationsingest_make_request(self):
        global sleep_time
        agent_num = 0
        thread = annotationsingest.AnnotationsIngestThread(
            0, agent_num, MockReq(), self.test_config)
        thread.slice = [[2, 0]]
        thread.position = 0
        thread.finish_time = 10000
        valid_payload = {
            "what": "annotation org.example.metric.0",
            "when": 1000, "tags": "tag", "data": "data"}

        url, payload = thread.make_request(pp, thread.time())
        # confirm request generates proper URL and payload
        self.assertEqual(
            url,
            'http://metrics-ingest.example.org/v2.0/2/events')
        self.assertEqual(eval(payload), valid_payload)

        # confirm request increments position if not at end of report interval
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 10000)
        thread.position = 2
        thread.make_request(pp, thread.time())

        # confirm request resets position at end of report interval
        self.assertEqual(sleep_time, 9000)
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 16000)

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class MakeIngestRequestsTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(
                           {'report_interval': (1000 * 6),
                            'num_tenants': 3,
                            'enum_num_tenants': 4,
                            'annotations_num_tenants': 3,
                            'metrics_per_tenant': 7,
                            'enum_metrics_per_tenant': 2,
                            'annotations_per_tenant': 2,
                            'batch_size': 3,
                            'ingest_weight': 2,
                            'enum_ingest_weight': 2,
                            'query_concurrency': 20,
                            'annotations_weight': 2,
                            'singleplot_query_weight': 11,
                            'multiplot_query_weight': 10,
                            'search_query_weight': 9,
                            'enum_search_query_weight': 9,
                            'enum_single_plot_query_weight': 10,
                            'enum_multiplot_query_weight': 10,
                            'annotations_query_weight': 8,
                            'name_fmt': "org.example.metric.%d",
                            'num_nodes': 2,
                            'query_url': 'http://metrics.example.org',
                            'url': 'http://metrics-ingest.example.org'})

    def test_ingest_make_request(self):
        global sleep_time
        agent_num = 0
        thread = ingest.IngestThread(0, agent_num, MockReq(), self.test_config)
        thread.slice = [[[2, 0], [2, 1]]]
        thread.position = 0
        thread.finish_time = 10000
        valid_payload = [
            {"collectionTime": 1000, "ttlInSeconds": 172800, "tenantId": "2",
             "metricValue": 0, "unit": "days",
             "metricName": "org.example.metric.0"},
            {"collectionTime": 1000, "ttlInSeconds": 172800, "tenantId": "2",
             "metricValue": 0, "unit": "days",
             "metricName": "org.example.metric.1"}]

        url, payload = thread.make_request(pp, thread.time())
        # confirm request generates proper URL and payload
        self.assertEqual(
            url,
            'http://metrics-ingest.example.org/v2.0/tenantId/ingest/multi')
        self.assertEqual(eval(payload), valid_payload)

        # confirm request increments position if not at end of report interval
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 10000)
        thread.position = 2
        thread.make_request(pp, thread.time())
        # confirm request resets position at end of report interval
        self.assertEqual(sleep_time, 9000)
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 16000)

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class MakeIngestEnumRequestsTest(TestCaseBase):
    def setUp(self):
        self.real_shuffle = random.shuffle
        self.real_randint = random.randint
        self.real_time = abstract_thread.AbstractThread.time
        self.real_sleep = abstract_thread.AbstractThread.sleep
        random.shuffle = lambda x: None
        random.randint = lambda x, y: 0
        abstract_thread.AbstractThread.time = lambda x: 1000
        abstract_thread.AbstractThread.sleep = mock_sleep

        self.test_config = abstract_thread.default_config.copy()
        self.test_config.update(
                           {'report_interval': (1000 * 6),
                            'num_tenants': 3,
                            'enum_num_tenants': 4,
                            'annotations_num_tenants': 3,
                            'metrics_per_tenant': 7,
                            'enum_metrics_per_tenant': 2,
                            'annotations_per_tenant': 2,
                            'batch_size': 3,
                            'ingest_weight': 2,
                            'enum_ingest_weight': 2,
                            'query_concurrency': 20,
                            'annotations_weight': 2,
                            'singleplot_query_weight': 11,
                            'multiplot_query_weight': 10,
                            'search_query_weight': 9,
                            'enum_search_query_weight': 9,
                            'enum_single_plot_query_weight': 10,
                            'enum_multiplot_query_weight': 10,
                            'annotations_query_weight': 8,
                            'name_fmt': "org.example.metric.%d",
                            'num_nodes': 2,
                            'query_url': 'http://metrics.example.org',
                            'url': 'http://metrics-ingest.example.org'})

    def test_ingest_enum_make_request(self):
        global sleep_time
        agent_num = 0
        thread = ingestenum.EnumIngestThread(0, agent_num, MockReq(),
                                             self.test_config)
        thread.slice = [[[2, 0], [2, 1]]]
        thread.position = 0
        thread.finish_time = 10000
        valid_payload = [
            {
                'tenantId': '2',
                'timestamp': 1000,
                'enums': [{
                    'value': 'e_g_0_0',
                    'name': ingestenum.EnumIngestThread.
                            generate_enum_metric_name(0, self.test_config)
                }]
            },
            {
                'tenantId': '2',
                'timestamp': 1000,
                'enums': [{
                    'value': 'e_g_1_0',
                    'name': ingestenum.EnumIngestThread.
                            generate_enum_metric_name(1, self.test_config)
                }]
            }
        ]

        url, payload = thread.make_request(pp, thread.time())
        # confirm request generates proper URL and payload
        self.assertEqual(url,
                         'http://metrics-ingest.example.org/v2.0/tenantId/' +
                         'ingest/aggregated/multi')
        self.assertEqual(eval(payload), valid_payload)

        # confirm request increments position if not at end of report interval
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 10000)
        thread.position = 2
        thread.make_request(pp, thread.time())
        # confirm request resets position at end of report interval
        self.assertEqual(sleep_time, 9000)
        self.assertEqual(thread.position, 1)
        self.assertEqual(thread.finish_time, 16000)

    def tearDown(self):
        random.shuffle = self.real_shuffle
        random.randint = self.real_randint
        abstract_thread.AbstractThread.time = self.real_time
        abstract_thread.AbstractThread.sleep = self.real_sleep


class MakeQueryRequestsTest(TestCaseBase):
    def setUp(self):
        self.agent_num = 0
        self.config = clean_configs(grinder_props)
        self.requests_by_type = requests_by_type.copy()

    def test_query_make_SinglePlotQuery_request(self):
        random.randint = lambda x, y: 40
        req = requests_by_type[query.SinglePlotQuery]
        qq = query.SinglePlotQuery(0, self.agent_num, req, self.config)
        result = qq._make_request(None, 1000, 0,
                                  'org.example.metric.metric123')
        self.assertEqual(req.get_url,
                         "http://metrics.example.org/v2.0/0/views/" +
                         "org.example.metric.metric123?from=-86399000&" +
                         "to=1000&resolution=FULL")
        self.assertEquals(req.get_url, result)

    def test_query_make_SearchQuery_request(self):
        req = requests_by_type[query.SearchQuery]
        qq = query.SearchQuery(0, self.agent_num, req, self.config)
        result = qq._make_request(None, 1000, 10,
                                  'org.example.metric.*')
        self.assertEqual(req.get_url,
                         "http://metrics.example.org/v2.0/10/metrics/search?" +
                         "query=org.example.metric.*")
        self.assertEquals(req.get_url, result)

    def test_query_make_MultiPlotQuery_request(self):
        req = requests_by_type[query.MultiPlotQuery]
        qq = query.MultiPlotQuery(0, self.agent_num, req, self.config)
        payload_sent = json.dumps([
            "org.example.metric.0",
            "org.example.metric.1",
            "org.example.metric.2",
            "org.example.metric.3",
            "org.example.metric.4",
            "org.example.metric.5",
            "org.example.metric.6",
            "org.example.metric.7",
            "org.example.metric.8",
            "org.example.metric.9"
        ])
        result = qq._make_request(None, 1000, 20,
                                  payload_sent)
        self.assertEqual(req.post_url,
                         "http://metrics.example.org/v2.0/20/views?" +
                         "from=-86399000&to=1000&resolution=FULL")
        self.assertEqual(req.post_payload, payload_sent)
        self.assertEquals((req.post_url, req.post_payload), result)

    def test_query_make_AnnotationsQuery_request(self):
        req = requests_by_type[query.AnnotationsQuery]
        qq = query.AnnotationsQuery(0, self.agent_num, req, self.config)
        result = qq._make_request(None, 1000, 30)
        self.assertEqual(req.get_url,
                         "http://metrics.example.org/v2.0/30/events/" +
                         "getEvents?from=-86399000&until=1000")
        self.assertEquals(req.get_url, result)

    def test_query_make_EnumSearchQuery_request(self):
        req = requests_by_type[query.EnumSearchQuery]
        qq = query.EnumSearchQuery(0, self.agent_num, req, self.config)
        result = qq._make_request(None, 1000, 40)
        self.assertEqual(req.get_url,
                         "http://metrics.example.org/v2.0/40/metrics/search?" +
                         "query=enum_grinder_org.example.metric.*&" +
                         "include_enum_values=true")
        self.assertEquals(req.get_url, result)

    def test_query_make_EnumSinglePlotQuery_request(self):
        req = requests_by_type[query.EnumSinglePlotQuery]
        qq = query.EnumSinglePlotQuery(0, self.agent_num, req, self.config)
        result = qq._make_request(None, 1000, 50,
                                  'enum_grinder_org.example.metric.metric456')
        self.assertEqual(req.get_url,
                         "http://metrics.example.org/v2.0/50/views/" +
                         "enum_grinder_org.example.metric.metric456?" +
                         "from=-86399000&to=1000&resolution=FULL")
        self.assertEquals(req.get_url, result)

    def test_query_make_EnumMultiPlotQuery_request(self):
        req = requests_by_type[query.EnumMultiPlotQuery]
        qq = query.EnumMultiPlotQuery(0, self.agent_num, req, self.config)
        payload_sent = json.dumps([
            "enum_grinder_org.example.metric.0",
            "enum_grinder_org.example.metric.1",
            "enum_grinder_org.example.metric.2",
            "enum_grinder_org.example.metric.3"
        ])
        result = qq._make_request(None, 1000, 4,
                                  payload_sent)
        self.assertEqual(req.post_url,
                         "http://metrics.example.org/v2.0/4/views?" +
                         "from=-86399000&to=1000&resolution=FULL")
        self.assertEqual(req.post_payload, payload_sent)
        self.assertEquals((req.post_url, req.post_payload), result)


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(ThreadManagerTest))
suite.addTest(loader.loadTestsFromTestCase(InitProcessTest))
suite.addTest(loader.loadTestsFromTestCase(GeneratePayloadTest))
suite.addTest(loader.loadTestsFromTestCase(MakeAnnotationsIngestRequestsTest))
suite.addTest(loader.loadTestsFromTestCase(MakeIngestRequestsTest))
suite.addTest(loader.loadTestsFromTestCase(MakeIngestEnumRequestsTest))
suite.addTest(loader.loadTestsFromTestCase(MakeQueryRequestsTest))
unittest.TextTestRunner().run(suite)


class TestRunner:
    def __init__(self):
        pass

    def __call__(self):
        pass


import re

from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

import thread_manager as tm
import py_java
from annotationsingest import AnnotationsIngestThread
from ingest import IngestThread
from ingestenum import EnumIngestThread
from query import SinglePlotQuery, MultiPlotQuery, SearchQuery
from query import EnumSearchQuery, EnumSinglePlotQuery, AnnotationsQuery
from query import EnumMultiPlotQuery
from config import clean_configs
import abstract_thread
from throttling_group import ThrottlingGroup
from throttling_request import ThrottlingRequest

# ENTRY POINT into the Grinder

# The code inside the TestRunner class is gets executed by each worker thread
# Outside the class is executed before any of the workers begin
#
# Module-level code gets run exactly once by the main thread.
#
# TestRunner.__init__ gets run once for each worker thread, and is run by that
# worker thread
#
# TestRunner.__call__ gets run `grinder.runs` times by each worker thread, for
# a total of `grinder.runs` * `grinder.threads` times.
#
# Each worker thread gets its own TestRunner instance, and re-uses that
# instance for all runs
#


config = abstract_thread.default_config.copy()
config.update(clean_configs(py_java.get_config_from_grinder(grinder)))

throttling_groups = {}
for k, v in config.iteritems():
    m = re.match(
        '(grinder\.bf\.)?throttling_group\.(\w+)\.max_requests_per_minute',
        str(k))
    if m:
        name = m.groups()[-1]
        throttling_groups[name] = ThrottlingGroup(name, int(v))


def create_request_obj(test_num, test_name, tgroup_name=None):
    test = Test(test_num, test_name)
    request = HTTPRequest()
    test.record(request)
    if tgroup_name:
        tgroup = throttling_groups[tgroup_name]
        request = ThrottlingRequest(tgroup, request)
    return request

requests_by_type = {
    IngestThread: create_request_obj(1, "Ingest test"),
    EnumIngestThread: create_request_obj(7, "Enum Ingest test"),
    AnnotationsIngestThread:
        create_request_obj(2, "Annotations Ingest test"),
    SinglePlotQuery: create_request_obj(3, "SinglePlotQuery"),
    MultiPlotQuery: create_request_obj(4, "MultiPlotQuery"),
    SearchQuery: create_request_obj(5, "SearchQuery"),
    EnumSearchQuery: create_request_obj(8, "EnumSearchQuery"),
    EnumSinglePlotQuery: create_request_obj(9, "EnumSinglePlotQuery"),
    EnumMultiPlotQuery: create_request_obj(10, "EnumMultiPlotQuery"),
    AnnotationsQuery: create_request_obj(6, "AnnotationsQuery"),
}

thread_manager = tm.ThreadManager(config, requests_by_type)


class TestRunner:
    def __init__(self):
        agent_number = grinder.getAgentNumber()
        self.thread = thread_manager.setup_thread(
            grinder.getThreadNumber(), agent_number, throttling_groups)

    def __call__(self):
        result = self.thread.make_request(grinder.logger.info,
                                          self.thread.time())

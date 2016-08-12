#!/usr/bin/env python

from __future__ import with_statement
import threading
import time


class ThrottlingGroup(object):
    def __init__(self, name, max_requests_per_minute, time_source=None,
                 sleep_source=None):

        if time_source is None:
            time_source = time.time
        if sleep_source is None:
            sleep_source = time.sleep

        self.name = name
        self.max_requests_per_minute = max_requests_per_minute
        self.count = 0
        self.lock = threading.Lock()
        self.start_time = -1
        self.time_source = time_source
        self.sleep_source = sleep_source

    def count_request(self):
        with self.lock:
            current_time = self.time_source()
            if self.start_time < 0:
                self.count += 1
                self.start_time = current_time
                return

            seconds_since_start = current_time - self.start_time
            if seconds_since_start >= 60:
                self.count = 1
                self.start_time = current_time
            elif self.count < self.max_requests_per_minute:
                self.count += 1
                if self.start_time < 0:
                    self.start_time = current_time
            else:
                seconds_to_wait = self.start_time + 60 - current_time
                if seconds_to_wait > 0:
                    self.sleep_source(seconds_to_wait)
                self.count = 1
                self.start_time = self.time_source()

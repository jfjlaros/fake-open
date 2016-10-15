"""
Tests for the fake_open CLI.
"""
import StringIO

from fake_open import fake_open

from shared import md5_check


class TestCLI(object):
    def setup(self):
        self._output = StringIO.StringIO()

    def _md5_check(self, md5sum):
        return md5_check(self._output.getvalue(), md5sum)

    def test_1(self):
        pass

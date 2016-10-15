"""
Tests for the fake_open library.
"""
from __future__ import (
    absolute_import, division, print_function, unicode_literals)
from future.builtins import str, zip

from fake_open import FakeOpen, md5_check, make_fake_file

import rot1


class TestLibrary(object):
    def setup(self):
        opener = FakeOpen()
        self._handles = opener.handles
        rot1.open = opener.open

        self._input = make_fake_file('input_file_name', 'aaaa\n')
        rot1.rot1(self._input, 'output_file_name')

    def test_input_name(self):
        assert self._input.name == 'input_file_name'

    def test_input_data(self):
        assert md5_check(
            self._input.getvalue(), 'e5828c564f71fea3a12dde8bd5d27063')

    def test_output_name_1(self):
        assert self._handles['output_file_name']

    def test_output_name_2(self):
        assert self._handles['output_file_name'].name == 'output_file_name'

    def test_output_data(self):
        assert md5_check(
            self._handles['output_file_name'].getvalue(),
            '059e71e41e137d96d7be0bf827036f6a')

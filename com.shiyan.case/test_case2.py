#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: test_case2.py
@time: 2021/5/17 19:27
"""
import pytest


class TestCase2(object):

    def setup_class(self):
        print("setup_class在每个类之前执行")

    def teardown_class(self):
        print("teardown_class在每个类之后执行")

    def setup_method(self):
        print("setup_method在每个方法之前执行")

    def teardown_method(self):
        print("teardown_method在每个方法之后执行")

    def test_a(self):
        print("test_a")
        assert 1

    def test_b(self):
        print("test_b")
        assert 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_case2.py'])

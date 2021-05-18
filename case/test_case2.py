#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: test_case2.py
@time: 2021/5/17 19:27
"""
import pytest


class TestCase2(object):

    def test_a(self):
        print("test_a")
        assert 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_case2.py'])

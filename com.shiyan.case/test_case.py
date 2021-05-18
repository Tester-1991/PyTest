#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: test_case.py
@time: 2021/5/17 14:57
"""
import pytest


def setup_function():
    print("setup_function每个方法执行之前")


def teardown_function():
    print("teardown_function每个方法执行之后")


def test_a():
    print("test_a")
    assert 1


@pytest.mark.slow
def test_b():
    print("test_b")
    assert 0


if __name__ == '__main__':
    pytest.main(["-s", "test_case.py"])

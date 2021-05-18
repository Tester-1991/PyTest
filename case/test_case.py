#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@author: 石岩
@file: test_case.py
@time: 2021/5/17 14:57
"""
import pytest


def test_a():
    assert 1


if __name__ == '__main__':
    pytest.main(["-s", "test_case.py"])

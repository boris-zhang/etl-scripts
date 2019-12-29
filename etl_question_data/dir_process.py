#!/usr/local/var/pyenv/versions/anaconda3-5.3.1/bin/python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------
File Name   : dir_process.py
Description : 目录和文件操作
Created at  : 2019/12/21
---------------------------------------------------------------------------
"""
__author__ = 'zhang zhiyong'

import warnings
warnings.filterwarnings("ignore")

import os
import jsonpath


def list_dir(path, res):
    """
    递归读取websiterootpath下的目录与文件
    """
    for i in os.listdir(path):
        i = i.strip(' ')
        if i == '' or i == '.DS_Store':    # 过滤mac中的.DS_Store文件
            continue

        temp_dir = os.path.join(path, i)
        if os.path.isdir(temp_dir):
            temp = {"dirname": temp_dir, 'child_dirs': [], 'files': []}
            res['child_dirs'].append(list_dir(temp_dir, temp))
        else:
            res['files'].append(i)
    return res


def json_analysis(jsonobj, indexstr):
    """
    解析json字典，读取对应级别的内容
    :return:
    """
    strlist = jsonpath.jsonpath(jsonobj, indexstr)
    return strlist




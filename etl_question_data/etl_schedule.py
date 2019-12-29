#!/usr/local/var/pyenv/versions/anaconda3-5.3.1/bin/python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------
File Name   : etl_schedule.py
Description : etl主体调度程序。
              1. 目录说明（教材版本如"xx版-六年级下册"）
                a）comp_loading/教材版本：加载数据文件存放目录，期中images目录下存放题目图像文件
                b）comp_loaded/教材版本/images：加载完成的题目图像数据文件存放存放目录
                c）comp_loaded/教材版本/text：加载完成的题目文本数据文件存放存放目录
              2. 循环加载教材版本
                a）images中的数据文件不加载，直接移到 "comp_loaded/教材版本" 目录下
                b）解析数据文件目录名，加载到staging.question_textbook
                c）解析csv数据文件，加载到staging.question_unit_klpoint
                d）解析csv数据文件，加载到staging.question_stem
Created at  : 2019/12/21
---------------------------------------------------------------------------
"""
__author__ = 'zhang zhiyong'

import warnings
warnings.filterwarnings("ignore")

import os
import shutil
import sys
sys.path.append("../pub/lib/")
import dir_process as dp
import load_question_data as lqk


ROOTPATH = '/Users/zhangzhiyong/Desktop/puxue_project/dataset'
DIR_LOADING = 'comp_loading'
DIR_CSV = 'csv'
DIR_IMAGE = 'images'

subject_type = '数学'
if subject_type == '数学':
    DIR_LOADED = 'comp_bak_math'
elif subject_type == '物理':
    DIR_LOADED = 'comp_bak_physics'
elif subject_type == '化学':
    DIR_LOADED = 'comp_bak_chemistry'

tablename_question_textbook = 'staging.question_textbook'
tablename_question_ukt = 'staging.question_unit_klpoint_type'
tablename_question_stem = 'staging.question_stem'


if __name__ == '__main__':
    child_dirs_dirname = '$.child_dirs[:].dirname'
    child_dirs_files = '$.child_dirs[:].files'
    res = {'dirname': 'root', 'child_dirs': [], 'files': []}

    path_loading = ROOTPATH + '/' + DIR_LOADING
    path_loaded = ROOTPATH + '/' + DIR_LOADED
    jsonobj_textbook_list = dp.list_dir(path_loading, res)
    textbook_dirs_list = jsonobj_textbook_list['child_dirs']

    for textbook_dir in textbook_dirs_list:
        path_textbook = textbook_dir['dirname']
        textbook_name = path_textbook.split('/')[-1]
        file_name_list = textbook_dir['files']
        path_textbook_image_src = path_textbook + '/' + DIR_IMAGE
        path_textbook_image_dest = path_loaded + '/' + textbook_name + '/' + DIR_IMAGE

        # a）移动目录下的images到loaded目录
        shutil.move(path_textbook_image_src, path_textbook_image_dest)

        # b）加载版本目录名
        lqk.load_question_textbook(subject_type, textbook_name, path_textbook_image_dest,
                                   tablename_question_textbook)

        # c）加载章节、知识点、题型
        lqk.load_question_unit_klpoint(subject_type, textbook_name, file_name_list,
                                       tablename_question_textbook, tablename_question_ukt)

        # d）加载文件数据
        print(path_textbook, textbook_name)
        lqk.load_file_data(tablename_question_stem, tablename_question_textbook, tablename_question_ukt,
                           path_textbook, subject_type, textbook_name)

        # e）csv数据加载完成，将数据文件移到loaded目录
        path_textbook_csv_dest = path_loaded + '/' + textbook_name + '/' + DIR_CSV
        shutil.move(path_textbook, path_textbook_csv_dest)

        # exit()

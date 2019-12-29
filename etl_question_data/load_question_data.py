#!/usr/local/var/pyenv/versions/anaconda3-5.3.1/bin/python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------
File Name   : load_question_data.py
Description : 解析数据文件目录名，加载到数据表中。
Created at  : 2019/12/21
---------------------------------------------------------------------------
"""
__author__ = 'zhang zhiyong'

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import csv

import sys
sys.path.append("../pub/lib/")
import mysql_conn as msc


def load_question_textbook(subject_type, textbook_name, path_textbook_image, tablename):
    """
    加载教材版本信息
    """
    mysql = msc.MyPymysqlPool("dbMysql")
    init_sql = ''.join(['insert into ', tablename, "(path_image_loaded,textbook_name," \
                            "textbook_version_name,grade_name,subject_type,load_time) " \
                            " values('str_path_textbook_image', 'str_textbook_name'," \
                            "        'str_textbook_version_name', 'str_grade_name'," \
                            "        'str_subject_type', CURRENT_TIMESTAMP());", ])

    str_textbook_version_name = textbook_name.split('-')[0].strip(' ')
    str_grade_name = textbook_name.split('-')[1].strip(' ')

    sql = init_sql.replace('str_path_textbook_image', path_textbook_image)
    sql = sql.replace('str_textbook_name', textbook_name)
    sql = sql.replace('str_textbook_version_name', str_textbook_version_name)
    sql = sql.replace('str_grade_name', str_grade_name)
    sql = sql.replace('str_subject_type', subject_type)
    mysql.insert(sql)
    mysql.dispose()


def load_question_unit_klpoint(subject_type, textbook_name, file_name_list,
                               tablename_question_textbook, tablename_question_ukt):
    """
    加载文件名对应的章节、知识点信息
    文件名示例: 第1章 两、三位数乘一位数-整数的乘法及应用-单选.csv
               1  时、分、秒-时、分、秒及其关系、单位换算与计算-判断题.csv
    注：由于文件名格式有错误，加载后需要手工编辑数据
    """
    mysql = msc.MyPymysqlPool("dbMysql")

    # 读取数据表中的目录名
    sql0 = ''.join(['select textbook_id from ', tablename_question_textbook, \
                   " where textbook_name='", textbook_name, "' and subject_type='", subject_type, "';", ])
    rstData = mysql.getAll(sql0)
    textbook_id = pd.DataFrame(list(list(x.values()) for x in rstData)).iloc[0][0]

    init_sql_quk = ''.join(['insert into ', tablename_question_ukt, \
                            "(file_name,textbook_id,unit_name," \
                            "knowledge_name,question_type_name,load_time) " \
                            " values('str_file_name', ", str(textbook_id), ", 'str_unit_name'," \
                            "        'str_knowledge_name', 'str_question_type_name', CURRENT_TIMESTAMP());", ])

    # 文件名："1　观察物体（三）-正方体的特征-判断题.csv"
    for str_file_name in file_name_list:
        str_file_name_prefix = str_file_name.split('.')[0].strip(' ')
        str_unit_name = str_file_name_prefix.split('-')[0]
        str_knowledge_name = str_file_name_prefix.split('-')[1]
        str_question_type_name = str_file_name_prefix.split('-')[2]

        sql = init_sql_quk.replace('str_file_name', str_file_name)
        sql = sql.replace('str_unit_name', str_unit_name)
        sql = sql.replace('str_knowledge_name', str_knowledge_name)
        sql = sql.replace('str_question_type_name', str_question_type_name)
        # print(sql)
        mysql.insert(sql)
    mysql.dispose()


def load_file_data(tablename_question_stem, tablename_question_textbook, tablename_question_ukt,
                   path_textbook, subject_type, textbook_name, skipfirstrow=True):
    """
    读取数据表中的文件路径，加载文件数据
    """
    mysql = msc.MyPymysqlPool("dbMysql")

    # 读取数据表中的目录名
    sql0 = ''.join(['select file_id,file_name from ', tablename_question_ukt, \
                   " t1 inner join ", tablename_question_textbook, " t2 on t1.textbook_id=t2.textbook_id"
                   " where t2.textbook_name='", textbook_name , "' and t2.subject_type='", subject_type, \
                   "' order by file_id;", ])
    rstData = mysql.getAll(sql0)
    if rstData:
        dataSet = pd.DataFrame(list(list(x.values()) for x in rstData))

        init_sql = ''.join(['insert into ', tablename_question_stem, \
                            "(file_id,row_no,question_stem,question_options,difficulty,image_filename,url,load_time)" \
                           " values(str_file_id, str_row_no, 'str_question_stem', " \
                                   "'str_question_options', str_difficulty, 'str_image_filename', " \
                                   "'str_url', CURRENT_TIMESTAMP());", ])
        for i in range(dataSet.shape[0]):
            str_file_id = str(dataSet.iloc[i][0])
            path_file_name = path_textbook + '/' + str(dataSet.iloc[i][1])

            # 读取文件内容，形如：[',5千克铁的质量大于5000克棉花的质量．（ \xa0 ）,', '', '难度: 0.47', '*.png']
            # mysql.begin()   # 开启事务
            with open(path_file_name, 'r') as f:
                reader = csv.reader(f)
                row_no = 1
                for line in reader:
                    if skipfirstrow and row_no == 1:    # 跳过首行
                        row_no += 1
                        continue
                    str_question_stem = line[0].strip(',').replace('。,', '。').replace('\'', '"')
                    str_question_options = line[1].replace('[', '').replace(']', '').replace('\'', '').replace('、,', '、').strip(',')
                    str_difficulty = line[2].strip('难度: ')
                    str_image_filename = line[3].strip(' ')
                    str_url = line[4].strip(' ')
                    # print(line, str_question_stem, str_option, str_difficulty, str_image_filename, str_url)

                    # 插入文件名关联数据
                    sql = init_sql.replace('str_file_id', str_file_id)
                    sql = sql.replace('str_row_no', str(row_no))
                    sql = sql.replace('str_question_stem', str_question_stem)
                    sql = sql.replace('str_question_options', str_question_options)
                    sql = sql.replace('str_difficulty', str_difficulty)
                    sql = sql.replace('str_image_filename', str_image_filename)
                    sql = sql.replace('str_url', str_url)
                    try:
                        # if str_file_id == '2113' and row_no == 2:
                        #     print('path_file_name1: ', path_file_name, str_file_id, '-', row_no)
                        #     print(sql)
                        mysql.insert(sql)
                    except Exception:
                        print('path_file_name: ', path_file_name, str_file_id, '-', row_no)
                        print(sql)

                    row_no += 1
                f.close()
            mysql.end()     # 结束提交
        mysql.dispose()


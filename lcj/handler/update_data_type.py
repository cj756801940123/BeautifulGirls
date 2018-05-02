#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import jieba
import jieba.analyse
import re
from lcj.handler import database_handler
from lcj.handler import file_util

file_path = (os.path.dirname(os.path.dirname(os.path.abspath("update_data_type.py"))) + '/data/').replace('\\', '/')

def update_data_type():
    jieba.load_userdict(file_path + 'train_files/dictionary.txt')
    tables = ['product_eye','product_perfume', 'product_baseMakeup','product_other_perfume','product_lipstick',]
    # tables = ['product_lipstick']

    for table in tables:
        data = '%万%'
        sql = ' select comment_count,id from '+table+' where comment_count like %s '
        comment_count = database_handler.search_sql(sql,data)
        for i in comment_count:
            comment = i[0]
            id = i[1]
            print(comment)
            index = comment.find('.')
            if index > 0:
                comment = int(comment[0:index])

            print(comment)
            # sql = 'update '+table+' set comment_count=%s where id=%s'
            # data = [comment,id]
            # database_handler.update_sql(sql,data)

if __name__ == '__main__':
    # file_util.del_duplicate('train_files/dictionary.txt')
    update_data_type()

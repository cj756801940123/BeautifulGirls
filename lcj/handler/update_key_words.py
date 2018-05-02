#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import jieba
import jieba.analyse
import re
from lcj.handler import database_handler
from lcj.handler import file_util

file_path = (os.path.dirname(os.path.dirname(os.path.abspath("update_key_words.py"))) + '/data/').replace('\\', '/')

def update_key_words():
    jieba.load_userdict(file_path + 'train_files/dictionary.txt')
    tables = ['product_eye','product_perfume', 'product_baseMakeup','product_other_perfume','product_lipstick',]

    for table in tables:
        sql = ' select key_words,platform,id from '+table
        results = database_handler.search_sql(sql,None)
        # print(results)
        for i in results:
            key_words = i[0]
            platform = i[1]
            id = i[2]
            if platform=='' or platform is None or key_words=='' or key_words is None:
                continue
            platform = ' '.join(jieba.cut(platform))
            key_words = platform +' '+ key_words
            # print(key_words)
            sql = 'update '+table+' set key_words=%s where id=%s'
            data = [key_words,id]
            database_handler.update_sql(sql,data)

if __name__ == '__main__':
    file_util.del_duplicate('train_files/dictionary.txt')
    # update_key_words()

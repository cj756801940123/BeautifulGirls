#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import jieba
import jieba.analyse
import re
from lcj.handler import database_handler
from lcj.handler import file_util

file_path = (os.path.dirname(os.path.dirname(os.path.abspath("full_index.py"))) + '/data/').replace('\\', '/')

def update_key_words():
    jieba.load_userdict(file_path + 'train_files/dictionary.txt')
    tables = ['product_eye','product_perfume', 'product_baseMakeup','product_other_perfume','product_lipstick',]
    # tables = ['product_lipstick']

    for table in tables:
        # database_handler.update_sql(' alter table '+table+' engine=innodb', None)
        # database_handler.update_sql(' alter table ' + table + ' add key_words varchar(255)', None)
        # database_handler.update_sql(' alter table '+ table + ' add fulltext index keyword_index (key_words)', None)
        data = '%.%'
        sql = ' select description from '+table+' where comment_count like %s '
        # sql = ' select description from '+table
        descriptions = database_handler.search_sql(sql,data)
        for i in descriptions:
            description = i[0]
            former = i[0]
            if description=='' or description is None:
                continue
            word = re.sub('[^a-zA-Z]',' ',description)
            description = re.sub("[\s+\.\!\/_,$%^*()?;；:\-【】+\"\']+|[+——\-！，;:。？、~@#￥%……&*（）]+", "", description)
            description = word + description
            description = ' '.join(list(set(jieba.cut(description))))
            print(description)
            sql = 'update '+table+' set key_words=%s where description=%s'
            data = [description,former]
            database_handler.update_sql(sql,data)

if __name__ == '__main__':
    # file_util.del_duplicate('train_files/dictionary.txt')
    update_key_words()

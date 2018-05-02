#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from operator import itemgetter
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from lcj.handler import database_handler
import jieba

file_path = (os.path.dirname(os.path.dirname(os.path.abspath("mapping_handler.py"))) + '/data/').replace('\\','/')

#获取应该去哪些数据库表中查询
def get_tables_and_keywords(keyword):
    if keyword.find('唇')>=0 or keyword.find('口')>=0 or keyword.find('嘴')>=0:
        tables = ['product_lipstick']
    elif keyword.find('眼')>=0 or keyword.find('睫毛')>=0 or keyword.find('眉')>=0:
        tables = ['product_eye']
    elif keyword.find('香水')>=0:
        tables = ['product_perfume','product_other_perfume']
    else:
        tables = ['product_baseMakeup']

    #获取需要模糊匹配的单词
    temp = list(jieba.cut(keyword))
    keywords = []
    for i in temp:
        keywords.append('%'+i+'%')
    return tables,keywords

def get_other_tables(tables):
    kinds = ['product_lipstick','product_eye','product_perfume', 'product_baseMakeup','product_other_perfume']
    for i in tables:
        kinds.remove(i)
    return kinds

def handle_sql_results(tables,keywords,page_no):
    #获取需要进行查询的sql语句
    sql_list = []
    for i in tables:
        sql = 'select name,price,img1_address,address,good_comment_percentage,comment_count,platform,description from '+i+' where description like %s'
        for j in range(len(keywords)-1):
            sql = sql+' and description like %s'
        sql_list.append(sql)

    #进行sql查询并处理查询结果
    all_list = []
    for i in sql_list:
        temp = list(database_handler.execute_sql(i,keywords))
        if len(temp)==0:
            continue
        for j in temp:
            item = list(j)
            comment_num = item[5]
            index = comment_num.find('万')
            if index>0:
                item[5] = float(comment_num[0:index])*10000
            else:
                index = comment_num.find('+')
                if index>0:
                    item[5] = float(comment_num[0:index])
                else:
                    item[5] = float(comment_num)
            all_list.append(item)

    result = {}
    if len(all_list) ==0:
        result['error_code'] = 1
        result['msg'] = '搜索不出对应的产品!'
        result['page_count'] = 0
        return result

    all_list.sort(key=itemgetter(5,4), reverse=True)

    items = []
    start = (page_no-1)*20
    for i in range(start,start+20):
        if(i<len(all_list)):
            temp = {}
            temp["name"] = all_list[i][0]
            temp["price"] = float(all_list[i][1])
            temp["img1_address"] = all_list[i][2]
            temp["address"] = all_list[i][3]
            temp["good_comment_percentage"] = all_list[i][4]
            temp["comment_count"] = int(all_list[i][5])
            temp["platform"] = all_list[i][6]
            temp["description"] = all_list[i][7]
            items.append(temp)

    data = {}
    data['item_list'] = items
    result['error_code'] = 0
    result['msg'] = 'success'
    result['data'] = data


    page_count = int(len(all_list)/20)
    if len(all_list)%20>0 :
        page_count +=1
    result['page_count'] = page_count
    return result

def get_products_page(keyword,page_no):
    result = get_tables_and_keywords(keyword)
    tables = result[0]
    keywords = result[1]
    result = handle_sql_results(tables, keywords, page_no)
    print(result)
    page_count = int(result['page_count'])

    if page_count==0:
        tables = get_other_tables(tables)
        result = handle_sql_results(tables, keywords, page_no)
    return result


@require_http_methods(["GET"])
def handle_search(request):
        keywords = request.GET.get('wd')

        page_no = request.GET.get('PageNo')
        print (keywords,page_no)
        results = get_products_page(keywords,int(page_no))
        print (results)
        return JsonResponse(results,safe=False)

if __name__ == '__main__':
    # http://127.0.0.1:8000/productsList/getProductsPage?wd=卡姿兰蜗牛气垫调控霜&PageNo=1
    keyword = '卡姿兰蜗牛气垫调控霜'
    page_no = 2
    get_products_page(keyword,page_no)









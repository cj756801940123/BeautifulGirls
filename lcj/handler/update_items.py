#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql

def updateDB_baseMakeup(item,tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time,good_for_skin,SPF,"
            "PA)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s')"
            % (tableName,item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time, item.good_for_skin, item.SPF,
               item.PA)
        )
        db.commit()
    except Exception as e:
        print(e)
        #raise e
    finally:
        db.close()  # 关闭连接

def updateDB_lipstick(item, tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s')"
            % (tableName, item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time)
        )
        db.commit()
    except Exception as e:
        print(e)
        # raise e
    finally:
        db.close()  # 关闭连接

def updateDB_eye(item, tableName):
    db = pymysql.connect(host="39.108.185.66", user="root", password="1234", db="beautyGirls_database", port=3306,
                         charset="utf8")
    cur = db.cursor()  # 获取操作游标
    try:
        cur.execute(
            "INSERT INTO %s( first_category,third_category,second_category,"
            "img1_address,img2_address,img3_address,img4_address,img5_address,"
            "address,price,description,number,name,"
            "brand,produce_address,comment_count,kg,good_for_who,"
            "expiration_date,color,result_effectiveness,category,makeup_effectiveness,"
            "good_comment_percentage,who_handly,get_time)"
            "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s',"
            "'%s','%s','%s','%s','%s','%s','%s','%s')"
            % (tableName, item.first_category, item.third_category, item.second_category,
               item.img1_address, item.img2_address, item.img3_address, item.img4_address, item.img5_address,
               item.address, item.price, item.description, item.number, item.name,
               item.brand, item.produce_address, item.comment_count, item.kg, item.good_for_who,
               item.expiration_date, item.color, item.result_effectiveness, item.category,
               item.makeup_effectiveness,
               item.good_comment_percentage, item.who_handly, item.get_time)
        )
        db.commit()
    except Exception as e:
        print(e)
    finally:
        db.close()  # 关闭连接


#记住要先修改数据库表的内容
#getItemURL('https://list.jd.com/list.html?cat=1316,1387,13549',"D:/itemDetailURL_eye.txt")
#searchItem("D:/itemDetailURL_eye.txt",'美妆个护','香水彩妆','眼线','jd_product_eye','jd_hk_product_eye','eye')
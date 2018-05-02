
class Item(object):
    def __init__(self):
        self.first_category = ''        #一级大类，比如美妆个护'
        self.second_category = ''       #二级大类，比如香水彩护'
        self.third_category = ''        #一级大类，比如美妆个护
        self.address = ''               #商品链接网址
        self.description = ''           #商品全称/简述，比如"克丽丝汀迪奥DIOR魅惑润唇蜜SPF10 3.5g"
        self.price = 200                #decimal(10,2) NULL
        self.img1_address = ''          #商品图片的链接地址，至少一个，至多5个
        self.img2_address = ''          #商品图片的链接地址，至少一个，至多5个
        self.img3_address = ''          #商品图片的链接地址，至少一个，至多5个
        self.img4_address = ''          #商品图片的链接地址，至少一个，至多5个
        self.img5_address = ''          #商品图片的链接地址，至少一个，至多5个
        self.brand = ''                 #品牌，比如迪奥
        self.name = ''                  #商品名字，比如迪奥唇膏
        self.number = ''                #varchar(30) NULL COMMENT商品编号，比如1458853
        self.kg = ''                    #varchar(255) NULL COMMENT商品毛重，比如35.00g
        self.produce_address = ''       #varchar(255) NULL COMMENT产地，比如法国
        self.good_for_who = ''          #varchar(255) NULL COMMENT '适用人群' ,
        self.good_for_skin = ''
        self.expiration_date=''         # datetime NULL COMMENT '保质期' ,
        self.color=''                   #varchar(255) NULL COMMENT '比如橘黄色' ,
        self.result_effectiveness = ''  #varchar(255) NULL COMMENT '功效，比如“丰唇”' ,
        self.category =''               #varchar(255) NULL COMMENT '分类，比如“唇膏/口红”' ,
        self.makeup_effectiveness = ''  #varchar(255) NULL COMMENT '妆效' ,
        self.SPF = ''
        self.PA = ''
        self.comment_count = ''         #varchar(255) NULL COMMENT '商品评价总数，比如：4万+' ,
        self.good_comment_percentage = ''  #varchar(255) NULL COMMENT '好评度，比如78%' ,
        self.get_time = ''
        self.who_handly = '刘彩君'         #varchar(255) NULL COMMENT '负责人，爬取这条记录的人的名字，比如张敏华' ,


def getItem():
    item = Item()
    return item

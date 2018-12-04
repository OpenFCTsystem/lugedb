
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# import pymysql
# from Tengxun import settings



class TengxunPrintPipeline(object):

    def process_item(self, item, spider):
        print("=================")
        print('职位名称：' + item["zhName"])
        print('职位链接：' + item["zhLink"])
        print('职位类型：' + item["zhType"])
        print('招聘人数：' + item["zhNum"])
        print('工作地点：' + item["zhAddress"])
        print('发布时间：' + item["zhTime"])
        print("=================")
        return item


# class TengxunMongoPipeline(object):
#     '''使用mangodb数据库存储数据'''
#     def __init__(self):
#         # 从settings.py中获取变量的值
#         host = settings.MONGODB_HOST
#         port = settings.MONGODB_PORT
#         # 创建数据库连接对象、库对象、集合对象
#         conn = pymongo.MongoClient(host=host,port=port)
#         db = conn.Tencent
#         self.myset = db.zhaoping
#     def process_item(self, item, spider):
#         # 把item对象转为字典
#         bookInfo = dict(item)
#         self.myset.insert(bookInfo)
#         print("存入数据库成功")
#         return item


# class TengxunMysqlPipeline(object):
#     '''使用mysql数据库存储数据'''
#     def __init__(self):
#         #初始化数据库，需要确保数据库开启服务
#         host = settings.MYSQL_HOST
#         user = settings.MYSQL_USER
#         pwd = settings.MYSQL_PWD
#         dbName = settings.MYSQL_DB
#         self.db = pymysql.connect(host=host,user=user,
#                      password = pwd,
#                      db = dbName,
#                      charset = "utf8")
#         #创建游标对象
#         self.cursor = self.db.cursor()

#     def process_item(self,item,spider):
#         #需要提前创建表定义字段
#         ins = 'insert into 表名 values(%s,%s,%s,%s,%s,%s)'
#         L = [item['zhName'],item['zhLink'],item['zhType'],item['zhNum'],item['zhAddress'],item['zhTime']]
#         self.cursor.execute(ins,L)
#         self.db.commit()
#         return item


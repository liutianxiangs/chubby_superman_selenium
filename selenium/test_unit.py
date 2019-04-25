#__author__ = 'chubby_superman'  胖超人
#_*_coding=utf-8 _*
import pymysql

class db_ope():
    def __init__(self,host,user,password,port,lib):
        self.host=host
        self.user=user
        self.password=password
        self.lib=lib
        self.port=port
    # 连接数据库
    def get_db(self):
        db = pymysql.connect(self.host,self.user,self.password,self.lib,self.port,charset='utf8')
        return db
    #查询方法
    def select_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            data = cursor.fetchone()
        except Exception as e:
            print(e)
            database.rollback()
        print("查询结果\n",data)
        database.close()
        return data
    #插入方法
    def insertinto_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            #print("保存成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            raise e
            print("保存失败")
            database.rollback()
        database.close()
    def delete_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            print("删除成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            print(e)
            database.rollback()
        database.close()
    def updata_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            print("更新成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            print(e)
            database.rollback()
        database.close()

if __name__ == "__main__":
    host = "rm-.mysql.rds.aliyuncs.com"
    user = "pipitest"
    password = "abcd1234_"
    port = 3306
    lib = "pipitest"
    data_base=db_ope(host,user,password,port,lib)
    data_base.select_func("select * from shelf_goods WHERE id=11616")


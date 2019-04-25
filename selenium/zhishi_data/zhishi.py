#__author__ = 'chubby_superman'  胖超人
#_*_coding=utf-8 _*
import pyodbc
import pymysql
import schedule
def connect_db(ip,username,password,libname):
    db = pyodbc.connect(ip,username,password,libname)
    return db.cursor()

def con_mysql(ip,username,password,libname):
    db = pymysql.connect(ip,username,password,libname)
    return db.cursor()

def select_db(db,tablename):
    try:
        db.execute("select * from %s;"%tablename)
        index = db.description
        head =[]
        for i in index:
            head.append(i[0])
        return list(db.fetchall()),head
        db.close
    except Exception as e:
        print(e)
        db.rollback
def txt_w(file_path,name,a):
    x = file_path+name
    with open(x,mode="w") as f:
        f.write(str(a[-1])+'\n')
    for i in a[0]:
        with open(x,mode="a") as f:
            f.write(str(list(i))+'\n')

def main(ip,username,password,libname,tablename,file_path,name,mysql_ip,mysql_username,mysql_password,mysql_libname):
    infor_db = connect_db(ip,username,password,libname)
    r = select_db(infor_db,tablename)
    txt_w(file_path,name,r)#写入txt
    try:                         #写入mysql表
        for i in r[0]:
            print(i)
            con_mysql(mysql_ip,mysql_username,mysql_password,mysql_libname).execute("insert into chubby_superman_test(`id`, `symptom_id`, `image`, `path`, `status`, `order_no`, `create_time`) VALUES %s"%(str(i)))
    except Exception as e:
        print(e,1)
ip = r"rm-aliyun.com"
username="pipitest"
password="abcd1234_"
libname="pipitest"
tablename="shelf_banner"
file_path=r"C:\Users\Administrator\Desktop/"
name = "bbb.txt"
mysql_ip= r"rm-aliyun.com"
mysql_username="pipitest"
mysql_password="abcd1234_"
mysql_libname="pipitest"

schedule.every(5).seconds.do(main,ip,username,password,libname,tablename,file_path,name,mysql_ip,mysql_username,mysql_password,mysql_libname)
#schedule.every(5).seconds.do(sql_test_database,0)#每隔5秒执行sql_test_database方法
#schedule.every(5).minutes.do(sql_test_database)#每隔五分钟执行sql_test_database方法
#schedule.every(5).hours.do(sql_test_database)#每隔5小时执行sql_test_database方法
while 1:
    schedule.run_pending()
#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*


import schedule
import time

def sql_test_database(count,ass):
    print(time.time())

schedule.every(5).seconds.do(sql_test_database,1,1)#每隔5秒执行sql_test_database方法
#schedule.every(5).minutes.do(sql_test_database)#每隔五分钟执行sql_test_database方法
#schedule.every(5).hours.do(sql_test_database)#每隔5小时执行sql_test_database方法

if __name__ == '__main__':
    while 1:
        schedule.run_pending()


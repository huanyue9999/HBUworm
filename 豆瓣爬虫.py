import requests
from bs4 import BeautifulSoup
import time
import random

import pymysql
import requests
from lxml import etree




# 设置header
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Connection': 'keep - alive'
        }
movie_list = []

def get_pages_link():
    # https://movie.douban.com/top250?start=25
    for item in range(1,25,1):
        url = "https://www.liepin.com/zhaopin/?init=-1&headckid=8b8a11cc05e34e78&fromSearchBtn=2&ckid=8b8a11cc05e34e78&degradeFlag=0&key=Java开发".format(item)
        web_data = requests.get(url,headers=header)
        time.sleep(1 + random.random())
        soup = BeautifulSoup(web_data.text,'lxml')
        for item in soup.select('.sojob-list li'):
            job = item.select('.job-info h3 a')[0].get_text().strip()
            condition = item.select('.condition')[0].get_text()
            (salary,addr,edu,experence) = condition.split()
            print(job)
            print(salary)
            print(addr)
            print(edu)
            print(experence)
            date = item.select('time')[0].attrs['title']
            print(date)
            company = item.select('.company-name')[0].get_text().strip()
            print(company)
            field = item.select('.field-financing')[0].get_text().strip()
            print(field)
            node = item.select('.temptation')
            if node:
                temptation = item.select('.temptation')[0].get_text().strip()
                print(temptation)
            print('-' * 20)

            db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='zhaopin',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
            try:
                # 使用cursor()创建游标对象cursor
                cursor = db.cursor()
                # 使用execute()方法执行SQL DROP: 如果表存在则删除
                cursor.execute("drop table if exists stockinfo")
                # 创建表语句
                # ENGINE=InnoDB使用innodb引擎,为MySQL AB发布binary的标准之一.
                # DEFAULT CHARSET=utf8 数据库默认编码为utf-8
                sql = """
                        create table stockinfo(
                        id int(11) not null primary key auto_increment,
                        stockid int(11) not null,
                        stockname varchar(64) not null)
                        ENGINE=InnoDB DEFAULT CHARSET=utf8;
                    """
                # 执行sql语句
                cursor.execute(sql)

                sql_stock = """insert into jobs (job,salary,addr,edu,exper) values('%s', '%s', '%s', '%s', '%s')""" % (job, salary, addr, edu,experence)

                cursor.execute(sql_stock)

                db.commit()
                print("代码执行完毕!")

            except pymysql.Error as err:
               print(err)
            finally:
               cursor.close()
               db.close()
    print('\n' + ' - ' * 50 + '\n')
if __name__ =='__main__':
    get_pages_link()


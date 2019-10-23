import  pymysql
import re

db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='dict',
                    charset='utf8')
cur=db.cursor()
f=open('/home/tarena/1908/month02/day01/dict.txt','r')
# for line in f:
# word=line.split('　',1)[0]
# mean=line.split(' ',1)[1].srtip(' ')
args_list=[]
for line in f:
    #获取单词和解释
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    args_list.append(tup)
f.close()
try:
    sql="insert into words(word,mean) values(%s,%s)"
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
cur.close()
db.close()
import requests
import json
import csv

L1='121.54,30.10' #左上坐标
L2='121.64,30.05' #右下坐标
a=float(L1.split(',')[0])  #左上坐标x
b=float(L1.split(',')[1])  #左上坐标y
c=float(L2.split(',')[0])  #右下坐标x
d=float(L2.split(',')[1])  #右下坐标y


def request_data(url):
    req = requests.get(url, timeout=30) # 请求连接
    req_jason = req.json() # 获取数据
    return req_jason
i=[]


n=6 #划分表格x轴
m=10   #划分表格y轴

f = open('公司企业.csv', 'w', encoding='gbk',newline='')
csv_writer=csv.writer(f);
csv_writer.writerow(["name","x","y","type","id","address"])

for x in range(n):
    for y in range(n):
        z1=str(a+x*(c-a)/n) + ',' + str(b+y*(d-b)/m)
        z2=str(a+(x+1)*(c-a)/n) + ',' + str(b+(1+y)*(d-b)/m)
        print(z1,'   ',z2)
        for k in range(10):
            url="https://restapi.amap.com/v5/place/polygon?polygon=" + str(z1) + "|" + str(z2)+ "&page_size=25&types=公司企业&key=&page_num="+str(k+1)  #添加你的key
            i=request_data(url)['pois']+i
        print("数据抓取成功")
        #data=json.dumps(i)
        #data1=json.loads(data)        

for j in range(len(i)):
    try:
        csv_writer.writerow([i[j]['name'],i[j]['location'].split(',')[0],i[j]['location'].split(',')[1],i[j]['type'],i[j]['id'],i[j]['address']])
    except:
        pass
print("写入表格成功")
f.close()

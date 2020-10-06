import re
import requests
from bs4 import BeautifulSoup

print("正在设置变量......")
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"}
url ="http://www.op.gg/champion/statistics"
debug_mode = 0
keylist=[]
zhlist=[]
posdict={}
poszh2en={'上单':'top','中单':'mid','打野':'jungle','下路':'bot','辅助':'support'}
print("正在打开目录站点，并获取英雄中英文名以及位置信息......")
req = session.get(url,headers=headers)
soup=BeautifulSoup(req.text,'lxml')

for k in soup.find_all('div',class_='champion-index__champion-item__name'):
	k=k.string
	key = k.parent.parent.parent['data-champion-key']
	if(debug_mode):
		print(k)
		print(key)
	zhlist.append(k)
	keylist.append(key)
	k1str=''
	for k1 in k.parent.parent.find_all('div',class_='champion-index__champion-item__position'):
		k1str+=poszh2en[k1.span.string]+','
	k1str=k1str.strip(',')
	posdict[key]=k1str
print("开始获取英雄数据：")
if len(zhlist)==len(keylist):
	filename="./herodata/hero_data.txt"
	with open(filename,'w') as f:
		for i in range(len(keylist)):
			print('正在获取英雄数据：'+str(i)+zhlist[i]+':'+keylist[i])
			for pos in posdict[keylist[i]].split(','):
				herourl="http://www.op.gg/champion/"+keylist[i]+"/statistics/"+pos+"/matchup"
				req=session.get(herourl,headers=headers)
				soup=BeautifulSoup(req.text,'lxml')
				wtstr=zhlist[i]+"|"+pos+"|"
				for k in soup.find_all('div',class_='champion-matchup-list__champion'):
					wtstr+=k.span.string.strip()+':'
					for kn in k.find_all('span',class_='champion-matchup-list__winrate'):
						wtstr+=kn.string.strip()+','
				wtstr=wtstr.strip(',')
				wtstr+='\n'
				f.write(wtstr)
	print("程序完成")

else:
	print("中英两个英雄列表英雄数量不同！请检查\n")
	print(len(zhlist))
	print(len(keylist))

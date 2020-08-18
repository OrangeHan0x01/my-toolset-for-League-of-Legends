import argparse

parser = argparse.ArgumentParser(description="使用方法：")
parser.add_argument("-n","--hero_name",help="显示英雄的克制、被克制关系，分为轻微（52%%/48%%）和严重（55%%/45%%）")
parser.add_argument("-s","--statistics",help="输入位置（top,mid,jungle,bot,support）可统计不怎么被克制的英雄、克制得分较高的英雄，输入all则统计全英雄")
parser.add_argument('-i','--item',help='输入英雄名，给出装备的胜率排行，功能正在设计中')
args = parser.parse_args()
filename="./herodata/hero_data.txt"
poslist = ['top','mid','jungle','bot','support']
trenddata = "./herodata/hero_trend.txt"
hero_trend = []
hero_data = []

def get_trend_data():
	with open(trenddata,'r') as f0:
		trend_t = f0.readlines()
	return trend_t

def get_data():
	with open(filename,'r') as f:
		data_t = f.readlines()
	return data_t

def trend_distinguish(trend):
	if(trend>=15):
		return 3
	elif(trend>=10):
		return 2
	elif(trend>=5):
		return 1.1
	elif(trend>=2):
		return 0.9
	elif(trend>=0.5):
		return 0.5
	elif(trend>=0.07):
		return 0.3
	else:
		return 0

hero_trend=get_trend_data()
hero_data=get_data()

if(args.hero_name):
	for i in range(len(hero_data)):
		if(hero_data[i].split('|')[0]==args.hero_name):
			c_rela = hero_data[i].split('|')[2].strip('\n').split(',')
			c_s = ''
			c_l = ''
			bc_s = ''
			bc_l = ''
			h_sc=0
			for k in c_rela:
				weight = 0
				for l in range(len(hero_trend)):
					if(k.split(':')[0]==hero_trend[l].split('|')[0])and(hero_data[i].split('|')[1]==hero_trend[l].split('|')[1]):
						td_=float(hero_trend[l].split('|')[2].split(',')[1])
						weight = trend_distinguish(td_)
						break
				rate = float(k.split(':')[1].strip('%'))
				if(rate>=55.0):
					c_s += k+'('+str(td_)+'%),'
					h_sc+=2*weight
				elif(rate>=52.0):
					c_l += k+'('+str(td_)+'%),'
					h_sc+=1*weight
				elif(rate<=45.0):
					bc_s += k+'('+str(td_)+'%),'
					h_sc-=2*weight
				elif(rate<=48.0):
					bc_l += k+'('+str(td_)+'%),'
					h_sc-=1*weight
			print(args.hero_name+'('+hero_data[i].split('|')[1]+')'+'的克制关系:')
			for l in range(len(hero_trend)):
				if(hero_trend[l].split('|')[0]==args.hero_name)and(hero_data[i].split('|')[1]==hero_trend[l].split('|')[1]):
					print('胜率 : '+str(hero_trend[l].split('|')[2].split(',')[0])+'%       ,登场率 : '+str(hero_trend[l].split('|')[2].split(',')[1].strip())+'% ')
					break
			print('	严重克制：'+c_s.strip(','))
			print('	轻微克制：'+c_l.strip(','))
			print('	严重被克制：'+bc_s.strip(','))
			print('	轻微被克制：'+bc_l.strip(','))
			print('	克制得分：'+str(round(h_sc,2)))
			print(' ')
if(args.statistics):
	h_sc = {}
	d_sc = {}
	if args.statistics in poslist:
		for i in range(len(hero_data)):
			if(hero_data[i].split('|')[1]==args.statistics):
				c_rela = hero_data[i].split('|')[2].strip('\n').split(',')
				h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
				d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
				for k in c_rela:
					weight = 0
					for l in range(len(hero_trend)):
						if(k.split(':')[0]==hero_trend[l].split('|')[0])and(hero_data[i].split('|')[1]==hero_trend[l].split('|')[1]):
							td_=float(hero_trend[l].split('|')[2].split(',')[1])
							weight = trend_distinguish(td_)
							break
					rate = float(k.split(':')[1].strip('%'))
					if(rate>=55.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=2*weight
					elif(rate>=52.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=1*weight
					elif(rate<=45.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2*weight
						d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2*weight
					elif(rate<=48.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1*weight
						d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1*weight
		h_sc=sorted(h_sc.items(), key=lambda item:item[1], reverse=True)
		d_sc=sorted(d_sc.items(), key=lambda item:item[1], reverse=True)
		num = 1
		print(h_sc)
		print("总计英雄中，有这些克制得分较高的英雄：")
		for it in h_sc:
			if(num<=10):
				print(str(num)+'  '+it[0]+':'+str(round(h_sc[num-1][1],2)))
				num+=1
		num=1
		print("总计英雄中，这些英雄被克制得分最高（难以被克制）:")
		for it in d_sc:
			if(num<=10):
				print(str(num)+'  '+it[0]+':'+str(round(d_sc[num-1][1],2)))
				num+=1
	elif(args.statistics=='all'):
		for i in range(len(hero_data)):
			c_rela = hero_data[i].split('|')[2].strip('\n').split(',')
			h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
			d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
			for k in c_rela:
				rate = float(k.split(':')[1].strip('%'))
				if(rate>=55.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=2*weight
				elif(rate>=52.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=1*weight
				elif(rate<=45.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2*weight
					d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2*weight
				elif(rate<=48.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1*weight
					d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1*weight
		h_sc=sorted(h_sc.items(), key=lambda item:item[1], reverse=True)
		d_sc=sorted(d_sc.items(), key=lambda item:item[1], reverse=True)
		num = 1
		print(h_sc)
		print("总计英雄中，有这些克制得分较高的英雄：")
		for it in h_sc:
			if(num<=20):
				print(str(num)+'  '+it[0]+':'+str(round(h_sc[num-1][1],2)))
				num+=1
		num=1
		print("总计英雄中，这些英雄被克制得分最高（难以被克制）:")
		for it in d_sc:
			if(num<=20):
				print(str(num)+'  '+it[0]+':'+str(round(d_sc[num-1][1],2)))
				num+=1
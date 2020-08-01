import argparse

parser = argparse.ArgumentParser(description="使用方法：")
parser.add_argument("-n","--hero_name",help="显示英雄的克制、被克制关系，分为轻微（52%%/48%%）和严重（55%%/45%%）")
parser.add_argument("-s","--statistics",help="输入位置（top,mid,jungle,bot,support）可统计不怎么被克制的英雄、克制得分较高的英雄，输入all则统计全英雄")
parser.add_argument('-i','--item',help='输入英雄名，给出装备的胜率排行，功能正在设计中')
args = parser.parse_args()
filename="hero_data.txt"
poslist = ['top','mid','jungle','bot','support']

with open(filename,'r') as f:
	hero_data = f.readlines()
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
				rate = float(k.split(':')[1].strip('%'))
				if(rate>=55.0):
					c_s += k+','
					h_sc+=2
				elif(rate>=52.0):
					c_l += k+','
					h_sc+=1
				elif(rate<=45.0):
					bc_s += k+','
					h_sc-=2
				elif(rate<=48.0):
					bc_l += k+','
					h_sc-=1
			print(args.hero_name+'('+hero_data[i].split('|')[1]+')'+'的克制关系:')
			print('	严重克制：'+c_s.strip(','))
			print('	轻微克制：'+c_l.strip(','))
			print('	严重被克制：'+bc_s.strip(','))
			print('	轻微被克制：'+bc_l.strip(','))
			print('	克制得分：'+str(h_sc))
			print(' ')
if(args.statistics):
	print('功能设计中')
	h_sc = {}
	d_sc = {}
	if args.statistics in poslist:
		for i in range(len(hero_data)):
			if(hero_data[i].split('|')[1]==args.statistics):
				c_rela = hero_data[i].split('|')[2].strip('\n').split(',')
				h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
				d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
				for k in c_rela:
					rate = float(k.split(':')[1].strip('%'))
					if(rate>=55.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=2
					elif(rate>=52.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=1
					elif(rate<=45.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2
						d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2
					elif(rate<=48.0):
						h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1
						d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1
		h_sc=sorted(h_sc.items(), key=lambda item:item[1], reverse=True)
		d_sc=sorted(d_sc.items(), key=lambda item:item[1], reverse=True)
		num = 1
		print(h_sc)
		print("总计英雄中，有这些克制得分较高的英雄：")
		for it in h_sc:
			if(num<=5):
				print(str(num)+'  '+it[0]+':'+str(h_sc[num-1][1]))
				num+=1
		num=1
		print("总计英雄中，这些英雄被克制得分最高（难以被克制）:")
		for it in d_sc:
			if(num<=5):
				print(str(num)+'  '+it[0]+':'+str(d_sc[num-1][1]))
				num+=1
	elif(args.statistics=='all'):
		for i in range(len(hero_data)):
			c_rela = hero_data[i].split('|')[2].strip('\n').split(',')
			h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
			d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]=0
			for k in c_rela:
				rate = float(k.split(':')[1].strip('%'))
				if(rate>=55.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=2
				elif(rate>=52.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]+=1
				elif(rate<=45.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2
					d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=2
				elif(rate<=48.0):
					h_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1
					d_sc[hero_data[i].split('|')[0]+'|'+hero_data[i].split('|')[1]]-=1
		h_sc=sorted(h_sc.items(), key=lambda item:item[1], reverse=True)
		d_sc=sorted(d_sc.items(), key=lambda item:item[1], reverse=True)
		num = 1
		print(h_sc)
		print("总计英雄中，有这些克制得分较高的英雄：")
		for it in h_sc:
			if(num<=5):
				print(str(num)+'  '+it[0]+':'+str(h_sc[num-1][1]))
				num+=1
		num=1
		print("总计英雄中，这些英雄被克制得分最高（难以被克制）:")
		for it in d_sc:
			if(num<=5):
				print(str(num)+'  '+it[0]+':'+str(d_sc[num-1][1]))
				num+=1
			
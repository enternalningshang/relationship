# coding:utf-8
"""
程序目的:人物关系
作者:向鹏
"""
import jieba as j
import jieba.posseg as pseg

j.load_userdict('角色.txt')#读取我规定的词典，其将这些分出来
Name = {}
names = {}
relationships = {}

with open('角色名.txt','r',encoding='UTF-8') as f:
	for line in f.readlines():
		total_name = line.split()
		for name in total_name:
			Name[name] = total_name[0]

with open('黎明破晓的街道.txt','r') as f:
	for line in f.readlines():
		line_allname = []
		words = pseg.cut(line)
		for word, flag in words:
			if flag == 'nr' and (word in Name):
				word = Name[word]
				if word not in names:
					names[word] = 0
					relationships[word] = {}
				names[word] += 1
				if word not in line_allname:
					line_allname.append(word)
		for name1 in line_allname:
			for name2 in line_allname:
				if name1!=name2:
					if name2 not in relationships[name1]:
						relationships[name1][name2] = 0
					relationships[name1][name2] += 1

with open('times.csv','w',encoding='utf-8') as f:
	f.write('Id' + ',' +'Label'+ ',' + 'Weight\n')
	for name,value in names.items():
		f.write(name + ',' + name + ',' + str(value) + '\n')
		
with open('relationships.csv','w',encoding='utf-8') as f:
	f.write('Source'+','+'Target'+','+'Weight\n')
	for name, network in relationships.items():
		for n, value in network.items():
			f.write(name + ',' + n +','+ str(value) + '\n')

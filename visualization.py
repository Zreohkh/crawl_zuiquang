import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
#解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class visual(object):
    def __init__(self,file,tx):
        self.df = pd.DataFrame(pd.read_excel(file))
        self.tx = tx
        self.tx.delete('1.0',END)

    def Msort(self,lists):
        if len(lists) <= 1:
            return lists
        middle = len(lists) // 2
        left = self.Msort(lists[:middle])
        right = self.Msort(lists[middle:])
        return self.Merge(left, right)

    def Merge(self,a, b):
        i = 0
        j = 0
        c = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            elif a[i] == b[j]:
                c.append(a[i])
                c.append(a[i])
                i += 1
                j += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return c

    def count_type_num(self):
        dict = {}
        for i in self.df['类型']:
            if '片' not in i:
                i+='片'
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1
        self.tx.insert(END,'类型及数量：\n')
        for i,j in dict.items():
            line = str(i) + str(j) +'\n'
            self.tx.insert(END,line)
        self.tx.update()
        X = list(dict.keys())
        Y = list(dict.values())
        plt.figure(figsize=(15, 8))
        plt.barh(range(len(X)), Y, color="orange")
        plt.yticks(range(len(X)), X)
        for (a, b) in zip(list(range(len(Y))),Y):
            plt.text(b + 5, a, str(b), color='r', fontsize=10)
        plt.grid(alpha=0.5)
        plt.xlabel('影片数量')
        plt.ylabel('影片类型')
        plt.title('影片类型及其数量')
        plt.savefig('./count_num_type.png',dpi=300)
        plt.show()
    def count_year_num(self):
        dict = { }
        for i in self.df['年份']:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i]+=1
        years =self.Msort(list(dict.keys()))
        nums = list(dict[year] for year in years)
        plt.figure(figsize=(15, 8))
        plt.xticks([1900+i*10 for i in range(1,20)])
        plt.xlim(1920,2030)
        plt.xlabel('发片时间')
        plt.ylabel('发片数量')
        plt.title('发片数量随发片时间变化')
        plt.plot(years,nums)
        plt.savefig('count_num_time.png',dpi=300)
        plt.show()
    def pile(self):
        # dict形式{ '年份' : { '类型' :数量 } }
        dict = {}
        # lis1形式['类型1','类型2',....]
        lis1 = []
        plt.figure(figsize=(17, 10))
        for i in range(self.df.shape[0]):
            k = self.df.iloc[i,3]
            if k not in dict.keys():
                dict[k] = {}
            s = self.df.iloc[i,2]
            if '片' not in s:
                s+='片'
            if s not in lis1:
                lis1.append(s)
            if s in dict[k].keys():
                dict[k][s]+=1
            else:
                dict[k][s]=1
        # lis2形式['年份1','年份2',....]
        lis2 = self.Msort(list(dict.keys()))[1:]
        # dict1形式{ '类型': [num1,num2,...] }
        dict1 = {}
        for i in lis1:
            lis3 = []
            for j in lis2:
                if i in dict[j].keys():
                    lis3.append(dict[j][i])
                else:
                    lis3.append(0)
            dict1[i] = lis3
        for i in dict1.keys():
            s = i
            length = len(dict1[s])
            break
        lis4 = []
        lis5 = []
        for a in dict1.keys():
            if a==s:
                lis5 = dict1[a]
            else:
                lis6 = dict1[a]
                for i in range(length):
                    lis5[i]=lis5[i]+lis6[i]
            lis4.append(lis5)
        x = np.arange(len(lis2))
        bar_with = 0.5
        plt.bar(x, dict1[s], width=bar_with,align= 'center', label = s)
        j = 0
        for i in dict1.keys():
            if j==0:
                j+=1
                continue
            plt.bar(x, dict1[i], width=bar_with, bottom=lis4[j-1],label = i)
        plt.xticks(x, lis2, rotation=90)
        plt.legend(loc= 'best')
        plt.title('各年份各类型的影片数量堆叠图')
        plt.xlabel('年份')
        plt.ylabel('数量')
        plt.savefig('type_num_time.png',dpi=500)
        plt.show()
    def main(self):
        self.count_type_num()
        self.count_year_num()
        self.pile()
        self.tx.insert(1.0, '\n已生成所有图片\n\n')




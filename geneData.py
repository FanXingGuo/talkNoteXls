import os
import datetime
import time
from datetime import date
import random

path=os.path.dirname(__file__)+"/"

with open(path+"data/"+"nameMC.txt","r",encoding="utf-8") as file:
    lines=file.readlines()

# key姓名 value专业班级
stuLists=[]
stu = {}
for line in lines:
    line=line.replace("\n","")
    if "	" in line:
        info=line.split("	")
        # stu["name"]=info[0]
        # stu["mjcl"]=info[1]
        stu[info[0]]=info[1]
        # stuLists.append(stu)
    elif "	" in line:
        info = line.split("	")
        # stu["name"] = info[0]
        # stu["mjcl"] = info[1]
        # stuLists.append(stu)
        stu[info[0]] = info[1]
    else:
        print("未正确读取行",line)

stuSet=set()
stuSetA=set()
for key in stu:
    stuSet.add(key)
    stuSetA.add(key)
    stuLists.append(key)

print("共计学生（名）：",len(stuSet))


#跳过学生名单

# 节假日
brDay=["4.5","4.6","5.1","5.2","5.3","5.4","6.7"]
def ShowDate(d):
    month=str(int(d.month))
    day=str(int(d.day))
    return month+"."+day
# 日期
sd1=datetime.datetime(2019,4,1) # 开始日期
endDay="7.1" #结束日期

# 产生工作日 日期数组
dayList=[]
while True:
    s=ShowDate(sd1)
    if s!="7.1":
        if sd1.isoweekday()<5 and s not in brDay:
            dayList.append(s)
        sd1=sd1+datetime.timedelta(days=1)
        s=ShowDate(sd1)
    else:
        break

# print(len(dayList))

# 内容 列表
with open(path+"data/"+"tConts.txt","r",encoding="utf-8") as file:
    tC_lines=[i.replace("p","\n") for i in file.readlines()]

tcL={}
for line in tC_lines:
    if line[0] in tcL:
        tcL[line[0]].append(line[1:])
    else:
        tcL[line[0]] =[line[1:]]


# 结果 列表
with open(path+"data/"+"tResults.txt","r",encoding="utf-8") as file:
    tR_lines=[i.replace("\n","") for i in file.readlines()]

tresuL={}
for line in tR_lines:
    if line[0] in tresuL:
        tresuL[line[0]].append(line[1:])
    else:
        tresuL[line[0]]=[line[1:]]

# 学生列表
with open(path+"data/"+"tReasons.txt","r",encoding="utf-8") as file:
    tReson=file.readlines()
dataCont={}
dataReas={}
for line in tReson:
    if not line.startswith("#"):
        if line[0].isalpha():
            alpha=line[0]
            line=line.replace(alpha,"").replace("\n","")
            # print(alpha)
            if ":" in line:
                reeason=line.split(":")[0]
                lists = [i.replace("\n","") for i in line.split(":")[1].split(" ")]
            else:
                lists=None
                reeason=line
                # print(lists)
            if alpha!="Z":
                dataReas[alpha] = reeason

            # 先处理特殊情况
            if "$" in line:
                nl=line.split("$")
                dataReas[alpha] =nl[0]
                par=nl[1]
                if "r" in par:
                    c=par[0]
                    num=par.replace(c,"")
                    lists1=random.sample(lists,int(num))
                    dataCont[alpha]=stuSet&set(lists1)
                    stuSet -= set(lists1)
                    continue

            # 一般情况
            if lists!=None and alpha!="Z":
                dataCont[alpha]=set(lists)&stuSet
                stuSet-=set(lists)
            if alpha=="Z":
                print("跳过学生（名）",len(lists))
                stuSet-=set(lists)
                z_set=set(lists)

# 剩余
dataCont["last"]=stuSet
print(dataReas)

# print(z_set)
# print(stuSetA)
bL=set(random.sample(dataCont["last"],20))
dataCont["B"]=bL
dataCont["last"]-=bL
dataCont["G"]=dataCont["last"]

allset=set()
for key in dataCont:
    allset.update(dataCont[key])
    # print(key,len(dataCont[key]))

if len(stuSetA)==len(z_set)+len(allset):
    print("人数校验成功","共计学生（名）",len(stuSetA),"。其中收录学生（名）:",len(allset),"，跳过学生（名）：",len(z_set))
else:
    print("缺少学生:",stuSetA-allset-z_set)

dataCont.pop("last")




















from stru.day03.mkFile import MF
from stru.day03.geneData import dataCont,tcL,tresuL,dayList,dataReas,stu
import random

mk=MF()
par={"SN":"张三","name":"张三","mjcl":"软工二班","tdate":"2019年07月02日","place":"寝室","stype":"",
         "tReason":"了解学生生活状况",
         "tCont":"""学生近期没有旷课情况，上课认真听讲，积极\n配合老师完成教学工作，及时完成并上交作业，\n课余时间喜欢画画、唱歌。希望学生能继续保持\n良好的学习习惯、和生活作风。""",
         "tResult":"学生表示会继续保持，努力学习"
    }

for key in dataCont:
    par["tReason"] = dataReas[key]
    stuL=dataCont[key]
    for student in stuL:
        par["name"] = student
        par["mjcl"] = stu[student]
        par["SN"] = student
        par["tdate"] = random.choice(dayList)
        par["place"] = random.choice(["寝室","办公室"])
        par["stype"] = ""
        par["tResult"]=random.choice(tresuL[key])
        par["tCont"]=random.choice(tcL[key])
        mk.addSheet(par)
mk.save()
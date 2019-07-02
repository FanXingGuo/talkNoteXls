import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

class MF():
    def __init__(self):
        self.alignment = xlwt.Alignment() # Create Alignment
        self.alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        self.alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
        self.alignment.wrap = 1
        self.title="谈心谈话记录表"
        self.f = xlwt.Workbook()

    def getTS(self):
        # 表头样式
        titleSty = xlwt.XFStyle()
        fnt = xlwt.Font()
        fnt.name = u"宋体"
        fnt.bold = True
        fnt.height = 20 * 24

        titleSty.font = fnt
        titleSty.alignment = self.alignment
        return titleSty

    def getBS(self):
        # 表体样式
        bodySty = xlwt.XFStyle()

        fnt1 = xlwt.Font()
        fnt1.name = u"宋体"
        fnt1.height = 20 * 12

        borders = xlwt.Borders()
        borders.left = 2
        borders.right = 2
        borders.top = 2
        borders.bottom = 2

        bodySty.font = fnt1
        bodySty.borders = borders
        bodySty.alignment = self.alignment

        return bodySty

    def addSheet(self,par):
        """

        :param par: {SN:sheetName,name,mjcl,tdate,place,stype,tReason,tCont,tResult}
        :return:
        """
        sheet=self.f.add_sheet(par["SN"],cell_overwrite_ok=True)
        name = par["name"]  #"张三";
        mjcl = par["mjcl"]  # "软件工程";
        tdate = par["tdate"]#"2019-01-11";
        place = par["place"]#"寝室";
        stype = par["stype"]#;
        tReason =par["tReason"]# "了解学生生活状况"
        tCont = par["tCont"]#"""学生近期没有旷课情况，上课认真听讲，积极\n配合老师完成教学工作，及时完成并上交作业，\n课余时间喜欢画画、唱歌。希望学生能继续保持\n良好的学习习惯、和生活作风。"""
        tResult = par["tResult"] #"学生表示会继续保持，努力学习"
        # 设置行高列宽
        for i in range(10):
            sheet.col(i).width = int(13.5 * 256 + 182)
        sheet.row(0).height_mismatch = True  # 必须设置高度才能生效
        sheet.row(1).height_mismatch = True  # 必须设置高度才能生效
        sheet.row(2).height_mismatch = True  # 必须设置高度才能生效
        sheet.row(3).height_mismatch = True  # 必须设置高度才能生效
        sheet.row(4).height_mismatch = True  # 必须设置高度才能生效
        sheet.row(0).height = int(36 * 20)
        sheet.row(1).height = int(36 * 20)
        sheet.row(2).height = int(36 * 20)
        sheet.row(3).height = int(249 * 20)
        sheet.row(4).height = int(66 * 20)

        sheet.write_merge(0, 0, 0, 9, self.title, style=self.getTS())
        r2 = ["学生姓名", name, "专业班级", mjcl, "谈话时间", tdate, "谈话地点", place, "学生类型", stype]
        for index, i in enumerate(r2):
            sheet.write(1, index, i, style=self.getBS())

        sheet.write(2, 0, "谈话事由", style=self.getBS())
        sheet.write_merge(2, 2, 1, 9, tReason, style=self.getBS())
        sheet.write(3, 0, "谈话内容", style=self.getBS())
        sheet.write_merge(3, 3, 1, 9, tCont, style=self.getBS())

        sheet.write(4, 0, "谈话效果", style=self.getBS())
        sheet.write_merge(4, 4, 1, 9, tResult, style=self.getBS())

    def save(self):
        self.f.save("data.xls")

if __name__ == '__main__':
    mk=MF()
    # {SN:sheetName,name,mjcl,tdate,place,stype,tReason,tCont,tResult}
    par={"SN":"张三","name":"张三","mjcl":"软工二班","tdate":"2019年07月02日","place":"寝室","stype":"",
         "tReason":"了解学生生活状况",
         "tCont":"""学生近期没有旷课情况，上课认真听讲，积极\n配合老师完成教学工作，及时完成并上交作业，\n课余时间喜欢画画、唱歌。希望学生能继续保持\n良好的学习习惯、和生活作风。""",
         "tResult":"学生表示会继续保持，努力学习"
    }

    mk.addSheet(par)
    par["SN"]="a"
    mk.addSheet(par)
    par["SN"]="b"
    mk.addSheet(par)
    mk.save()
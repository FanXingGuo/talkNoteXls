import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

title="谈心谈话记录表"

f = xlwt.Workbook()
sheet1 = f.add_sheet('a',cell_overwrite_ok=True)


for i in range(10):
    sheet1.col(i).width = int(13.5 * 256 + 182)
sheet1.row(0).height_mismatch = True  #必须设置高度才能生效
sheet1.row(1).height_mismatch = True  #必须设置高度才能生效
sheet1.row(0).height = int(27.95 * 20)
sheet1.row(1).height = int(27.95 * 20)

def getTS():
    #定义样式
    style = xlwt.XFStyle()

    #字体
    fnt = xlwt.Font()
    fnt.name=u"宋体"
    fnt.bold = True
    fnt.height=20*24
    #水平居中
    alignment = xlwt.Alignment() # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style.font=fnt
    style.alignment=alignment
    # style.borders=borders
    return style
def getBS():
    style1=xlwt.XFStyle()
    fnt1=xlwt.Font()
    fnt1.name=u"宋体"
    fnt1.height=20*12

    borders = xlwt.Borders()
    borders.left = 2
    borders.right = 2
    borders.top = 2
    borders.bottom = 2
    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style1.font=fnt1
    style1.borders=borders
    style1.alignment=alignment
    return style1




sheet1.write_merge(0,0,0,9,title,style=getTS())
sheet1.write(1,0,"学生姓名",style=getBS())



f.save("1.xls")

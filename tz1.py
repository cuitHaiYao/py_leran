import xlrd
import re
def exceltest2():
    data = xlrd.open_workbook("台账.xlsx", encoding_override='utf-8')
    table = data.sheets()[0] #文件中的第一张表
    nr = table.nrows
    nc = table.ncols
    with open('demo6.xls', 'w', encoding='utf-8') as obj_w:
        for i in range(1,nr):
            alldata = table.row_values(i)
            obj_w.write(str(alldata[0]) + '\t' + str(alldata[1])+'\t')
            if '塔吊' in str(alldata[2]):
                obj_w.write('1'+'\t')
            else:
                obj_w.write('0' + '\t')
            if '扬尘' in str(alldata[2]):
                obj_w.write('1'+'\t')
            else:
                obj_w.write('0' + '\t')
            if '人脸' or '实名制' in str(alldata[2]):
                obj_w.write('1'+'\t')
            else:
                obj_w.write('0' + '\t')
            if '运渣车' in str(alldata[2]):
                obj_w.write('1'+'\t')
            else:
                obj_w.write('0' + '\t')
            if '视频' in str(alldata[2]):
                obj_w.write('1'+'\t')
            else:
                obj_w.write('0' + '\t')
            obj_w.write(str(alldata[3]) + '\t' + str(alldata[4])+'\t'+str(alldata[5]) + '\t' + str(alldata[6])+'\t')
            obj_w.write('\n')


if __name__ == '__main__':
    exceltest2()


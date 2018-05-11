import os
import collections
import xlrd

from db_models import *

def get_data(filename,headline=True):
     #既可以打开xls类型的文件，也可以打开xlsx类型的文件
    start = 1 if headline else 0
    datas = []
    w = xlrd.open_workbook(filename)
    ws = w.sheets()[0]
    nrows = ws.nrows
    for i in range(start,nrows):
        data = ws.row_values(i)
        datas.append(data)
    return datas


@db_session
def check_file(filename):
    datas = get_data(filename)
    infos = []
    for index,data in enumerate(datas):
        info = ''
        signid = data[1]
        name = data[2]
        if not exists(s for s in StudPh if s.signid==signid and s.name==name):
            info = '第{}行数据，考号或姓名{},{}不正确；'.format(index+1,signid,name)
        levels = [data.strip() for data in data[3:]]
        if not all(lvl in ('A','B','C') for lvl in levels):
            info += '第{}行数据，{},{}包含不正确的等级{}.'.format(index+1,signid,name,','.join(levels))
        c = collections.Counter(levels)
        if c['A'] < 1 or c['C'] >2:
            info += '第{}行数据，{},{}等级不符合示范高中录取{}.'.format(index+1,signid,name,','.join(levels))
        if info:
            infos.append(info)

def get_files(directory):
    files = []
    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.xls') or f.endswith('.xlsx')]
    files = [os.path.join(directory,f) for f in files]
    return files

def check_files(path='.'):
    files = get_files(path)
    for file in files:
        print('check file:',file,'...')
        infos = check_file(file)
        if infos:
            for info in infos:
                print(info)

if __name__ == '__main__':
    check_files()

from pony.orm import *

DB_PARAMS = {
    'provider':'postgres',
    'user':'postgres',
    'password':'123456',
    'host':'localhost',
    'database':'ph18'
}

db = Database()

# 体育成绩总表
class  StudPh(db.Entity):
    signid = Required(str)
    phid = Optional(str,nullable = True)
    cardid = Optional(str,nullable = True)
    name = Required(str)
    sex = Required(str)
    idcode = Required(str)
    sch = Required(str)
    schcode = Required(str)
    exam_addr = Optional(str,nullable = True)
    exam_date = Optional(str,nullable = True)
    classcode = Optional(str,nullable = True)
    
    # 用于乱序 2018年使用
    sturand = Optional(float,nullable = True)

    # 2019 年启动字段hashlib_sha3_512 乱序，
    # 以达到稳定排号（只要考试编排exam_prog_set.py
    # 不变，每次运行生成准考证号相同）
    # sturand = Optional(str,nullable=True)

    # 免考标志
    free_flag = Optional(bool,nullable = True)
    # 选项
    jump_option = Optional(int,nullable = True)
    rope_option = Optional(int,nullable = True)
    globe_option = Optional(int,nullable = True)
    bend_option = Optional(int,nullable = True)

    # # 测试数据
    jump_data = Optional(str,nullable=True)
    rope_data = Optional(str,nullable=True)
    globe_data = Optional(str,nullable=True)    # cm
    bend_data = Optional(str,nullable=True)     # mm
    run8_data = Optional(str,nullable=True)
    run10_data = Optional(str,nullable=True)
    # 测试分数
    jump_score = Optional(int,nullable=True)
    rope_score = Optional(int,nullable=True)
    globe_score = Optional(int,nullable=True)
    bend_score = Optional(int,nullable=True)
    run8_score = Optional(int,nullable=True)
    run10_score = Optional(int,nullable=True)

    total_score = Optional(int,nullable = True)

    freetype = Optional(int,default=0,nullable = True)
    memo = Optional(str,nullable = True)

db.bind(**DB_PARAMS)
db.generate_mapping(create_tables=True)

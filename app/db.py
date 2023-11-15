from sqlalchemy import (TIMESTAMP, Column, Date, Index, Integer, String,
                        create_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# 创建 MySQL 数据库连接
engine = create_engine('mysql+pymysql://root:a1234567@127.0.0.1/hotel')


class PersonalInfo(Base):
    __tablename__ = 'personal_info'
    __table_args__ = (
        Index('uix_name_card_no', 'name', 'card_no', unique=True),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), comment='姓名')
    card_no = Column(String(255), comment='身份证号')
    descriot = Column(String(255))
    ctf_tp = Column(String(255))
    ctf_id = Column(String(255))
    gender = Column(String(1), comment='性别')
    birthday = Column(Date, comment='生日')
    address = Column(String(255), comment='住址')
    zip = Column(String(20))
    dirty = Column(String(1))
    district1 = Column(String(255))
    district2 = Column(String(255))
    district3 = Column(String(255))
    district4 = Column(String(255))
    district5 = Column(String(255))
    district6 = Column(String(255))
    first_nm = Column(String(255))
    last_nm = Column(String(255))
    duty = Column(String(255))
    mobile = Column(String(20), comment='手机')
    tel = Column(String(20), comment='电话')
    fax = Column(String(20))
    email = Column(String(255), comment='邮箱')
    nation = Column(String(255), comment='民族')
    taste = Column(String(255))
    education = Column(String(255), comment='学历')
    company = Column(String(255), comment='公司')
    c_tel = Column(String(20))
    c_address = Column(String(255))
    c_zip = Column(String(20))
    family = Column(String(255))
    version = Column(Integer)
    created_at = Column(TIMESTAMP, comment='插入时间', server_default=func.now())
    updated_at = Column(TIMESTAMP, comment='更新时间', nullable=False, server_default=func.now(), onupdate=func.now())  # noqa:E501

    def __repr__(self):
        return f"<PersonalInfo(name='{self.name}', card_no='{self.card_no}', birthday='{self.birthday}')>"  # noqa:E501


# 创建数据库表
Base.metadata.create_all(engine)

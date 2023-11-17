# alembic 使用文档

Generic single-database configuration.


安装alembic

```bash
pip install alembic
```

创建迁移环境

```bash
alembic init alembic
```

配置迁移环境

1. 在`alembic.ini`更改`sqlalchemy.url`配置项，
```ini
sqlalchemy.url = mysql+pymysql://root:a1234567@127.0.0.1/hotel
```

2. 配置`sqlalchemy`模型

3. 修改`env.py`

创建基础空迁移

```bash
alembic revision -m "Empty Init" 
```

升级数据库(迁移)

```bash
alembic upgrade head
```

自动生成迁移

```bash
alembic revision --autogenerate -m "Add Comments"
```

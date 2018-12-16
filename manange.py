import os
from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == "__main__":
    app.run(debug=True)

# 設定APP
# export FLASK_APP=manange.py

# 建資料庫
# flask shell
#from manange import db
# db.create_all()

# 查資料
#from manange import 物件
# 物件.query.all()
# db.session.commit()

#建權限
# from manange import *
# Role.insert_roles()
# admin=Role.query.filter_by(name='Administrator').first()
# for u in User.query.all()
# u.role=admin
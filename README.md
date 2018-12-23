# flask-demo

## 介紹

1071 逢甲軟體工程課程專題專案

## Quickstart

+ 創建虛擬環境(python3)
    + `pyvenv venv`
+ 啟動虛擬環境
    + `source venv/bin/activate`
+ Install dependencies
    + `pip install -r requirements.txt`
+ Configuration
    + `export FLASK_APP=manange.py`
    + `export FLASK_ADMIN=your_admin_email`
    + `flask shell`
    + `from manange import *`
    + `db.create_all()`
    + `Role.insert_roles()`
    + Visit [localhost:5000](http://localhost:5000)
    + 註冊您的管理員帳號(email需跟FLASK_ADMIN的一樣)，然後回到shell
    + `flask shell`
    + `from manange import *`
    + `admin=Role.query.filter_by(name='Administrator').first()`
    + `for u in User.query.all(): u.role=admin`
    + `db.session.commit()`

## 特色

+ 使用者註冊後能夠發文及 Follow 其他使用者
+ 文章頁面分為兩大部分
    + ALL : 能看到所有的文章，一頁最多顯示 5 篇(依照分文順序排列)
    + Follow : 能看到使用者 Follow 的其他使用者的文章，一頁最多顯示 5 篇(依照分文順序排列)
+ 使用者能修改自己的資訊(除 Username 外)方便其他使用者認識您
    + 修改 E-mail 尚未完成
+ 管理員能夠修改已註冊人員的任何資訊

## 技術細節

+ 使用 Ubuntu 16.04 開發
+ [Flask](https://github.com/pallets/flask) 為開發框架
    + 登入使用 [Flask-Login](https://github.com/maxcountryman/flask-login)
    + 資料庫使用 [SQLite](https://www.sqlite.org/index.html) 加上 [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)
    + 表單驗證使用 [Flask-WTF](https://github.com/lepture/flask-wtf)
+ 網頁使用 [Bootstrap4](https://getbootstrap.com/) 排版及美化

## TODO

+ 使用者修改  E-mail 功能
+ 完善各頁面的 flash 功能
# learn-flask

> 2019-08-27

learn flask for joy


## 如何运行

python enter.py即可



## 后期扩展

可能会教授api，以及网站相关内容


## 如何学习

flask官方文档，李辉以及狗书

## 文档结构

enter.py主文件

## 如何调试运行


win系统下

`set FLASK_APP=manage.py`

mac系统或linux下

`export FLASK_APP=manage.py`


首先运行`flask shell`，进入python终端

```python
from app import db
from app.models import Post, User

p1 = Post()
db.seesion.add(p1)
```


## 设定debug

FLASK_DEBUG = 1

不再支持app.run(debug=True)

## 初始化数据库

flask db init

flask db migrate

flask db upgrade

## 关于form的一点感想

form我之前的理解是用来验证post传来的数据，其实，他是为了在页面中渲染数据，然后，点击提交就可以获得用户

只有这样才能有效发挥表单的作用，而token，则是通过另一种方式获得

之所以支持`POST`和`GET`两种请求方式，是指第一次请求，一般是get，当提交表单时，触发的是post操作

所以，我们设计api时，不必考虑这种情况，一个资源的请求方式一定要分开来写。
#encoding:utf-8
from flask import Flask,config,url_for,redirect
#渲染html页面是需要用到的模块，html界面放在templates目录下
from flask import render_template

#导入配置文件
import config

app = Flask(__name__)
#使用第二种方法开启debug模式
app.config.from_object(config)



@app.route('/')
def hello_world():
    return 'Hello World!-Young'

#url传参,将参数用<>包围
@app.route('/demo1/<id>')
def demo1(id):
    return u"您传入的参数是：%s" %id

#URL反转：通过视图函数获取url地址,需要引入url_for
@app.route('/demo2/')
def demo2():
    # return url_for('hello_world')
    return url_for('demo1',id='chenyang')

#利用URL反转实现重定向和页面跳转,需要引入redirect
@app.route('/demo3/')
def demo3():
    #直接使用url地址方式
    # return redirect('/demo2/')
    #利用url反转
    return redirect(url_for('demo1',id='11111111'))

#渲染与传参1
@app.route('/index/')
def index():
    #调用index.html时用到了extends继承base.html页面和block
    return render_template('index.html',location=u'这个是首页面')
    # 如果参数很多时，将所有参数写入一个字典中，然后传入**dict,如下：
    # items = {
    #     'name':'Young',
    #     'age':29
    # }
    # return render_template('index.html',**items)


#渲染与传参2
@app.route('/news/')
def news():
    booklist = [
        {
            'name':u'西游记',
            'auditor':u'吴承恩',
            'price':109
        },
        {
            'name': u'红楼梦',
            'auditor': u'曹雪芹',
            'price': 108
        },
        {
            'name': u'三国演义',
            'auditor': u'罗贯中',
            'price': 104
        },
        {
            'name': u'水浒传',
            'auditor': u'施耐庵',
            'price': 100
        }

    ]
    #将整个列表作为参数传给html页面，调用news.html时用到了extends继承base.html页面和block
    return render_template('news.html',booklist=booklist)








if __name__ == '__main__':
    #开启DEBUG1：直接在run()中添加"debug=True"开启debug模式，就不用反复重启了
    # app.run(debug=True)
    #开启DEBUG2:使用config.py文件的方式，建议！
    app.run()



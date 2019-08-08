from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) # post는 비밀, get방식은 기록에 남음(근데 큰 데이터 집어넣는데 문제가 생긴다.)
def mainB():
    # import seaborn as sns  # seaborn

    print(request.path) # 현재활설화된 path를 알려준다.
    return render_template('index.html')

@app.route('/map/') # post는 비밀, get방식은 기록에 남음(근데 큰 데이터 집어넣는데 문제가 생긴다.)
def map():
    return render_template('1st.html')

@app.route('/data/') # post는 비밀, get방식은 기록에 남음(근데 큰 데이터 집어넣는데 문제가 생긴다.)
def data():
    return render_template('2nd.html')

@app.route('/', methods=['GET','POST']) # post는 비밀, get방식은 기록에 남음(근데 큰 데이터 집어넣는데 문제가 생긴다.)
def index():
    return render_template('index.html')
# jinja -> base (Extend) , -> 따라서 한명은 뼈대, 메뉴 , 등등을 만듦 .

if __name__ == '__main__':
    app.run()

    # if 'Macintosh' in request.headers['User-Agent']:
    #     print('Request from Mac OS')

    # print(request.method) # url들어갈 때마다 get 방식 -> 민감한 정보아니면 get방식
    # print(request.form) # request.form -> dictionary (immutable)
    # return 'Hello World!'
    # print(url_for('hello_world')) # 함수인지를 키면 어떤 애인지 알려준는 것
from flask import Flask, request
import os
from Answer.ChatGptAnswer import *
import json

app = Flask(__name__)

appkey = os.getenv('appkey')
token = os.getenv('token')
PORT = int(os.getenv('PORT'))
models=['gpt-3.5-turbo']
print(appkey)
print(token)
print(PORT)

error_response = {'code': -1, 'msg': '数据错误'}

@app.route('/api', methods=['GET','POST'])
def api():
    raw_data = request.get_data()
    print(raw_data)
    data = json.loads(raw_data)
    tk=data['tk']
    message=data['message']
    model=data['model']
    data={}
    if tk==token and model in models:
        chat = ChatGptAnswer(model,appkey)
        content = chat.ask_gpt(message)
        data['conent']=content
        data['code'] = '200'
        return json.dumps(data)
    else:
        return json.dumps(error_response)


if __name__ == '__main__':
    # 默认开启 debug 模式，生产环境请设置成 False
    app.run(host="0.0.0.0", port=PORT, debug=True)

from cgitb import reset
from flask import Flask, jsonify, request
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/getrank/<name>', methods=['GET'])
def getCountbyMonth(name):

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()

    sqlcomm = "select * from students where name='" + name + "'"
    sqlcomm = "select * from students"
    print(sqlcomm)
    # return "sqlcomm from getrank"
    cur.execute(sqlcomm)

    # cur.commit()
    # conn.close()
    data = cur.fetchall()
    # print(len(data))
    conn.close()
    jsonData = []
    
    for row in data:
        result = {}
        result['name'] = row[0]
        result['class'] = row[1]
        result['school'] = row[2]
        result['count'] = row[3]
        jsonData.append(result)
    
    # print(jsonData)
    # jsondatar = json.dumps(jsonData, ensure_ascii=False)
    # print(jsondatar)
    # print(jsondatar[1:len(jsondatar) - 1])

    resultdic = {}
    resultdic["code"] = '200'
    resultdic["message"] = "successful"
    resultdic["total"] = str(len(jsonData))
    resultdic["data"] =  jsonData
        # 去除首尾的中括号
        # return jsondatar[1:len(jsondatar) - 1]

    # # for row in cursor.fetchall():
    # #     print(row)

    # result_dict = {
    #     'code': '200',
    #     'code_msg': 'successful',
    #     'data': jsondatar[1:len(jsondatar) - 1]
    #     }
     #jsonify中保存着结果图片的base编码，拿下来客户端解码即可得到结果图片

    return jsonify(resultdic)
    # return jsonify(json.dumps(resultdic,ensure_ascii=False))

from flask import jsonify

@app.route('/demo')
def demo():
    json_dict = {
        "user_id": 1,
        "user_name": "张三"
    }
    return jsonify(json_dict)

if __name__ == "__main__":
     app.run()
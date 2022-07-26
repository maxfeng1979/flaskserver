# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import sqlite3
import json
from flask import jsonify
import base64
import sys


app = Flask(__name__)

#DB operation
def getDatafromDB(sqlcommand):
    
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute(sqlcommand)

    data = cur.fetchall()
    conn.close()
    datalist = []
    
    for row in data:
        result = {}
        result['name'] = row[0]
        result['class'] = row[1]
        result['school'] = row[2]
        result['count'] = row[3]
        datalist.append(result)

    return datalist

def image_to_base64(full_path):
    with open(full_path, "rb") as f:
        data = f.read()
        image_base64_enc = base64.b64encode(data)
        image_base64_enc = str(image_base64_enc, 'utf-8')
    return image_base64_enc


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/testPost",methods=['POST'])
def testPost():
    param1 = request.form['name']
    param2 = request.form['school']
    if request.method == 'POST':
        thefile = request.data
        with open("client-src.jpg","wb") as f:
            f.write(thefile)

    return "Hello Post!" + param1 + "  " + param2

@app.route("/testPostData",methods=['POST'])
def testPostData():   
    if request.method == 'POST':
        thefile = request.files["file1"] #这个request.files["file1"] 是flask的临时文件缓存。
        # print(type(thefile["file1"]))
        # print(len(thefile))
        # print(sys.getsizeof(thefile["file1"]))
        # print(len(request.form))
        # print(request.form['name'])
        # with open("client-src.jpg","wb") as f:
        #     f.write(thefile)
        
        #
        thefile.save("client-src.jpg") #可以直接保存诚文件，或用thefile.read()读出二进制流

    return "Hello PostData!" + request.form['name']

@app.route('/getAnUser/<name>', methods=['GET'])
def getAnUser(name):

    sqlcomm = "select * from students where name='" + name + "'"
    jsonData = getDatafromDB(sqlcomm)
   
    resultdic = {}
    resultdic["code"] = '200'
    resultdic["message"] = "successful"
    resultdic["total"] = str(len(jsonData))
    resultdic["data"] =  jsonData     

    return jsonify(resultdic)
    # conn = sqlite3.connect('student.db')
    # cur = conn.cursor()

    # sqlcomm = "select * from students where name='" + name + "'"
    # sqlcomm = "select * from students"
    # print(sqlcomm)
    # # return "sqlcomm from getrank"
    # cur.execute(sqlcomm)

    # # cur.commit()
    # # conn.close()
    # data = cur.fetchall()
    # # print(len(data))
    # conn.close()
    # jsonData = []
    
    # for row in data:
    #     result = {}
    #     result['name'] = row[0]
    #     result['class'] = row[1]
    #     result['school'] = row[2]
    #     result['count'] = row[3]
    #     jsonData.append(result)
    
    # # print(jsonData)
    # # jsondatar = json.dumps(jsonData, ensure_ascii=False)
    # # print(jsondatar)
    # # print(jsondatar[1:len(jsondatar) - 1])

    # resultdic = {}
    # resultdic["code"] = '200'
    # resultdic["message"] = "successful"
    # resultdic["total"] = str(len(jsonData))
    # resultdic["data"] =  jsonData
    #     # 去除首尾的中括号
    #     # return jsondatar[1:len(jsondatar) - 1]

    # # # for row in cursor.fetchall():
    # # #     print(row)

    # # result_dict = {
    # #     'code': '200',
    # #     'code_msg': 'successful',
    # #     'data': jsondatar[1:len(jsondatar) - 1]
    # #     }
    #  #jsonify中保存着结果图片的base编码，拿下来客户端解码即可得到结果图片

    # return jsonify(resultdic)
    # # return jsonify(json.dumps(resultdic,ensure_ascii=False))

@app.route('/getUsers', methods=['GET'])
def getUsers():
    
    sqlcomm = "select * from students"
    jsonData = getDatafromDB(sqlcomm)
   
    resultdic = {}
    resultdic["code"] = '200'
    resultdic["message"] = "successful"
    resultdic["total"] = str(len(jsonData))
    resultdic["data"] =  jsonData     

    return jsonify(resultdic)

@app.route('/demo')
def demo():
    json_dict = {
        "user_id": 1,
        "user_name": "张三"
    }
    return jsonify(json_dict)

@app.route('/predict', methods=['POST'])
def predict():

    thefile = request.files["file1"] #这个request.files["file1"] 是flask的临时文件缓存。
        # print(type(thefile["file1"]))
        # print(len(thefile))
        # print(sys.getsizeof(thefile["file1"]))
        # print(len(request.form))
        # print(request.form['name'])
        # with open("client-src.jpg","wb") as f:
        #     f.write(thefile)
        
        #
    thefile.save("client-src.jpg") #可以直接保存诚文件，或用thefile.read()读出二进制流
    res_cnt = 5
    result_dict = {
            'code': '200',
            'code_msg': 'successful',
            'detect_res': "Mock apicture",
            'detect_number':res_cnt
            }
    
    return jsonify(result_dict)



    # if request.method == 'POST':
    #     file = request.data
    #     with open("client-src.jpg","wb") as f:
    #         f.write(file)
	   
    #     # #调用检测函数 
    #     # res_image, res_cnt = detect("client-src.jpg")
    #     # json_res = image_to_base64("./server_resrbg.jpg")

    #     # result_dict = {
    #     #     'code': '200',
    #     #     'code_msg': 'successful',
    #     #     'detect_res': json_res,
    #     #     'detect_number':res_cnt
    #     #     }

    #     # json_res = image_to_base64("./server_resrbg.jpg")
    #     res_cnt = 5

    #     #更新数据库
    #     sqlcomm = "update * from students where name='" + name + "'"
    #     jsonData = getDatafromDB(sqlcomm)
    
    #     resultdic = {}
    #     resultdic["code"] = '200'
    #     resultdic["message"] = "successful"
    #     resultdic["total"] = str(len(jsonData))
    #     resultdic["data"] =  jsonData     


    #     result_dict = {
    #         'code': '200',
    #         'code_msg': 'successful',
    #         'detect_res': "apicture",
    #         'detect_number':res_cnt
    #         }

    # #jsonify中保存着结果图片的base编码，拿下来客户端解码即可得到结果图片
    # return jsonify(result_dict)


@app.route('/gettotal/<schoolname>', methods=['Get'])
def getTotal(schoolname):
    
    # schoolname = request.args.get('school')

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    sqlcomm = "select school, sum(bottolcount) as total from students group by school having school='"+ schoolname +"'"
    cur.execute(sqlcomm)

    data = cur.fetchall()
    conn.close()

    datalist = []
    
    for row in data:
        result = {}
        result['school'] = row[0]
        result['count'] = row[1]
        datalist.append(result)
   
    resultdic = {}
    resultdic["code"] = '200'
    resultdic["message"] = "successful"
    resultdic["total"] = str(len(datalist))
    resultdic["data"] =  datalist  

    return jsonify(resultdic) 

if __name__ == "__main__":
     app.run(debug=True)
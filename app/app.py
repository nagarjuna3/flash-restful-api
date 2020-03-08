from flask import Flask, render_template, request
import mysql.connector
import json
import random
import string
import time

app = Flask(__name__,template_folder='template')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_transaction_uuid(uuid):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'headers'
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    print (uuid)
    cursor.execute("""SELECT uuid, body FROM uuid WHERE uuid LIKE '%s' ORDER BY id DESC LIMIT 1""" % (uuid))
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return rows

def post_uuid(id, body, created):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'headers'
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    results=cursor.execute("INSERT INTO uuid(uuid, body, created) values(%s, %s, %s)", (id, body, created))
    #rows = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    # return results
    return 'Successfully posted the body for this POST request'

@app.route('/svc/')
def gen_uuid():
    new_uuid = id_generator()
    print (new_uuid)
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    body = ""
    post_uuid(new_uuid, body, date)

    return render_template("public/dynamic.html", uuid=new_uuid)

@app.route("/svc/<guid>", methods=['GET','POST'])
def profile(guid):
    if request.method == 'GET':
        return json.dumps({'uuid': get_transaction_uuid(guid)})
    if request.method == 'POST':
        check_uuid = get_transaction_uuid(guid)
        if check_uuid:
            req_data = request.get_json()
            date= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            str_obj = json.dumps(req_data)
            results = post_uuid(guid, str_obj, date)                    
        else:
            results = "No UUID found"
        return (results, 200, None)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
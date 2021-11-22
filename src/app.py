from flask import Flask, jsonify
import time
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def host_basic_information():
    hour=time.strftime('%H:%M:%S', time.localtime())
    date=time.strftime('%Y-%m-%d', time.localtime())
    timezone=time.strftime('%z', time.localtime())
    hostname = socket.gethostname()
    ip=socket.gethostbyname(hostname)
    data = {'Hour': hour,
            'Date':date,
            'Timezone':timezone,
            'Hostname':hostname,
            'IP':ip}
    
    return jsonify(data), 200

if __name__=='__main__':
    app.run(host="0.0.0.1", port=4000, debug=True)

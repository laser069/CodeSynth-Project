from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/data',methods=['POST','GET'])
def post_data():
    input_data = request.get_json()
    response = {
        'received_data': input_data,
        'status':"Sucess",
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, make_response, jsonify, request, abort
#from pymongo import MongoClient
#source = 'mongodb+srv://mccndcg:ePRZiwIV5x3uU66Q@cluster0.spy9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#client = MongoClient(source)
#db = client.testdb
#collection = db.testcoll

app = Flask(__name__, template_folder='./')

@app.route('/jajas')
def jajas():
    return make_response("i love you")

@app.route('/complete')
def complete():
    return render_template('indexcomplete.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()

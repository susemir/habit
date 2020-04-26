from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhabit

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def make_record():		# 클라이언트로부터 데이터를 받는 부분
    name_receive = request.form['name_give']
    color_receive = request.form['color_give']
    date_receive = request.form['date_give']

		# mongoDB에 넣는 부분
    habit = {'name': name_receive, 'color': color_receive, 'date': date_receive }

    db.habits.insert_one(habit)

    return jsonify({'result': 'success'})

@app.route('/record/', methods = ['GET'])
def get_record():
    habit_list = list(db.habits.find({}, {'_id': False}))
    return jsonify({'result': 'success'}, {'habit_list': 'habit_list'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

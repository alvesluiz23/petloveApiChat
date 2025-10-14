from modelo import generate_answer
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    if request.method == "POST":
        body = request.get_json()
        if('question' not in body):
            return "Passar o campo question no json", 422
        return {
            "response": generate_answer(body['question'])
        }, 200


if( __name__ == '__main__'):
    app.run()
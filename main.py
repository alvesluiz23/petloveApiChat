from modelo import generate_answer
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    if request.method == "POST":
        body = request.get_json()
        return generate_answer(body['question'])

app.run()
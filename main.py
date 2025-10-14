from flask import Flask, request

app = Flask(__name__)

@app.route("/api/question-and-answer", methods=['POST'])
def question_and_answer():
    if request.method == "POST":
        return  request.get_json()
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

with open('./01_esercizi_json/es_039.json', 'r') as f:
    flashcards = json.load(f)

@app.route('/flashcard/<int:id>', methods=['GET', 'POST'])
def flashcard(id):
    message = ''
    flashcard = ""
    return render_template('39.html', flashcard=flashcard, message=message)
    

@app.route('/')
def home():
    return render_template('home.html', flashcards=flashcards)

def prompt_for_answer() -> str:
    user_answer = input("Enter your answer: ")
    return user_answer

def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.lower() == correct_answer.lower()

if __name__ == '__main__':
    app.run(debug=True, port=6969)


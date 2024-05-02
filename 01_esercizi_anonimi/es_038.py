from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def loggin():
    return render_template('loggin.html')

@app.route('/success', methods=['GET','POST'])
def success():
    username = request.form['username']
    email = request.form['email']
    return render_template('success.html', username1=username, email1=email)

if __name__ == '__main__':
    app.run(debug=True,port=6969)
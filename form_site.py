from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def root():
    return render_template('form.html')

@app.route('/welcome', methods = ['GET', 'POST'])

def welcome():
    return render_template('welcome.html', method = request.method, username= request.form['username'])

if __name__ == '__main__':
    app.debug = True
    app.run()

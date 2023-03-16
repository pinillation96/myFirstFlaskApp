from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username[0].isupper() and password.isalnum():
            return redirect(url_for('success'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/success')
def success():
    return "Login exitoso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
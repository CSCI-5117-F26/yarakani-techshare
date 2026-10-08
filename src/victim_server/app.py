from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "a lame secret key"

comments = []
USERNAME = "admin"
PASSWORD = "supersecretpassword"

@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('username') != 'admin':
        return redirect('/login')

    if request.method == 'POST':
        comment = request.form.get('comment', '') 
        if comment:
            comments.append(comment) 
        return redirect('/')

    # otherwise GET request
    return render_template('index.html', comments=comments)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect('/')
        return redirect('/login')


    return render_template('login.html')

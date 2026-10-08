from flask import Flask, request, render_template, redirect

app = Flask(__name__)

comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form.get('comment', '') 
        if comment:
            comments.append(comment) 
        return redirect('/')

    # otherwise GET request
    return render_template('index.html', comments=comments)

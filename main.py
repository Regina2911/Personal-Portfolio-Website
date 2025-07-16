from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    project = None
    if request.method == 'POST':
        if 'button_python' in request.form:
            project = 'python'
        elif 'button_telegram' in request.form:
            project = 'telegram'
        elif 'button_html' in request.form:
            project = 'html'
        elif 'button_db' in request.form:
            project = 'db'
    return render_template('index.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)

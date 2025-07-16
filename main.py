from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy  # ← добавлено

app = Flask(__name__)

# Подключаем SQLite базу
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для хранения отзывов
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    project = None
    if request.method == 'POST':
        # Если отправлена форма обратной связи
        if 'email' in request.form and 'text' in request.form:
            email = request.form['email']
            text = request.form['text']
            new_feedback = Feedback(email=email, text=text)
            db.session.add(new_feedback)
            db.session.commit()
        elif 'button_python' in request.form:
            project = 'python'
        elif 'button_telegram' in request.form:
            project = 'telegram'
        elif 'button_html' in request.form:
            project = 'html'
        elif 'button_db' in request.form:
            project = 'db'
    return render_template('index.html', project=project)

if __name__ == '__main__':
    with app.app_context():  
        db.create_all()    
    app.run(debug=True)

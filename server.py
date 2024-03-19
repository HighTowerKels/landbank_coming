from flask import Flask, render_template, redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

# Create SQLAlchemy model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Flask-Admin setup
admin = Admin(app, name='Flask App', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

# Route for form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route("/db")
def database():
    db.drop_all()
    db.create_all()
    return "Hello done!!!"



if __name__ == '__main__':
    app.run(debug=True, port=5000)

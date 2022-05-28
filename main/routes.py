from flask import redirect,render_template,url_for,flash
from main import app,db,bcrypt
from main.forms import RegistrationForm, LoginForm
from flask_login import login_user

from main.models import User

posts = [
    {
        "author": "Korir",
        "title": "jack Sparrow",
        "content": "Quite a movie",
        "date_posted": "May"
    },
    {
        "author": "Moses",
        "title": "jack Captain",
        "content": "Quit a movie",
        "date_posted": "May 2"
    }
]


@app.route('/')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(userName=form.userName.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your Account has been created","success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user =  User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return render_template(url_for("home"))
        else:
            flash("login Unsuccessful , Please check your details ", "danger")
    return render_template("login.html", title="Login", form=form)
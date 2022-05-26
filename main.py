from flask import Flask, render_template, url_for, config, flash,redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "4b9ce44826fe9027547e917dbc278ebd"
from forms import RegistrationForm, LoginForm

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
        flash(f"Account created for {form.userName.data}, ""success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data== "korir@gmail.com" and form.password.data=="1111":
            flash("you have been logged in ","success")
            return redirect(url_for("home"))
        else:
            flash("login Unsuccessful , Please check your details ", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

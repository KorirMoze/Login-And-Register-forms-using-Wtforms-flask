import os

from flask import redirect, render_template, url_for, flash, request,Response
from main import app, db, bcrypt
from main.forms import RegistrationForm, LoginForm, ProductForm
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, logout_user, login_required

from main.models import User, product


@app.route('/')
def home():
    return render_template("home.html", )


@app.route('/about')
def about():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(userName=form.userName.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your Account has been created", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("login Unsuccessful , Please check your details ", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout_user")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    image_file = url_for("static", filename='profile_pics/' + current_user.userImage)
    return render_template("account.html", title="Account", image_file=image_file)


@app.route("/index")
def index():
    image_file = url_for("static", filename='profile_pics')
    return render_template("home.html", title="home", image_file=image_file)


@app.route("/basket")
def html():
    return render_template("basket.html", title="Goods", )


@app.route("/productr", methods=["GET", "POST"])
def productr():
    if request.method == "POST":
        file = request.files['file']
        if file.filename != '':
            file.save(file.filename)
        productName = secure_filename(file.filename)
        mimetype = file.mimetype
        form = ProductForm()
        image = product(productImage=file.read(), productName=form.productName.data ,productDescription=form.productDescription.data)
        flash("No file uploaded")
        db.session.add(image)
        db.session.commit()
        return f"Uploaded: {file.filename}"

    form = ProductForm()
    return render_template("product.html", title="Admin", form=form)
@ app.route("/<int:id>")
def get_image(id):
    image = product.query.filter_by(id=id)
    if not image:
        return "no image"
    return Response(image)

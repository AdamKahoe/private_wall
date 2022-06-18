from flask import render_template, session,redirect, request,flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.models_user import User
from flask_app.models.models_message import Message



bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['POST'])
def register():

    is_valid = User.validate_user(request.form)

    if not is_valid:
        return redirect('/')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    # print(data,"$"*60)

    return redirect('/dashboard')

@app.route("/login",methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    # print("**********************************")
    print(user.email)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")

    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    messages = Message.get_user_messages(data)
    users = User.get_all()
    print(id)
    return render_template("dashboard.html",user=user,users=users, messages=messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


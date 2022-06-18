from email import message
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.models_user import User
from flask_app.models.models_message import Message

@app.route('/post_message',methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id":  request.form['sender_id'],
        "reciever_id": request.form['reciever_id'],
        "content": request.form['content']
    }
    Message.save(data)
    print(data,"&" * 60)
    return redirect('/dashboard')

@app.route('/delete/message/<int:id>')
def delete_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/dashboard')
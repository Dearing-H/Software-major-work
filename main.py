from flask import Flask, render_template, request, flash, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from setup_db import User, ToDo
from datetime import datetime

app = Flask(__name__)
app.secret_key = "abc123"

#set up the database engine and session
engine = create_engine("sqlite:///todo.db") #replace with your actual DB URI
Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=["GET", "POST"])

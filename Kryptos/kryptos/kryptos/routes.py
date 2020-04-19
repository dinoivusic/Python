from kryptos.models import User, Post
from flask import render_template, url_for, flash, redirect, request,abort, jsonify,request
from kryptos import app, db
from kryptos.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/post")
def about():
    return render_template('about.html', title='About')


@app.route("/suggestions")
def suggestions():
    path = os.path.abspath(r'kryptos/ether.csv')
    df = pd.read_csv(path)
    df.drop(['Date'], 1, inplace=True)
    # A variable for predicting n days in future
    prediction_days = 30
    # Create dependent variables shifted n units up
    df['Prediction'] = df[['Price']].shift(-prediction_days)
    # Create independent dataset and convert df to numpy array and drop prediciton column
    X = np.array(df.drop(['Prediction'], 1))
    # Remove n days rows
    X = X[:len(df) - prediction_days]
    # Create dependent dataset
    y = np.array(df['Prediction'])
    # Get all values except the last n rows
    y = y[:-prediction_days]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Set prediction days list equal to last 30 rows
    prediciton_days_list = np.array(df.drop(['Prediction'], 1))[-1:]
    # Create and train model SVM
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
    svr_rbf.fit(X_train, y_train)
    #svr_rbf.predict(X_test)
    predictionEth = float(svr_rbf.predict(prediciton_days_list))

    #Btc
    path = os.path.abspath(r'kryptos/Bitcoins.csv')
    df = pd.read_csv(path)
    df.drop(['Date'], 1, inplace=True)
    # A variable for predicting n days in future
    prediction_days = 30
    # Create dependent variables shifted n units up
    df['Prediction'] = df[['Price']].shift(-prediction_days)
    # Create independent dataset and convert df to numpy array and drop prediciton column
    X = np.array(df.drop(['Prediction'], 1))
    # Remove n days rows
    X = X[:len(df) - prediction_days]
    # Create dependent dataset
    y = np.array(df['Prediction'])
    # Get all values except the last n rows
    y = y[:-prediction_days]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Set prediction days list equal to last 30 rows
    prediciton_days_list = np.array(df.drop(['Prediction'], 1))[-1:]
    # Create and train model SVM
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
    svr_rbf.fit(X_train, y_train)
    # svr_rbf.predict(X_test)
    predictionBtc = float(svr_rbf.predict(prediciton_days_list))

    #LTC
    path = os.path.abspath(r'kryptos/litecoin.csv')
    df = pd.read_csv(path)
    df.drop(['Date'], 1, inplace=True)
    # A variable for predicting n days in future
    prediction_days = 30
    # Create dependent variables shifted n units up
    df['Prediction'] = df[['Price']].shift(-prediction_days)
    # Create independent dataset and convert df to numpy array and drop prediciton column
    X = np.array(df.drop(['Prediction'], 1))
    # Remove n days rows
    X = X[:len(df) - prediction_days]
    # Create dependent dataset
    y = np.array(df['Prediction'])
    # Get all values except the last n rows
    y = y[:-prediction_days]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Set prediction days list equal to last 30 rows
    prediciton_days_list = np.array(df.drop(['Prediction'], 1))[-1:]
    # Create and train model SVM
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
    svr_rbf.fit(X_train, y_train)
    # svr_rbf.predict(X_test)
    predictionLtc = float(svr_rbf.predict(prediciton_days_list))


    #NEO
    path = os.path.abspath(r'kryptos/neo.csv')
    df = pd.read_csv(path)
    df.drop(['Date'], 1, inplace=True)
    # A variable for predicting n days in future
    prediction_days = 30
    # Create dependent variables shifted n units up
    df['Prediction'] = df[['Price']].shift(-prediction_days)
    # Create independent dataset and convert df to numpy array and drop prediciton column
    X = np.array(df.drop(['Prediction'], 1))
    # Remove n days rows
    X = X[:len(df) - prediction_days]
    # Create dependent dataset
    y = np.array(df['Prediction'])
    # Get all values except the last n rows
    y = y[:-prediction_days]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # Set prediction days list equal to last 30 rows
    prediciton_days_list = np.array(df.drop(['Prediction'], 1))[-1:]
    # Create and train model SVM
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
    svr_rbf.fit(X_train, y_train)
    # svr_rbf.predict(X_test)
    predictionNeo = float(svr_rbf.predict(prediciton_days_list))
    return render_template('suggestions.html', title='Suggestions', predictionEth=predictionEth, predictionBtc=predictionBtc, predictionLtc=predictionLtc, predictionNeo=predictionNeo)



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can login now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",  methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account is updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form,legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))


"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, UserForm
from models import UserProfile

###
#Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
@login_required
def profile():
    form = UserForm()
    if request.method == "POST" and form.validate_on_submit():
        try:
            first_name=form.first_name.data
            last_name=form.last_name.data
            gender=form.gender.data
            username=form.user_id.data
            DOB=form.DOB.data
            meal_preference=form.meal_preference.data
            password=form.password.data
            
            user=UserProfile(first_name,last_name,gender,username,meal_preference,password,DOB)
            """ add an user to the database """
            db.session.add(user)
            db.session.commit()
            flash("Profile Added", "success")
            
            """ redirecting to the login page """
            return redirect(url_for("login"))
        except :
            db.session.rollback()
            flash("Internal Error", "danger")
            return render_template("register.html", form=form,title='Register')
    
    return render_template("register.html", form =form, title='Register')

@app.route("/login", methods=["GET", "POST"])
def login():
    """ handle requests to the /login route"""
    """logs an user through the Login Form"""
    
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        
        # Get the username and password values from the form 
        username=form.username.data
        password=form.password.data
        

            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.

        user = UserProfile.query.filter_by(username=username).first()
             # get user id, load into session
        if user is not None and user.verify_password(password): 
            
            """ logs in the user in """
            login_user(user)

            # remember to flash a message to the user
            flash(' You have logged in successfully.', 'success')
            
            return redirect(url_for("secure_page"))  # they should be redirected to a secure-page route instead
        else:
            flash("Login Failed",'danger')
            
     # load login template       
    return render_template("login.html", form=form, title="Login")
    
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

@app.route('/logout')
@login_required
def logout():

   ### Handle requests to the logout route ###

    ## Logs an user out through the logout link ###
    logout_user()
    flash("You have successfully been logged out.")
    
    return redirect(url_for('login'))



@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

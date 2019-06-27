from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")

def rend_inx():
    return render_template("index.html")

@app.route("/", methods=['POST'])

def filled_form():
    name_error=''
    pass_error=''
    ver_error=''

    name = request.form['name']

    if (not name) or (name.strip() == '') or (len(name) < 3) or len(name) > 20 or (' ' in name):
        name_error = "Please re-type your name. Must be between 3 and 20 characters, no spaces"
        
    password = request.form['password']

    if (not password) or (password.strip() == '') or (len(password)< 3) or (len(password) > 20) or (' ' in password):
        pass_error = "Please type in a valid password (3-20 characters long, no spaces)"
        
    verify_password = request.form['verify_password']

    if (not password) or (password.strip() == '') or(verify_password != password):
        ver_error = "Passwords do not match"
    
    e-mail = request.form['e-mail']

    if not('@' in e-mail) or not('.' in e-mail) or (' ' in e-mail):
        mail_error = "Please use proper e-mail format"
    
    if name_error or pass_error or ver_error:
        return render_template("index.html", user_name=name, email_addy=e-mail, name_error=name_error, pass_error=pass_error, ver_error=ver_error, mail_error=mail_error)
    else:
        return render_template("welcome.html", username=name)
    

app.run()
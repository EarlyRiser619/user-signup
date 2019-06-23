from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/index.html")
def filled_form():
    name = request.form['name']

    if (not name) or (name.strip() == ''):
        error = "Please type in your name"
        return redirect('/?error=' + error)

    password = request.form['password']

    if (not password) or (password.strip() == ''):
        error = "Please type in a valid password (3-20 characters long, no spaces)"
        return redirect('/?error=' + error)

    verify-password = request.form['verify_password']

    if (not verify-password) or (verify-password.strip() == ''):
        error = "Passwords do not match."
        return redirect('/?error=' + error)
    
    e-mail = request.form['email']

    # create conditionals for errors


    return render_template("welcome.html", name=name)



@app.route("/welcome.html")

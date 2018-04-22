from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('home.html'), 200


@app.route("/sin")
def sin():
    return render_template('sin.html'), 200


@app.route("/login")
def login():
    return render_template('login.html'), 200

@app.route('/software/project')
def software_project():
    return render_template('software.html'), 200

@app.route("/project")
def project():
    return render_template('project.html'), 200

@app.route("/comment")
def comment():
    return render_template('comment.html'), 200


@app.route("/abcd")
def abcd():
    return render_template(url_for('root'))



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




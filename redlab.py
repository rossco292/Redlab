from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('home.html'), 200


@app.route("/sin.html")
def sin():
    return render_template('sin.html'), 200


@app.route("/login.html")
def login():
    return render_template('login.html'), 200

@app.route('/software/project')
def software_project():
    return render_template('software.html'), 200

@app.route("/project.html")
def project():
    return render_template('project.html'), 200
	
@app.route("/hardware.html")
def hardware():
    return render_template('hardware.html'), 200

@app.route("/software.html")
def software():
    return render_template('software.html'), 200

@app.route("/engineering.html")
def engineering():
    return render_template('engineering.html'), 200	

@app.route("/comment.html")
def comment():
    return render_template('comment.html'), 200
	
@app.route("/about.html")
def about():
	return render_template('about.html'), 200
	
@app.route("/contact.html")
def contact():
	return render_template('contact.html'), 200
	
@app.route("/about")
def rerouteabout():
  return redirect('about.html')
	
@app.route("/login")
def reroutelogin():
  return redirect('login.html')

@app.route("/home.html")
def reroutehome():
  return redirect(url_for('root'))
  


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




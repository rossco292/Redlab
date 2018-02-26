from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('home.html'), 200


@app.route("/sin")
def sin():
    return render_template('sin.html'), 200

@app.route("/list")
def list():
    return render_template('list.html'), 200



@app.route("/abcd")
def abcd():
    return render_template(url_for('root'))

@app.errorhandler (404)
def page_not_found ( error ):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




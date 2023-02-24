from flask import Flask

app = Flask(__name__)

@app.route("/names")
def names():
    return {"names":["Jeff","Marc"]}

if __name__== "__main__" :
    app.run(debug=True)
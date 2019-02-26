from flask import Flask

app = Flask(__name__)

@app.route("/")
def whoami():
    return "Michael"



if __name__ == '__main__':
    app.run(debug=True,port=9999)

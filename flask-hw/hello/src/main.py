from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Rich Chow"
    age = "21"
    context = { 'a': "Rich", 'b':"Chow", 'c':"M" }
    return render_template("hello.html", name=name, age=age, **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

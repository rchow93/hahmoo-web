from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "moochie"
    age = "21"
    context = { 'a': "Rich", 'b':"Chow", 'c':"M" }
    moochie = { 'name': "S", 'last-name': "S", "Gender": "F"}
    return render_template("hello.html", name=name, age=age, **context, moochie=moochie)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

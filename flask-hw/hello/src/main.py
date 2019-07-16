from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "moochie"
    age = "21"
    context = { 'a': "Rich", 'b':"Chow", 'c':"M" }
    moochie = { 'name': "S", 'last-name': "S", "Gender": "F"}
    mylist = [5,12,99,2,53]
    return render_template("hello.html", name=name, age=age, **context, moochie=moochie, mylist=mylist)

@app.route('/success/<bmi>')
def success(bmi):
    return 'Your BMI is %s' % str(bmi)

@app.route('/bmi',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        height = request.form['height']
        height = float(height)
        mass = request.form['mass']
        mass = float(mass)
        bmi = mass / (height*height)
        bmi = round(bmi,2)
        return redirect(url_for('success',bmi=bmi))
    else:
        return render_template('bmi.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

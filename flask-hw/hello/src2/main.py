from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        symbols = request.form['symbols']
#        symbols = bool(symbols)
        numbers = request.form['numbers']
#        numbers = bool(numbers)
#        bmi = mass / (height*height)
#        bmi = round(bmi,2)
        return render_template('answer.html', symbols=symbols, numbers=numbers)
    else:
        return render_template('index.html')

'''

@app.route('/answer')
def success(height, mass, bmi):
    return render_template('answer.html', height=height, mass=mass, bmi=bmi)

@app.route('/bmi',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        height = request.form['height']
        height = float(height)
        mass = request.form['mass']
        mass = float(mass)
        bmi = mass / (height*height)
        bmi = round(bmi,2)
        return render_template('answer.html', height=height, mass=mass, bmi=bmi)
    else:
        return render_template('ask.html')

  
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
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

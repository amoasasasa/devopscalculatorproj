from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])

def index():
    result = None
    if request.method == 'POST':
        try :
            num1 = float(request.form['num1']) 
            num2 = float(request.form['num2'])
        except ValueError:
            result = "enter integer"
            return render_template('calculator.html',result=result)
        operator = request.form['operator']
        if operator == 'add':
            result = float(num1 + num2)
        elif operator == 'subtract':
            result = float(num1 - num2)
        elif operator == 'multiply':
            result = float(num1 * num2)
        elif operator == 'divide':
            result = float(num1 / num2)
        else :
            result = "invalid operator"
            return render_template('calculator.html',result=result)
    return render_template('calculator.html',result=result)

if __name__ == '__main__':
    #add host ip address on which app is going to run
    app.run(host='0.0.0.0',debug=True)  
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            result = num1 / num2
    
    return render_template('calculator.html',result=result)

if __name__ == '__main__':
    #add host ip address on which app is going to run
    app.run(host='0.0.0.0',debug=True)
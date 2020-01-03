from flask import Flask, request
from fractions import Fraction
from decimal import Decimal

app = Flask(__name__)
@app.route('/')
def index():
    return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
    try:
        val1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val1='None'
    try:
        val2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val2='None'
    if val1 == 'None' or val2 == 'None' :
        return 'None'
    else:
        X = Fraction(val1)
        Y = Fraction(val2)
        result= X+Y
        return str(round(float(result),4))

@app.route('/sub')
def subtraction():
    try:
        val1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val1='None'
    try:
        val2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val2='None'
    if val1 == 'None' or val2 == 'None' :
        return 'None'
    else:
        X = Fraction(val1)
        Y = Fraction(val2)
        result= X-Y
        return(str(round(float(result),4)))


@app.route('/mul')
def multiplication():
    try:
        val1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val1='None'
    try:
        val2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val2='None'
    if val1 == 'None' or val2 == 'None' :
        return 'None'
    else:
        X = Fraction(val1)
        Y = Fraction(val2)
        result= X*Y
        return(str(round(float(result),4)))

@app.route('/div')
def division():
    try:
        val1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val1='None'
    try:
        val2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        val2='None'
    if val1 == 'None' or val2 == 'None' :
        return 'None'
    else:
        X = Fraction(val1)
        Y = Fraction(val2)
        try:
            result= X/Y
            return(str(round(float(result),4)))
        except ZeroDivisionError as error:
            return 'None'

if __name__ == "__main__":
    app.run()

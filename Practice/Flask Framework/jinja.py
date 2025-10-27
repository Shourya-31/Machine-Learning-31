## Building Url Dynamically
## Variable Rule

## Jinja 2 Template engine
'''
{{  }} expresion to read from backend datasource and o/p in html
{%...%} for conditional statements
{#...#} single lined comments
'''

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")  # decorator
def welcome():  # fixed typo
    return "<html><H1>Welcome! Its great!! Right</H1></html>"

@app.route("/index")  # decorator
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name} there!'
    return render_template('form.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Helloooooooooo {name} there!'
    return render_template('form.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    # return "The marks you got is: " + str(score)
    res=""
    if score>=70:
        res="Great Job! Passed!"
    else:
        res="You can improve!"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    # return "The marks you got is: " + str(score)
    res=""
    if score>=70:
        res="Great Job! Passed!"
    else:
        res="You can improve!"
    
    exp={'score:':score,"res:":res}
    return render_template('result1.html',results=exp)

# if condition
@app.route('/successif/<int:score>')
def successif(score):
    # return "The marks you got is: " + str(score)
    res=""
    return render_template('resultif.html',results=score)

## Building Url Dynamically
@app.route('/fail/<int:score>')
def fail(score):

    return render_template('resultif.html',results=score)

@app.route('/submitt',methods=['POST','GET'])
def submitt():
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        
        total_score_avg=(science+maths+c+data_science)/4
        return redirect(url_for('successres',score=total_score_avg))
    return render_template('getresults.html')
    
if __name__ == "__main__":
    app.run(debug=True)  # automatically reloads on code changes

from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run(debug=True)  # automatically reloads on code changes

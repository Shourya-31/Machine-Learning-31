# from flask import Flask

# ## WSGI (Web Server Gateway Interface) Apllication
# app=Flask(__name__)

# # Skeleton 

# if __name__=="__main__":
#     app.run()

from flask import Flask, render_template

app=Flask(__name__)

@app.route("/") #decorator
def welcom():
    return "<html><H1>Welcome! Its great!! Right</H1></html>"

@app.route("/index") #decorator
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True) # Help to update the web page by restarting the server on saving

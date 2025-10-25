# from flask import Flask

# ## WSGI (Web Server Gateway Interface) Apllication
# app=Flask(__name__)

# # Skeleton 

# if __name__=="__main__":
#     app.run()

from flask import Flask

app=Flask(__name__)

@app.route("/") #decorator
def welcom():
    return "Welcome! Its great!! Right"

@app.route("/index") #decorator
def index():
    return "Welcome! Its great!! Haha!"

if __name__=="__main__":
    app.run(debug=True) # Help to update the web page by restarting the server on saving

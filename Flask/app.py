from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    print("Hey Print")
    return "Hello, It's a flask app. Hey this is main root."


@app.route("/index")
#with html tag
def index():
    return "<html><h1>Hey from Index</h1></html>"

@app.route("/about")
def about():
    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True)

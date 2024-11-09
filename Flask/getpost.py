from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def welcome():
    print("Hey Print")
    return "<h1>Hello, It's a flask app. Hey this is main root.</h1>"


@app.route("/form",methods=["Get","POST"])
def about():
    if request.method=='POST':
        name=request.form["name"]
        return f"Hello {name}!, Welcome to the app."
    return render_template("form.html")


#with conditions

@app.route("/result",methods=["POST","GET"])
def result():
    total=0
    if request.method=="POST":
        math=float(request.form['math'])
        hindi=float(request.form['hindi'])
        english=float(request.form['english'])
        total=(math+hindi+english)/3

        marks={"Hindi":hindi,"Math":math,"English": english,"Total":total}

        return render_template("result.html",results=marks)
    return render_template("formdata.html")



if __name__=="__main__":
    app.run(debug=True)
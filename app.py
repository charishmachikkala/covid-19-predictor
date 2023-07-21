from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)
@app.route('/')
def input():
        return render_template('input.html')
@app.route("/index",methods=['POST',"GET"])
def index():
        if request.method=='POST':
                return redirect(url_for('index'))
        return render_template("index.html")
@app.route("/display",methods=['POST',"GET"])
def display():
        name=request.args.get("name")
        age=request.args.get("age")
        question_1=request.args.get("question_1")
        question_2=request.args.get("question_2")
        question_3=request.args.get("question_3")
        question_4=request.args.get("question_4")
        question_5=request.args.get("question_5")
        question_6=request.args.get("question_6")
        question_7=request.args.get("question_7")
        question_8=request.args.get("question_8")
        question_9=request.args.get("question_9")
        question_10=request.args.get("question_10")
        return render_template('display.html',name=name,age=age,question_1=question_1,question_2=question_2,question_3=question_3,question_4=question_4,question_5=question_5,question_6=question_6,question_7=question_7,question_8=question_8,question_9=question_9,question_10=question_10)
if __name__=='__main__':
     app.run(debug=True)
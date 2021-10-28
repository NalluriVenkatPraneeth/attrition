from flask import Flask,render_template,request
from flasgger import Swagger

#WSGI
app = Flask(__name__)
Swagger(app)

@app.route('/',methods=['GET'])
def welcome():
    return render_template("index.html")
@app.route('/name/<name>')
def names(name):
    return f"Welcome to {name}"

@app.route('/checking_req',methods=['POST','GET'])
def get_params():
    """ Practicing Swagger
    ---
    parameters:
     - name: student_name
       in: query
       type: string
       required: true
     - name: rollno
       in: query
       type: number
       required: true
    responses:
       200:
            description: Result is

    """
    student_name = request.args.get("student_name")
    rollno = request.args.get("rollno")
    return f"student name is {student_name} and roll no is {rollno}"

if __name__ == "__main__":
    app.run(debug=True)
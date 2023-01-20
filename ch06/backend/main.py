from crypt import methods
from flask import Flask, request
from database import Connection
from database import Employees

app = Flask(__name__)
connection = Connection(
    "postgresql://streamlit:streamlit309@127.0.0.1:5432/CompanyData"
)


@app.route("/employees")
def get_all_employees():
    with connection.use_session() as session:
        employees = session.query(Employees).all()
        employees = [employee.to_dict() for employee in employees]
        return {"data": employees}


@app.route("/employee", methods=["POST"])
def add_employee():
    body = request.json
    with connection.use_session() as session:
        session.add(Employees(**body))
        session.commit()
    return {"message": "New employee added successfully"}


app.run()

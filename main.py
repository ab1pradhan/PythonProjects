'''
Build a REST application in Python which does the following thing :
1) employeeCountByDept()
2) findEmp(empName, condition) - empName should work along with condition - condition is startWith/endsWith/Like Operator/Case Sensitive/Case Insensitive
3) Data has to be stored in Database and fetch the data using JDBC/ODBC
4) DB + Application should be running in Docker container
5) The code should have well designed classes & funtions - good coding standards + documentation

'''

import uvicorn
from fastapi import FastAPI
from schemas import Employee
import pyodbc
import json
import config
import py_functions
#from fastapi.security import OAuth2PasswordBearer


def connect_db():
    # Create a cursor from the connection
    conn = pyodbc.connect(config.connection_string)
    conn.autocommit = True
    return conn

# Database connection
conn = connect_db()

app = FastAPI()

@app.get("/")
async def getitems():
    df = py_functions.get_all(conn)
    return df.to_dict('records')

@app.get("/dept_count")
async def employeeCountByDept():
    df = py_functions.count_by_dept(conn)
    return df.to_dict('records')

@app.get("/emp_details")
async def employeesearch(empName:str, condition:str):
    # URL --> http://127.0.0.1:80/emp_details?empName=amit&condition=like

    df = py_functions.fetch_emp_by_condition(conn,empName,condition)
    return df.to_dict('records')

@app.post("/new_emp/")
async def add_emp(emp : Employee):
    out = py_functions.add_entry(conn, emp.emp_name, emp.dept)
    if out:
        return {"res":"data inserted"}
    else:
        return {"res":"Not inserted"}





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 80)

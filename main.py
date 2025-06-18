from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from neo4j import GraphDatabase, basic_auth


app = FastAPI()

# Sandbox
URI = "bolt://44.200.9.221:7687"
AUTH = basic_auth('neo4j', 'explosions-warning-gravity')

# Local
# URI = "bolt://localhost:7687"
# AUTH = ("neo4j", "123456789")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()


class EmployeeCreate(BaseModel):
    name: str
    emp_id: int



@app.post("/employee")
def create_employee(employee: EmployeeCreate):
    with driver.session(database="employee") as session:
        # Check if emp_id already exists
        result = session.run(
            "MATCH (e:Employee {emp_id: $emp_id}) RETURN e",
            emp_id=employee.emp_id
        )
        if result.single():
            raise HTTPException(status_code=400, detail="Employee ID already exists")

        # Create the Employee node
        session.run(
            "CREATE (e:Employee {name: $name, emp_id: $emp_id})",
            name=employee.name,
            emp_id=employee.emp_id
        )

    return {"message": "Employee node created", "employee": employee}



@app.get("/employees")
def get_all_employees():
    with driver.session(database="employee") as session:
        result = session.run("MATCH (e:Employee) RETURN e.name AS name, e.emp_id AS emp_id")
        employees = []
        for record in result:
            employees.append({
                "name": record["name"],
                "emp_id": record["emp_id"]
            })
    return employees


# @app.delete("/employee/{emp_id}")
# def delete_employee(emp_id: int):
#     with driver.session(database="employee") as session:
#         # Vérifie si l'employé existe
#         result = session.run(
#             "MATCH (e:Employee {emp_id: $emp_id}) RETURN e",
#             emp_id=emp_id
#         )
#         if not result.single():
#             raise HTTPException(status_code=404, detail="Employee not found")

#         # Supprime le noeud Employee
#         session.run(
#             "MATCH (e:Employee {emp_id: $emp_id}) DELETE e",
#             emp_id=emp_id
#         )

#     return {"message": f"Employee with ID {emp_id} deleted"}
# 
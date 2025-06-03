from neo4j import GraphDatabase

uri = "bolt+s://0b6ec3d2333f856e991a353950da4ec2.neo4jsandbox.com:7474"
username = "neo4j"
password = "buckles-forearm-interaction"

driver = GraphDatabase.driver(uri, auth=(username, password))

with driver.session() as session:
    result = session.run("RETURN 1 AS val")
    print(result.single()["val"])

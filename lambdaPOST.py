import sys
import pymysql
import json


def handler(event, context):
    statusCode = 200
    message = []

    rds_host  = "rds-mysql-demo.csnnean90nqb.us-east-2.rds.amazonaws.com"
    name = "KyleYangRDS"
    password = "tiger8319610"
    db_name = "demoRDSDB"

    newName = json.loads(event["body"]).get("newName", "AAA")
    newEmpID = json.loads(event["body"]).get("newEmpID", "BBB")

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        print("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    print "SUCCESS: Connection to RDS mysql instance succeeded"

    cur = conn.cursor()
    sql = "INSERT INTO `Employee3` (`EmpID`,`Name`) VALUE ('%s', '%s')" % (newEmpID, newName)

    try:
        cur.execute(sql)
        conn.commit()
        print "Input Data"

        cur.execute("select * from Employee3")
        for row in cur:
            message.append(row)

        statusCode = 200
        body = {'message' : message}

    except:
        conn.rollback()
        print "Input Data Fail"

        body = {'message' : 'Input Data Fail'}
        statusCode = 400

    if conn:
        conn.close()

    response = {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
          "Access-Control-Allow-Origin": "*"
        }
    }

    return response

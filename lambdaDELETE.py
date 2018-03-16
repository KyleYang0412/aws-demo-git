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

    newEmpID = json.loads(event["body"]).get("newEmpID", "BBB")
    print "newEmpID", newEmpID
    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        print("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    print "SUCCESS: Connection to RDS mysql instance succeeded"

    cur = conn.cursor()
    sql = "DELETE FROM `Employee3` WHERE `EmpID` = '%s'" % (newEmpID)

    try:
        cur.execute(sql)
        conn.commit()
        print "Delete Data"

        cur.execute("select * from Employee3")
        for row in cur:
            message.append(row)

        statusCode = 200
        body = {'message' : message}

        print "Delete Data Success"

    except:
        conn.rollback()
        print "Delete Data Fail"

        body = {'message' : 'Delete Data Fail'}
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

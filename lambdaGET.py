import sys
import pymysql
import json


def handler(event, context):
    statusCode = 200
    message = []

    rds_host  = "rds-mysql-demo.csnnean90nqb.us-east-2.rds.amazonaws.com"
    name = "USER_NAME"
    password = "USER_PASSWORD"
    db_name = "DB_NAME"

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        print("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    print "SUCCESS: Connection to RDS mysql instance succeeded"

    cur = conn.cursor()
    sql = "select * from Employee3"

    try:
        cur.execute(sql)
        conn.commit()
        for row in cur:
            message.append(row)

        statusCode = 200
        body = {'message' : message}

    except:
        conn.rollback()

        statusCode = 400
        body = {'message' : 'Get Data Fail'}

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

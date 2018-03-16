## A Simple Web Application Using AWS RDS, Lambda, and API Gateway

### Client
==========
#### 1. GET
- List all user info

#### 2. POST
- Insert user ID and user NAME to RDS
- Input - user ID/user Name

#### 3. DELETE
- Delete user info by user ID
- Input - user ID

### Server
==========
#### AWS Service

#### 1. Amazon API Gateway
- Method - GET/POST/DELETE
  
#### 2. AWS Lambda
- Runtime - Python2.7
- Method GET Function - awsDemoLambdaGet
- Method POST Function - awsDemoLambda
- Method DELETE Function - awsDemoLambdaDelete

#### 3. Amazon Relational Database Service(RDS)
- DB Engine - MySQL 5.6.39
- DB instance class - db.t2.micro


*******************
### Reference
[Amazon]:https://aws.amazon.com/tw/
[Docker]:https://hub.docker.com/
[MySql]:https://www.mysql.com/
[Python]:https://www.python.org/
[jQuery]:https://jquery.com/

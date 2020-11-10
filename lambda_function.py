import json
import boto3

def addDataInSNS(data):
    a = 10
    sns = boto3.client('sns')
    sns.subscribe(TopicArn='arn:aws:sns:us-east-2:354117786283:sample',Protocol='email',Endpoint=data['email'])
    sns.publish(TopicArn = 'arn:aws:sns:us-east-2:354117786283:sample', Subject = 'ok', Message = "Hello")

def addDataInDynamoDb(data):
    #if not dynamodb:
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('notifier')
    response = table.put_item(Item={'name': data['username'],'email': data['email'],'package': data['package']})
   
    

def lambda_handler(event, context):
    
    string = str(event)
    encoded_string = string.encode("utf-8")

    bucket_name = "notifierfile"
    file_name = "hello.txt"
    lambda_path = "/tmp/" + file_name
    s3_path = "/" + file_name

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
    addDataInDynamoDb(event)
    addDataInSNS(event)
    

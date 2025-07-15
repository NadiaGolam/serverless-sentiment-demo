import json
import boto3
import os
from datetime import datetime

comprehend = boto3.client('comprehend')
dynamodb  = boto3.resource('dynamodb')
table     = dynamodb.Table(os.environ['DYNAMO_TABLE'])

def lambda_handler(event, context):
    for rec in event['Records']:
        bkt = rec['s3']['bucket']['name']
        key = rec['s3']['object']['key']
        s3  = boto3.client('s3')
        txt = s3.get_object(Bucket=bkt, Key=key)['Body'].read().decode()
        resp = comprehend.detect_sentiment(Text=txt, LanguageCode='en')
        item = {
          'id':        f"{bkt}/{key}",
          'timestamp': datetime.utcnow().isoformat(),
          'sentiment': resp['Sentiment'],
          'details':   resp
        }
        table.put_item(Item=item)
    return {'statusCode':200, 'body':json.dumps({'message':'Done'})}

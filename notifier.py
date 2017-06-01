import logging

import boto3

client = boto3.client('sns', region_name='us-west-2')

def notify(subject, body):
    result = client.publish(
        #TopicArn='arn:aws:sns:us-west-2:181051542904:nlp',
        TargetArn='arn:aws:sns:us-west-2:181051542904:nlp',
        #PhoneNumber='+19293237674',
        Message='{}:\n{}'.format(subject, body),
        #Subject='string',
        #MessageStructure='string',
        #MessageAttributes={
        #    'string': {
        #        'DataType': 'string',
        #        'StringValue': 'string',
        #        'BinaryValue': b'bytes'
        #    }
        #}
    )
    print(f'notification result: {result}')

notify('Results', 'Confusion matrix: ...')

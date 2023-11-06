import json
import boto3

def lambda_handler(event, context):

    user_pool_id = 'us-east-1_dnXTz0DGG'
    client_id = '6k30uhnmuksb8ftd3ed3kib56b'

    cognito_client = boto3.client('cognito-idp')
    
    
    
    try:
        
        if 'body' in event:
        
            request_body = json.loads(event['body'])
            
            if 'cpf' in request_body:
                cpf = request_body['cpf']
            
            if 'password' in request_body:
                password = request_body['password']

        
        username = cpf
        password = password #'Postech@2023'
    
        response = cognito_client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
            }
        )

        access_token = response['AuthenticationResult']['AccessToken']

        return {
            'statusCode': 200,
            'body': json.dumps('Bearer '+access_token)
        }
    

    except Exception as e:
        return {
            'statusCode': 401, 
            'body': str(e)
        }
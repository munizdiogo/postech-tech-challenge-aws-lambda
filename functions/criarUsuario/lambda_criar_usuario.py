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
            
            if 'name' in request_body:
                name = request_body['name']
            
            if 'email' in request_body:
                email = request_body['email']
        
        password = 'Postech@2023'
        username = cpf
    
        
        user_attributes = [
            {
                'Name': 'email',
                'Value': email
            },
            {
                'Name': 'name',
                'Value': name
            },
            {
                'Name': 'custom:cpf',
                'Value': cpf
            }
        ]
    
            
        response = cognito_client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=username,
            UserAttributes=user_attributes,
            TemporaryPassword='Temp@2023', 
            MessageAction='SUPPRESS'  
         )
         
        response = cognito_client.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=username,
            Password=password,
            Permanent=True
        )
    
        return {
            'statusCode': 200,
            'body':  json.dumps({
                'status' : 'usuario-criado-com-sucesso',
                'atributos' : {
                    'email': email,
                    'nome': name,
                    'cpf': cpf
                }
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': str(e)
        }
import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directorio']
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{nombre_directorio}/')

    return {
        'statusCode': 200,
        'mensaje': f'Directorio {nombre_directorio}/ creado en {nombre_bucket}'
    }
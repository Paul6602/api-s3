import boto3

def lambda_handler(event, context):

    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directorio']
    nombre_archivo = event['body']['archivo']
    contenido = event['body']['contenido']

    # Proceso
    s3 = boto3.client('s3')

    response = s3.put_object(
        Bucket=nombre_bucket,
        Key=nombre_directorio + '/' + nombre_archivo,
        Body=contenido
    )

    # Salida
    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'archivo': nombre_archivo,
        'response': str(response)
    }
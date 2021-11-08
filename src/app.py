def handler(event, context):
    response = {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json"
        },
        'body': 'some stuff normally goes here'
    }
    
    return response
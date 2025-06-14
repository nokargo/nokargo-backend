def handler(event, context):
    print("Auto-disable IAM user logic goes here")
    return {
        'statusCode': 200,
        'body': 'IAM user disable triggered'
    }

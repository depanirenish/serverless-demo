import json


def hello(event, context):
    body = {
        "message": "This is github action!",
        "custom_heading": "This is value of custom heading",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

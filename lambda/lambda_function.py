import json

def lambda_handler(event, context):
    print("Event received:", event)

    # Extract values sent by Django
    room_id = event.get("room_id", None)
    is_available = event.get("is_available", True)
    discount = event.get("discount", 0)

    # Response back to Django
    return {
        "statusCode": 200,
        "body": json.dumps({
            "room_id": room_id,
            "is_available": is_available,
            "discount": discount,
            "message": "Room check processed successfully"
        })
    }


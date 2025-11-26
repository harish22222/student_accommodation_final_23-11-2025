import boto3
from botocore.exceptions import ClientError

def test_send_sns():
    sns_client = boto3.client("sns", region_name="us-east-1")

    topic_arn = "arn:aws:sns:us-east-1:471112797649:BookingNotifications" 

    subject = "🔔 SNS Test Notification"
    message = "Hello! This is a test SNS message from your Student Accommodation project."

    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Subject=subject,
            Message=message
        )
        print("✅ SNS message sent successfully!")
        print(response)
    except ClientError as e:
        print("❌ SNS error:", e)

if __name__ == "__main__":
    test_send_sns()

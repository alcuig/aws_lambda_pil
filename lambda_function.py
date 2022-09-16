import boto3
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    input_file_path = '/tmp/input_file.jpg'
    output_file_path = '/tmp/output_file.png'
    
    s3.download_file(source_bucket, object_key, input_file_path)

    im1 = Image.open(input_file_path)
    im1.save(output_file_path)

    target_bucket = 'aws-boto-output'
    with open(output_file_path, "rb") as f:
        s3.upload_fileobj(f, target_bucket, object_key.replace(".jpg", ".png"))

    return True



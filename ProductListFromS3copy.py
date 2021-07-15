import json
import boto3

s3 = boto3.client('s3')
 

def lambda_handler(event, context):
    
    bucket = 'store-product-list'
    key = 'sampleProducts.json'
    
    response = s3.get_object(Bucket=bucket, Key=key)
    
    content = response['Body']
    
    jsonObject = json.loads(content.read())
    
    sampleProducts = jsonObject["sampleProducts"]
    
    for record in sampleProducts:
        print("Product Name: " +record['prod_name'])
        print("Product Price: " +str(record['prod_price']))
        print("Product Image: " +str(record['prod_image']))
        print("Product Quantity: " +str(record['prod_qty']))
        print("---Success---")
        
        
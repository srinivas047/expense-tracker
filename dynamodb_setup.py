import boto3

dynamodb = boto3.resource('dynamodb')

def create_expense_table():
    table = dynamodb.create_table(
        TableName='Expenses',
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print("Table created successfully")

if __name__ == "__main__":
    create_expense_table()

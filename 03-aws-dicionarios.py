
# import json
# def ler_json(arq_json):
#     with open(arq_json, 'r', encoding='utf8') as f:
#         return json.load(f)
#         print(type(f))


# print(len(lista))
# print(type(lista))

# import boto3
# client = boto3.client('s3')
# response = client.list_buckets()
# print(type(response))
# for bucket in response['Buckets']:
#     print(bucket['Name'])

# #Exemplo pratico de dicionarios:
# import boto3
# region = 'sa-east-1'
# ec2 = boto3.client('ec2', region_name=region)


# #função, listar e parar todos as instancias t2.micro de uma vez e salvar log num json
# def pegar():
#     print('Into DescribeEc2Instance')
#     instances = ec2.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])
#     for ins_id in instances['Reservations']:
#                 print(type(ins_id))
#                 print(ins_id)
#                 input("continue")
#                 print('----- \n')
# pegar()
	
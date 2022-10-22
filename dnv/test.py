from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient
import pandas as pd
sas_url = "https://we1dnvglpstgcus0000c9k8z.blob.core.windows.net/aisyrisk-samples91a25ad6-b81e-4aaf-a7fc-bc7548c5d454?sv=2018-03-28&sr=c&sig=pPrxD9x9EllCv0e%2F9VxG975QDznncB%2BD7eKUqzg1Pko%3D&st=2022-10-21T12%3A08%3A47Z&se=2022-11-20T13%3A09%3A50Z&sp=rl"
container = ContainerClient.from_container_url(sas_url)

# Get the BlobClient from the ContainerClient to interact with a specific blob
blob_client = container.get_blob_client("test.txt")

#Get container content list
blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name)

print("Hello world")
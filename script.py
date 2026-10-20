import os
import pandas as pd
import boto3
from pathlib import Path
from datetime import date
now =  date.today()
file_path = r"C:\Users\darce\OneDrive\Desktop\Coding Projects\PycharmProjects\PlusUltraCreditUnion\templates\anime_bank_accounts_sample.csv"
file_name = f"batch_update_{now}.txt"
folder_path = r"C:\Users\darce\OneDrive\Desktop\Coding Projects\PycharmProjects\PlusUltraCreditUnion\templates"
fp2 = os.path.join(folder_path, file_name)
df = pd.read_csv(file_path, header=None, names=["First_Name", "Last_Name", "Account_Number"])
Path(fp2).touch()
print(fp2)
client = boto3.client(
            "s3",
            aws_access_key_id="INSERT",
            aws_secret_access_key="INSERT",
            region_name="INSERT"
        )
for row_str in df.astype(str).apply(lambda x: ', '.join(x), axis=1):
    data = row_str.split(",")
    sentence =f"{data[0].strip()} {data[1].strip()} Account Number is: #{data[2].strip()}\n"
    with open(fp2, 'a') as file:
        file.write(sentence)
    print(sentence)

if os.path.exists(file_path):
    local_path = os.path.join("./templates", "anime_bank_accounts_sample.csv")
    with open(local_path, 'rb') as data:
        client.upload_fileobj(data, "plus-ultra-credit-union-saves-bucket", "anime_bank_accounts_sample.csv")
    os.remove(file_path)


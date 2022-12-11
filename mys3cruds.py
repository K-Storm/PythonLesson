from tkinter import *
from tkinter import ttk
import boto3
import os

AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

class S3Methods:
    # オブジェクト更新
    def s3_put_object():
        bucket_name = "kunimitsu-test"
        directory_name = "test/test4"
        s3.put_object(Bucket=bucket_name, Key=directory_name+'/')

    # バケット一覧取得
    def s3_get_object():
        res = s3.list_buckets()
        print(res)

    # バケットのオブジェクト削除
    def s3_delete_object():
        bucket_name = "kunimitsu-test"
        directory_name = "test/test4"
        s3.delete_object(Bucket=bucket_name, Key=directory_name+'/')
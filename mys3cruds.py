from tkinter import *
from tkinter import ttk
import boto3
import os
import json

session = boto3.Session(profile_name="k-storm")
s3= session.client('s3')

class S3Methods:
    # オブジェクト更新
    def s3_put_object():
        bucket_name = "sample-test"
        directory_name = "test/test4"
        s3.put_object(Bucket=bucket_name, Key=directory_name+'/')

    # バケット一覧取得
    def s3_get_object():
        res = s3.list_buckets()
        bucket_name_str = json.dumps(res["Buckets"], default=str)
        bucket_name_dict = json.loads(bucket_name_str)
        for i in range(len(bucket_name_dict)):
            print("Bucketname:",bucket_name_dict[i]["Name"])

    # バケットのオブジェクト削除
    def s3_delete_object():
        bucket_name = "kunimitsu-test"
        directory_name = "test/test4"
        s3.delete_object(Bucket=bucket_name, Key=directory_name+'/')
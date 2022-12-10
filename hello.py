from tkinter import *
from tkinter import ttk
import boto3
import os

AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

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

def sub_window():
    sub_root = Tk()
    sub_root.title('aws s3 CRUD')
    sub_frame = ttk.Frame(sub_root, padding=16)
    sub_label = ttk.Label(sub_frame, text='S3オブジェクト更新')
    str = StringVar()
    sub_entry = ttk.Entry(sub_frame, textvariable=str)
    sub_button = ttk.Button(
        sub_frame,
        text='PutObject',
        command=lambda: s3_put_object()
    )

    get_label = ttk.Label(sub_frame, text='S3バケット検索')
    str = StringVar()
    get_entry = ttk.Entry(sub_frame, textvariable=str)
    get_button = ttk.Button(
        sub_frame,
        text='GetObject',
        command=lambda: s3_get_object()
    )

    delete_label = ttk.Label(sub_frame, text='S3バケット検索')
    str = StringVar()
    delete_entry = ttk.Entry(sub_frame, textvariable=str)
    delete_button = ttk.Button(
        sub_frame,
        text='DeleteObject',
        command=lambda: s3_delete_object()
    )

    sub_frame.pack()
    sub_label.pack(side=LEFT)
    sub_entry.pack(side=LEFT)
    sub_button.pack(side=LEFT)
    get_label.pack(side=LEFT)
    get_entry.pack(side=LEFT)
    get_button.pack(side=LEFT)
    delete_label.pack(side=LEFT)
    delete_entry.pack(side=LEFT)
    delete_button.pack(side=LEFT)

root = Tk()
root.title('AWS S3 CRUD')

frame1 = ttk.Frame(root, padding=16)
t = StringVar()
button1 = ttk.Button(
    frame1,
    text='START',
    command=lambda: sub_window()
)

frame1.pack()
button1.pack(side=LEFT)

root.mainloop()
from tkinter import *
from tkinter import ttk
import boto3
import os

AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]

def s3_ls():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    bucket_name = "***"
    directory_name = "test/test2"
    s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))


def sub_window():
    sub_root = Tk()
    sub_root.title('aws s3 CRUD')
    sub_frame = ttk.Frame(sub_root, padding=16)
    sub_label = ttk.Label(sub_frame, text='S3バケット検索')
    str = StringVar()
    sub_entry = ttk.Entry(sub_frame, textvariable=str)
    sub_button = ttk.Button(
        sub_frame,
        text='PutObject',
        command=lambda: s3_ls()
    )

    sub_frame.pack()
    sub_label.pack(side=LEFT)
    sub_entry.pack(side=LEFT)
    sub_button.pack(side=LEFT)

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
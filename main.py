from tkinter import *
from tkinter import ttk
import boto3
import os
import mys3cruds

s3ope=mys3cruds.S3Methods

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
        command=lambda: s3ope.s3_put_object()
    )

    get_label = ttk.Label(sub_frame, text='S3バケット検索')
    str = StringVar()
    get_entry = ttk.Entry(sub_frame, textvariable=str)
    get_button = ttk.Button(
        sub_frame,
        text='GetObject',
        command=lambda: s3ope.s3_get_object()
    )

    delete_label = ttk.Label(sub_frame, text='S3バケット検索')
    str = StringVar()
    delete_entry = ttk.Entry(sub_frame, textvariable=str)
    delete_button = ttk.Button(
        sub_frame,
        text='DeleteObject',
        command=lambda: s3ope.s3_delete_object()
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
from tkinter import *
from tkinter import ttk
import boto3
import os
import mys3cruds

s3ope=mys3cruds.S3Methods

def sub_window():
    root_sub_window = Tk()
    root_sub_window.title('aws s3 CRUD')
    root_sub_window.geometry("600x600")
    put_sub_frame = ttk.Frame(root_sub_window, padding=16)
    s3_put_label = ttk.Label(put_sub_frame, text='S3オブジェクト更新')
    str1 = StringVar()
    s3_put_entry = ttk.Entry(put_sub_frame, textvariable=str1)
    put_button = ttk.Button(
        put_sub_frame,
        text='PutObject',
        command=lambda: s3ope.s3_put_object()
    )

    get_sub_frame = ttk.Frame(root_sub_window, padding=16)
    s3_get_label = ttk.Label(get_sub_frame, text='S3バケット検索')
    str = StringVar()
    s3_get_entry = ttk.Entry(get_sub_frame, textvariable=str)
    get_button = ttk.Button(
        get_sub_frame,
        text='GetObject',
        command=lambda: s3ope.s3_get_object()
    )

    delete_sub_frame = ttk.Frame(root_sub_window, padding=16)
    s3_delete_label = ttk.Label(delete_sub_frame, text='S3バケット検索')
    str = StringVar()
    s3_delete_entry = ttk.Entry(delete_sub_frame, textvariable=str)
    s3_delete_button = ttk.Button(
        delete_sub_frame,
        text='DeleteObject',
        command=lambda: s3ope.s3_delete_object()
    )

    # 更新
    put_sub_frame.pack(fill="x")
    s3_put_label.pack(side=LEFT)
    s3_put_entry.pack(side=LEFT)
    put_button.pack(side=LEFT)
    # 取得
    get_sub_frame.pack(fill="x")
    s3_get_label.pack(side=LEFT)
    s3_get_entry.pack(side=LEFT)
    get_button.pack(side=LEFT)
    # 削除
    delete_sub_frame.pack(fill="x")
    s3_delete_label.pack(side=LEFT)
    s3_delete_entry.pack(side=LEFT)
    s3_delete_button.pack(side=LEFT)

# 初期画面
root_window = Tk()
root_window.title('AWS S3 CRUD')
root_window.geometry("400x100")
root_frame = ttk.Frame(root_window, padding=30)
t = StringVar()
root_button = ttk.Button(
    root_frame,
    text='START',
    command=lambda: sub_window()
)

# 初期画面のウィジェット配置
root_frame.pack()
root_button.pack()

root_window.mainloop()
def outer_func():
    print('外側の関数')

    def inner_func():
        print('内側の関数')

    return inner_func()

outer_func()

def test_function():
    inner_function()
    def inner_function():
        def second_test():
            print("Я в области видимости функции test_function")

inner_function()
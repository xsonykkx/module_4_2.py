def test_function():
    def inner_function():
        inner_function()
        print("Я в области видимости функции test_function")

test_function()

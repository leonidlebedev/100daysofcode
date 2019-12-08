from hello import get_hello

def test_hello_name():
    assert get_hello('L') == 'Hello, L'
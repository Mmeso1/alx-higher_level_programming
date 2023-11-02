#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4.pyc

    module = dir(hidden_4.pyc)

    for name in module:
        if not name.startswith('__'):
            print(name)

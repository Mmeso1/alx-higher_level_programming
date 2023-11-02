#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    module = dir(hidden_4)

    for name in module:
        if not name.startswith('__'):
            print(name)

def modern_print(s):
    if s not in output:
        print(s)
        output.add(s)


output = set()
if __name__ == '__main__':
    modern_print("Hello!")
    modern_print("Hello!")
    modern_print("How do you do?")
    modern_print("Hello!")

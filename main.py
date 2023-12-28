import pyperclip

first = True
prompt = "Please input the string you want to convert...\n" \
         "examples: \"E hello\", \"d \\u1234\"...\n\n"

def copy_to_clipboard(s):
    pyperclip.copy(s)
    print("Copied successfully!")

def encode(s):
    return s.encode('unicode-escape').decode()

def decode(s):
    return s.encode().decode('unicode-escape')

def run():
    global first
    s = ""
    if(first):
        s = input(prompt)
    else:
        s = input("Continue...\n")
    temp = s.split(" ")
    if not len(temp) == 2:
        print("Invalid input!")
        return
    mode, text = temp[0], temp[1]
    result = ""
    if mode == 'e' or mode == "E":
        result = encode(text)
    if mode == 'd' or mode == 'D':
        result = decode(text)
    print(result)
    copy_to_clipboard(result)
    first = False
def main():
    while True:
        run()


if __name__ == "__main__":
    main()

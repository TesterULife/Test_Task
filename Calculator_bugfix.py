def main(input: str):
    chars = []
    current = ""
    symb = 0

    for char in input:
        if char.isdigit():
            current += char
        else:
            if current:
                chars.append(int(current))
                current = ""
    if current:
        chars.append(int(current))

    for i in input:
        if i in "+-*/":
            symb += 1

    if len(chars) != 2 or symb != 1:
        return "throws Exception"

    a, b = chars[0], chars[1]

    if not (1 <= a <= 10 and 1 <= b <= 10):
        return "throws Exception"

    if "+" in input:
        result = a + b
    elif "-" in input:
        result = a - b
    elif "*" in input:
        result = a * b
    elif "/" in input:
        if a == 0 or b == 0:
            return "throws Exception"
        result = a // b

    return str(result)

while True:
    user_input = input()
    result = main(user_input)
    if user_input == "exit":
        break
    elif result == "throws Exception":
        print("throws Exception")
        break
    else:
        print(result)
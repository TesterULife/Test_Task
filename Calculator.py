def main(input: str):
    chars = []
    current = ""

    for char in input:
        if char.isdigit():
            current += char
        else:
            if current:
                chars.append(int(current))
                current = ""
    if current:
        chars.append(int(current))
    if len(chars) != 2:
        return "throws Exception"

    a, b = chars[0], chars[1]

    for num in chars:
        if num >= 1 and num <= 10:
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
            else:
                return "throws Exception"
        else:
            return "throws Exception"

    return str(result)

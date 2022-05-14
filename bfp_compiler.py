"""
    bfPlus Compiler - by poklop

    Just basic bf, but with some
    more features.
    Read README for help.

"""

def bf(code):
    arr = [0]
    pointerPos = 0
    i = 0
    ob = 0
    while i < len(code):
        if code[i] == "<":
            if pointerPos > 0:
                pointerPos -= 1
        elif code[i] == ">":
            pointerPos += 1
            if pointerPos >= len(arr):
                arr.append(0)
        elif code[i] == "+":
            arr[pointerPos] += 1
        elif code[i] == "-":
            arr[pointerPos] -= 1
        elif code[i] == ".":
            print(arr[pointerPos], chr(arr[pointerPos]))
        elif code[i] == ",":
            inp = input("> ")
            try:
                np = int(inp)
            except ValueError:
                np = ord(inp)
            arr[pointerPos] = np
        elif code[i] == "*":
            try:
                mv = int(code[i + 1])
                pointerPos += mv
                print(mv, pointerPos)
            except ValueError:
                print(f"error (pos {pointerPos}): missing number after *")
        elif code[i] == "[":
            if arr[pointerPos] == 0:
                ob = 1
                while ob > 0:
                    i += 1
                    if code[i] == "[":
                        ob += 1
                    elif code[i] == "]":
                        ob -= 1
        elif code[i] == "]":
            ob = 1
            while ob > 0:
                i -= 1
                if code[i] == "[":
                    ob -= 1
                elif code[i] == "]":
                    ob += 1
            i -= 1
        
        i += 1

bf("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>------------.<+++++++++++.")

"""
    bf+ Compiler - by Prokop Schovanec

    Just basic bf, but with some
    more features.
    Read README for help.

"""

import sys

def bf(code):
    arr = [0]
    pointerPos = 0
    maxInt = 4
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
            print(pointerPos, arr[pointerPos], chr(arr[pointerPos]))

        elif code[i] == ",":
            inp = input("> ")
            try:
                np = int(inp)
            except ValueError:
                np = ord(inp)
            arr[pointerPos] = np

        elif code[i] == "*":
            plMov = ""
            for n in range(maxInt):
                try:
                    num = int(code[i + n])
                    plMov += str(num)
                except ValueError:
                    pass
            pointerPos += int(plMov)
            if pointerPos >= len(arr):
                for n in range(int(plMov)):
                    arr.append(0)

        elif code[i] == "@":
            plNum = ""
            for n in range(maxInt):
                try:
                    num = int(code[i + n])
                    plNum += str(num)
                except ValueError:
                    pass
            arr[pointerPos] = int(plNum)

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

#bf("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>------------.<+++++++++++.")
#bf(">++++++++++[<+++++++>-]<.")
#bf(">,[>,]<[<]>[.>]")
#bf("@72.@69.@76.@76.@79.")
#bf("*777.")

if __name__ == "__main__":
    try:
        bfCode = str(sys.argv[1])
        bf(bfCode)
    except IndexError:
        print("no args")
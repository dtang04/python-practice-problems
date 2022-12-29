# Be-a-Computer: Recursion

In the following exercises, you will be shown a piece of code, and will have to figure out what it does (without running it yourself in the Python interpreter)


## Exercise #1

What is the output of the following code?

    def mystery(a, b, c, d):
        if c == 0:
            return d
        elif c % 2 == 0:
            return b + mystery(a, b, c - 2, d)
        else:
            return a + mystery(a, b, c - 1, d)

    print("Result:")
    print(mystery("x", "y", 6, "z"))
    print(mystery("x", "y", 5, "z"))
    print()

mystery("x","y",6,"z"):
    a = "x", b = "y", c = 6, d = "z"
    c = 6 -> 6 % 2 == 0
        return "y" + mystery("x","y",4,"z")
        mystery("x","y",4,"z"):
            a = "x", b = "y", c = 4, d = "z"
            c = 4 -> 4 % 2 == 0
                return "y" + mystery("x","y",2,"z")
                mystery("x","y",2,"z"):
                    a = "x", b = "y", c = 2, d = "z"
                    c = 4 -> 4 % 2 == 0
                        return "y" + mystery("x","y",0,"z")
                        mystery("x","y",0,"z"):
                            a = "x", b = "y", c = 0, d = "z"
                                c = 0 == 0
                        return "z"
                return "yz"
        return "yyz"
return "yyyz
Output: "yyyz"

mystery("x", "y", 5, "z"):
    a = "x", b = "y", c = 5, d = "z"
    c = 5 -> 5 % 2 != 0
        return "x" + mystery("x","y", 4, "z")
        mystery("x","y", 4, "z")
            a = "x", b = "y", c = 4, d = "z"
            c = 4 -> 4 % 2 == 0
                return "y" + mystery("x","y",2,"z")
                mystery("x","y",2, "z")
                    a = "x", b = "y", c = 2, d = "z"
                    c = 2 -> 2 % 2 = 0
                        return "y" + mystery("x","y",0,"z")
                        mystery("x","y",0,"z")
                            a = "x", b = "y", c = 0, d = "z"
                            c = 0 == 0
                        return "z"
                return "yz"
        return "yyz"
return "xyyz"
Output = "xyyz"


## Exercise #2

What is the output of the following code?

    def flip(s, a):
        if a == 0:
            return s
        for i in range(a):
            if s[i] == "*":
                s[i] = "-"
            else:
                s[i] = "*"
        return flip(s, a//2)

    print("Result:")
    s = []
    for i in range(64):
        s.append("*")
    s = flip(s, 64)
    t = ""
    for c in s:
        t = t + c
    print(t)

flip(["*"]*64,64)
    s = ["*"]*64, a = 64
    return flip(["-"]*64, 32)
        s = ["-"]*64, a = 32
        return flip(["*"]*32 + ["-"]*32, 16)
            s = ["*"]*32+["-"]*32, a = 16
            return flip(["-"]*16+["*"]*16+["-"]*32,8)
                s = ["-"]*16+["*"]*16+["-"]*32, a = 8
                    return flip(["*"]*8+["-"]*8+["*"]*16+["-"]*32,4)
                        s = ["*"]*8+["-"]*8+["*"]*16+["-"]*32, a = 4
                            return flip(["-"]*4+["*"]*4+["-"]*8+["*"]*16+["-"]*32,2)
                                s = ["-"]*4+["*"]*4+["-"]*8+["*"]*16+["-"]*32, a = 2
                                    return flip(["*"]*2+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32,1)
                                        s = ["*"]*2+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32, a = 1
                                            return flip(["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32, 0)
                                                s = ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32, a = 0
                                                return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
                                    return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
                            return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
                    return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
            return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
        return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
    return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32
return ["-"]*1+["*"]*1+["-"]*2+["*"]*4+["-"]*8+["*"]*16+["-"]*32

t = "-*--****--------****************--------------------------------"

Output: "-*--****--------****************--------------------------------"                           




## Exercise #3

What is the output of the following code?

    def mystery2(N):
        if N < 1:
            return
        mystery2(N-1)
        print(N)
        mystery2(N-2)

    print("Result:")
    mystery2(4)

## Exercise #4

This exercise is a bit more challenging than the previous ones. What is the output of the following code?

    def mystery3(s, c, d, x):
        if s == "":
            return x
        elif s[0] == c:
            return mystery3(s[1:], c, d, x+1)
        elif s[0] == d:
            if x > 0:
                return mystery3(s[1:], c, d, x-1)        
            return -1
        else:
            return mystery3(s[1:], c, d, x)


    def recursion_warmup():
        output_str = 'mystery3("{}", "a", "b", 0): {}'
        for s in ["ab", "abab", "abaab", "ababb", "ababaa"]:
            print(output_str.format(s,  mystery3(s, "a", "b", 0)))

    print("Result:")
    recursion_warmup()
'''
Scanner module of the Simple JAVA Compiler
Author:             Iron-Legion@GCOEJ
Date:               30 AUGUST 2021
'''
import os
import sys
import json
import Omegalib.Preprocessor as pc

# Python Keyword
keywords = [
    "import", "from", "if", "else", "for", "while", "def", "return", "elif", "as", "and", "or", "not", "in", "break", "continue", "True", "False", "try", "except", "with", "class", "pass", "finally", "None", "assert", "async", "await", "del", "global", "is", "lambda", "nonlocal", "raise", "yeild"
]

# Python special characters
symbols = [
    "(", ")", "[", "]", "{", "}", ",", ":", "@", "."
]

operators = [
    "+", "-", "*", "/", "%", "=", ">", "<", "&", "|", "~", "^", "!"
]

# Function to handle indents


def manage_indent(indent, lines, ind7):
    for i in range(ind7, len(lines)):
        leading_spaces = len(lines[i]) - len(lines[i].lstrip())
        if leading_spaces > 0 and ("'''" not in lines[i] and '"""' not in lines[i]):
            lines[i] = "\t"*(leading_spaces//indent)+lines[i][leading_spaces:]

    return lines


def char_token(x):
    if x in keywords:
        token = (x, "KEYWORD")
    elif x[0] == "'" or x[0] == '"':
        token = (x, "STRING")
    elif x.replace(" ", "").isdecimal():
        token = (x, "INT")
    else:
        token = (x, "IDENTIFIER")
    return token


def solve_puzzled(x, tokens):
    k = 0
    l = []
    lenx = len(x)
    while(k < lenx):
        if x[k] == '"' or x[k] == "'":
            try:
                ind0 = x[k+1:].index(x[k])
            except:
                #print("Error in " + x[k:])
                pass
            tokens.append((x[k+1:k + ind0+1], "STRING"))
            k = k + ind0 + 2
        elif x[k] in operators:
            s = "".join(l)
            if s != "":
                tokens.append((s, "IDENTIFIER"))
                try:
                    del s
                    l = []
                except:
                    l = []
            if k + 1 < len(x):
                if x[k+1] in operators:
                    if k + 2 < len(x):
                        if x[k+2] in operators:
                            token = (x[k:k+3], "SYMBOL")
                            k = k + 3
                        else:
                            token = (x[k:k+2], "SYMBOL")
                            k = k + 2
                    else:
                        token = (x[k:k+2], "SYMBOL")
                        k = k + 2

                else:
                    token = (x[k], "SYMBOL")
                    k = k + 1

            else:
                token = (x[k], "SYMBOL")
                k = k + 1
            tokens.append(token)
        else:
            if x[k] in symbols:
                s = "".join(l)
                if x[k] == ".":
                    if x[k+1].isdecimal():
                        u = k + 1
                        while 1:
                            try:
                                if x[u].isdecimal():
                                    u = u + 1
                                else:
                                    break
                            except:
                                break
                        if s.isdecimal():
                            token = (s+x[k:u], "FLOAT")
                            tokens.append(token)
                            k = u
                        else:
                            token = (s, "IDENTIFIER")
                            tokens.append(token)
                            tokens.append((".", "SYMBOL"))
                            k = k + 2
                    elif x[k] == ":":
                        tokens.append((x[k], "SYMBOL"))
                        k = k + 1
                    else:
                        lo = x.split(".")
                        lu = []
                        i1 = 0
                        while i1 < len(lo):
                            if lo[i1][-1] in '0123456789':
                                lu.append(lo[i1] + "." + lo[i1+1])
                                i1 += 1
                                # print(lu[-1])
                            elif lo[i1][0] in '0123456789':
                                lu[-1] = lu[-1]+lo[i1]
                            else:
                                lu.append(lo[i1])
                            i1 += 1
                        mnt = 1
                        for g in lu:
                            if g.isalnum():
                                token = char_token(g)
                                tokens.append(token)
                            else:
                                solve_puzzled(g, tokens)
                            if mnt < len(lo):
                                tokens.append((".", "SYMBOL"))
                            mnt = mnt + 1

                        break
                else:
                    if s.isalpha() or s.isalnum():
                        token = char_token(s)
                        tokens.append(token)
                    else:
                        if s != "":
                            tokens.append((s, "IDENTIFIER"))
                    tokens.append((x[k], "SYMBOL"))
                    try:
                        del s
                        l = []
                        k = k + 1
                    except:
                        l = []
                        k = k + 1
            else:
                l.append(x[k])
                k = k + 1
    else:
        s = "".join(l)
        if s == "True" or s == "False":
            tokens.append((s, "BOOL"))
        elif s != "":
            tokens.append((s, "IDENTIFIER"))

# Function to generate tokens


def generate_tokens(words):
    tokens = []
    for x in words:
        if x[0] == "\t":
            leading_spaces = len(x) - len(x.lstrip())
            tokens.append((x[:leading_spaces], "INDENT"))
            x = x[leading_spaces:]

        if x.isalpha():
            token = char_token(x)
            tokens.append(token)
        elif x in symbols:
            token = (x, "SYMBOL")
            tokens.append(token)
        elif x.isalnum():
            if all([v in "0123456789 " for v in x]):
                if x.isdecimal():
                    token = (x, "INT")
                elif x.replace(" ", "").isdecimal():
                    token = (x, "INT")
            else:
                token = (x, "IDENTIFIER")
            tokens.append(token)
        else:
            solve_puzzled(x, tokens)
    return tokens


def main(src_file):
    # Pre-Process the file
    lines = pc.pre_process_file(src_file)
    # Manage Indentation
    for x in lines:
        leading_spaces = len(x) - len(x.lstrip())
        if leading_spaces > 0:
            line1 = x
            ind7 = lines.index(x)
            break

        if leading_spaces > 0:
            lines = manage_indent(leading_spaces, lines, ind7)

        # Eliminate space
        words = [y for x in lines for y in x.split(" ")]

        # Handle Spaces eliminated from string values or parameters e.g: print("Hello World")
        i = 0
        while True:
            if i == len(words):
                break
            try:
                ind_w = words[i].index('"')
                try:
                    ind_w1 = words[i][ind_w+1:].index('"')
                    i += 1
                except:
                    words[i] = words[i] + " " + words[i+1]
                    words.remove(words[i+1])
            except:
                try:
                    ind_w = words[i].index("'")
                    try:
                        ind_w1 = words[i][ind_w+1:].index("'")
                        i += 1
                    except:
                        words[i] = words[i] + " " + words[i+1]
                        words.remove(words[i+1])
                except:
                    i += 1

        # handle indentations
        words = [x for x in words if x != "" and x not in [
            "\t"*i for i in range(1, 21)]]

        # generate tokens using words
        try:
            tokens = generate_tokens(words)
            f = open("SymbolTableManager.json", "w")
            json_object = json.dumps(
                {"tokens": tokens, "f": src_file}, indent=4)
            f.write(json_object)
            f.close()
        except:
            pass

'''
Preprocessor module of the Simple JAVA Compiler
Author:             Iron-Legion@GCOEJ
Date:               11 OCTOBER 2021
'''

import os

# Eliminate prefixes from called methods.
# E.g.: module_name.method(list_of_args) => method(list_of_args)
def eliminate_prefix(lines, final_modules):
    for module in final_modules:
        i = 0
        while True:
            if i == len(lines):
                break
            elif module in lines[i]:
                line = lines[i].split(module)
                lines[i] = line[0] + line[1][1:]
                i += 1
            else:
                i += 1
    return lines

# Arrange lines in order
def get_Ordered(lines):
    starter = []
    i = 0
    while True:
        if i == len(lines):
            break
        elif "import" in lines[i]:
            starter.append(lines[i])
            lines.remove(lines[i])
        else:
            i += 1
    return starter + lines

#Function to remove single line comment
def pre_process(x):
    while True:
        try:
            ind = x.index('#')
            return x[:ind].replace("\n","")

        except:
            return x.replace("\n","")

# Function remove multiline comments
def remove_multiline(lines):
    opening, l, flag = 0, 0, 0
    while True:
        try:
            ind8 = lines[l].index('"""')
            lines[l] = lines[l][:ind8]
            flag = 1
            opening += 1
            if opening==2:
                flag = opening
                opening = 0
                lines.remove(lines[l])
                continue
            l += 1
        except:
            try:
                ind8 = lines[l].index("'''")
                lines[l] = lines[l][:ind8]
                flag = 1
                opening += 1
                if opening==2:
                    flag = opening
                    opening = 0
                    lines.remove(lines[l])
                    continue
                l += 1
            except:
                if flag==1:
                    lines.remove(lines[l])
                elif flag == 2 or flag == 0:
                    l += 1
        if l == len(lines):
            break
    return lines

# Handle multiple user-defined imported libraries
def importAllFiles(lines,f_path):
    #Eliminate single line comments and empty lines
    lines = [pre_process(line) for line in lines if line != "\n" and line != "\t"]

    # Remove mutiline comments
    lines = remove_multiline(lines)

    # Check for imported libraries in root folder
    x = 0
    final_modules = []
    while True:
        try:
            ind16 = lines[x].index("import")
            # If user defined library exist, replace the import statement
            # with the code from the file
            # modules can be , separated
            modules = lines[x][ind16 + 7:].split(",")
            if os.path.exists(f_path+modules[0].replace(" ","")+".py"):
                lines.remove(lines[x])
            for module in modules:
                if os.path.exists(f_path+module.replace(" ","")+".py"):
                    final_modules.append(module)
                    f = open(f_path+module.replace(" ","")+".py","r")
                    insertlines = f.readlines()
                    f.close()
                    lines = lines[:x] + insertlines + lines[x:]

                    # Remove Comments
                    lines = [pre_process(line) for line in lines if line != "\n" and line != "\t"]
                    lines = remove_multiline(lines)
                else:
                    x += 1
                    break
        except:
            x += 1
        if x == len(lines):
            break
    return lines, final_modules

# Preprocess the file
def pre_process_file(f_path):
    f = open("./"+f_path.lower()+"/lib/main.py","r")
    lines = f.readlines()
    f.close()
    lines, final_modules = importAllFiles(lines,"\\".join(f_path.split("\\")[:-1])+"\\")
    #print(final_modules)
    lines = get_Ordered(lines)
    lines = eliminate_prefix(lines, final_modules)
    return lines

#print(pre_process_file("..\\..\\test\\main.py"))
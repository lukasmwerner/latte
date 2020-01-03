import os
import glob
import sys

if len(sys.argv) == 2 and (".latte" in sys.argv[1] or ".lt" in sys.argv[1]):
    fileName = sys.argv[1]
    fileNameClean = sys.argv[1].replace(".latte", "").replace(".lt", "").replace(".\\", "")

    lines = []

    print("[LATTE COMPILER] RUNNING TRANSPILE")
    with open(fileName, 'r') as f:
        content = f.readlines()
        for line in content:
            lines.append(line)

    if "main" in lines[0]:
        lines.insert(0, "public class " + fileNameClean + "{ \n")
        lines.insert(len(lines)-1, "}")

    

    x = 0
    for line in lines:
        i = 0
        oLine = list(line)
        for char in line:
            if char == "\n" and "{" not in line and "}" not in line and "if" not in line and "for" not in line:
                oLine[i] = ";\n"
            i+=1
        lines[x] = "".join(oLine)
        lines[x] = lines[x].replace("print", "System.out.println")

        x+=1
    with open(fileName.replace(".latte", ".java").replace(".lt", ".java"), 'w') as f:
        for line in lines:
            f.write(line)
    print("[LATTE COMPILER] RUNNING COMPILE")
    os.system("javac " + fileName.replace(".latte", ".java").replace(".lt", ".java"))
    print("[LATTE COMPILER] RUNNING JAVA CLASS")
    os.system("java " + fileName.replace(".latte", "").replace(".lt", "").replace(".\\", ""))
import os, sys

path = "."

for file in os.listdir(path):
    if file.endswith(".txt"):

        dblines = []
        nuclines = []
        headers = []
        loops = [] # dots
        stems = [] # brackets

        f = open(file, "r")
        for line in f:
            if line.startswith(">"):
                headers.append(line)
            elif "." in line:
                dblines.append(line)
            else:
                nuclines.append(line)

        f.close()

        for i in range(len(lines[0])):
            curr = dblines[0][i]
            found = True
            for j in range(len(lines)):
                if dblines[j][i] in curr:
                    found = True
                else:
                    found = False
                    break

            if found:
                if dblines[j][i] in ".":
                    loops.append(curr)
                elif dblines[j][i] in "\n":
                    loops.append(curr)
                    stems.append(curr)
                else:
                    stems.append(curr)

        floop = open(file.replace(".txt","_loop.txt"), "w")
        fstem = open(file.replace(".txt","_stem.txt"), "w")

        for k in range(1,len(headers)):
            floop.write(headers[k])
            fstem.write(headers[k])
            floop.write(loops[k])
            fstem.write(stems[k])
            
        floop.close()
        fstem.close()
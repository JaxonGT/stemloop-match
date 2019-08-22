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

        for n in range(len(dblines)):
            loops.append("")
            stems.append("")

        for i in range(len(dblines[0])):
            # reference character
            # all chars in same alignment pos should be equivalent
            curr = dblines[0][i]

            if "-" in curr:
                # ignore dashes
                continue

            found = True
            for j in range(len(dblines)):
                if dblines[j][i] in curr:
                    found = True
                else:
                    # different char found
                    # quit searching alignment pos
                    found = False
                    break

            if found:
                for k in range(len(dblines)):
                    nuc = nuclines[k][i]
                    if dblines[k][i] in ".":
                        loops[k] = loops[k] + nuc
                    elif dblines[j][i] in "\n":
                        loops[k] = loops[k] + nuc
                        stems[k] = stems[k] + nuc
                    else:
                        stems[k] = stems[k] + nuc

        floop = open(file.replace(".txt","_loop.txt"), "w")
        fstem = open(file.replace(".txt","_stem.txt"), "w")

        for k in range(len(headers)):
            floop.write(headers[k])
            fstem.write(headers[k])
            floop.write(loops[k])
            fstem.write(stems[k])
            
        floop.close()
        fstem.close()
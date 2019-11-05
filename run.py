file = open("../../Downloads/korean-single-speaker-speech-dataset/transcript.v.1.3.txt", 'r')
jsonfile = open("./dataset.json", 'w')

L = []
while (1):
    line = file.readline()

    try:
        escape = line.index('\n')
    except:
        escape = len(line)

    if line:
        L.append(line[0:escape])
    else:
        break

file.close()
jsonfile.write("{\n")
for idx in range(len(L)):
    filelocation = L[idx][0:2]
    filename = L[idx][2:12]
    L[idx] = L[idx][13:]
    orlocation = L[idx].find('|')
    L[idx] = L[idx][:orlocation]

    to_save = ("\t\"./datasets/korean-speech/" + filelocation + filename + "\": " + "\"" + L[idx] + "\",\n")
    jsonfile.write(to_save)
jsonfile.write("}")
jsonfile.close()
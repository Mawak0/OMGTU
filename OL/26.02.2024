f = open("temp", "r")
lines = [s.strip() for s in f.readlines()]


magic = ""
parts_of_magic = []
for line in lines:
    comps = line.split(" ")
    for comp in comps:
        try:
            a = int(comp)
            line = line.replace(" "+comp, " _"+comp+"_ ", 1)
        except:
            pass
    if "MIX" in line:
        s = line.replace("MIX", "").replace(" ", "")
        s = "MX"+s+"XM"
        parts_of_magic.append(s)
    if "WATER" in line:
        s = line.replace("WATER", "").replace(" ", "")
        s = "WT" + s + "TW"
        parts_of_magic.append(s)
    if "DUST" in line:
        s = line.replace("DUST", "").replace(" ", "")
        s = "DT" + s + "TD"
        parts_of_magic.append(s)
    if "FIRE" in line:
        s = line.replace("FIRE", "").replace(" ", "")
        s = "FR" + s + "RF"
        parts_of_magic.append(s)


for i in range(len(parts_of_magic), 1, -1):
    while "_" in parts_of_magic[i-1]:
        num = int(parts_of_magic[i-1].split("_")[1])
        parts_of_magic[i-1] = parts_of_magic[i-1].replace("_"+str(num)+"_", parts_of_magic[num-1])

print(parts_of_magic[-1])

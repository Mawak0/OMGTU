stri = ""
persons = dict() #[id: [name, [sub1id, sub2id]]]


path = "D:/A/code/C#/OMGTU/temp.txt"
f = open(path, "r")


while True:
    stri = f.readline().strip()
    if stri == "END":
        break
    if len(stri.split(" ")) == 1:
        xid = int(stri)
        name = None
    elif len(stri.split(" ")) > 1:
        s = stri.split(" ", 1)
        xid = int(s[0])
        name = s[1]
    boss_xid = xid
    if xid not in persons.keys():
        persons.update({xid: [None, []]})
    if name != None:
        persons[xid][0] = name

    stri = f.readline().strip()
    if stri == "END":
        break
    if len(stri.split(" ")) == 1:
        xid = int(stri)
        name = None
    elif len(stri.split(" ")) > 1:
        s = stri.split(" ", 1)
        xid = int(s[0])
        name = s[1]
    if xid not in persons.keys():
        persons.update({xid: [None, []]})
    if name != None:
        persons[xid][0] = name
    persons[boss_xid][1].append(xid)


need_boss = f.readline().strip()
need_boss_id = -1
need_boss_name = -1
try:
    need_boss_id = int(need_boss)
except:
    need_boss_name = need_boss

if need_boss_id == -1:
    for e in persons.items():
        if e[1][0] == need_boss_name:
            need_boss_id = e[0]

subs = []
newlen = len(subs)
oldlen = -1

subs += persons[need_boss_id][1]

while oldlen != newlen:
    oldlen = newlen
    for sub in subs:
        subs += persons[sub][1]
    subs = list(set(subs))
    newlen = len(subs)

subs.sort()

for sub in subs:
    name = persons[sub][0]
    if name == None:
        name = "Unknown Name"
    substr = str(sub)
    while len(substr) != 4:
        substr = "0"+substr
    print(substr, name)

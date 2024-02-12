stri = ""
persons = [] # [xid, name, subs] subs = [[xid1, name1], [xid2, name2], ...]


path = "temp"
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
    added = False
    for i in range(0, len(persons)):
        if persons[i][0] == xid:
            if name != None:
                persons[i][1] = name
            added = True
    if not added:
        persons.append([xid, name, []])

    stri = f.readline().strip()
    if len(stri.split(" ")) == 1:
        xid = int(stri)
        name = None
    elif len(stri.split(" ")) > 1:
        s = stri.split(" ", 1)
        xid = int(s[0])
        name = s[1]

    for i in range(0, len(persons)):
        if persons[i][0] == boss_xid:
            persons[i][2].append([xid, name])

need_boss = f.readline().strip()
need_boss_id = -1
need_boss_name = -1
try:
    need_boss_id = int(need_boss)
except:
    need_boss_name = need_boss


total_subs = []
total_subs_ids = []
boss = None
for p in persons:
    if p[0] == need_boss_id:
        boss = p
        break
    if p[1] == need_boss_name:
        boss = p
        break
total_subs += boss[2]
for s in total_subs:
    total_subs_ids.append(s[0])
old_len = len(total_subs)
new_len = old_len+1

while old_len != new_len:
    old_len = new_len
    for s in total_subs:
        for i in range(0, len(persons)):
            if persons[i][0] == s[0]:
                for sub in persons[i][2]:
                    if sub not in total_subs:
                        total_subs.append(sub)
                        total_subs_ids.append(sub[0])
    new_len = len(total_subs)


for xid in sorted(total_subs_ids):
    printed = False
    formated_xid = str(xid)
    while len(str(formated_xid)) != 4:
        formated_xid = "0"+formated_xid
    for q in range(0, len(total_subs)):
        if total_subs[q][0] == xid:
            if total_subs[q][1] != None:
                print(formated_xid, total_subs[q][1])
                printed = True
            else:
                for i in range(0, len(persons)):
                    if persons[i][0] == xid:
                        print(formated_xid, persons[i][1])
                        printed = True
            if not printed:
                print(formated_xid, "Unknown Name")



list = []
n = 4
for i in range(n):
    list.append(int(input("Enter adddress: ")))
segment1 = {100: 0, 500: 0, 200: 0, 300: 0, 600: 0}

for i in range(len(list)):
    for key in segment1:
        if segment1[key]==0 and list[i]<=key:
            segment1[key]=list[i]
            break

print(segment1)

segment = {100: 0, 500: 0, 200: 0, 300: 0, 600: 0}
for i in range(len(list)):
    best_key=float("inf")
    for key in segment:
        if segment[key]==0 and key>=list[i]:
            if key<best_key:
                best_key=key
    segment[best_key]=list[i]
print(segment)


segment3 ={100: 0, 500: 0, 200: 0, 300: 0, 600: 0}

for i in range(len(list)):
    worst_key=-1
    for key in segment3:
        if segment3[key]==0 and key>=list[i]:
            if key>worst_key:
                worst_key=key
    if worst_key!=-1:
        segment3[worst_key]=list[i]
print(segment3)
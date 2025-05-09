list = []
n = 4
for i in range(n):
    list.append(int(input("Enter adddress: ")))
segment = {100: 0, 500: 0, 200: 0, 300: 0, 600: 0}
#first fit
for i in range(len(list)):
    for key in segment:
        if segment[key] == 0 and key >= list[i]:
            segment[key] = list[i]
            break 
print('first fit',segment)

#best fit
segment = {100: 0, 500: 0, 200: 0, 300: 0, 600: 0}
for req in list:
    best_key = None
    best_size = float('inf')  

    for key in segment:
        if segment[key] == 0 and key >= req:
            if key < best_size:
                best_size = key
                best_key = key

    if best_key is not None:
        segment[best_key] = req
print('best fit',segment)

#worst fit
segment = {100: 0, 500: 0, 200: 0, 300: 0, 600: 0}
for req in list:
    worst_key = None
    worst_size = -1
    for key in segment:
        if segment[key] == 0 and key >= req:
            if key > worst_size:
                worst_size = key
                worst_key = key200
    if worst_key is not None:
        segment[worst_key] = req
print('Worst Fit:', segment)

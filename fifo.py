def fifo(pages, capacity):
    frame = []
    faults = 0
    hit=0
    for page in pages:
        if page in frame:
            print(f"Page {page} → HIT")
            hit+=1
        else:
            print(f"Page {page} → FAULT")
            if len(frame) == capacity:
                frame.pop(0)
            frame.append(page)
            faults += 1
    print("Total Page Faults:", faults)
    print("Total Page Hits:", hit)
    print("Frame:", frame)
    return faults

pages = [7, 0, 1, 2, 0, 3, 0, 4]
fifo(pages, 3)




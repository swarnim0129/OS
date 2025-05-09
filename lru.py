def lru(pages, capacity):
    frame = []
    faults = 0
    hits = 0

    for page in pages:
        if page not in frame:
            print(f"Page {page}: Fault")
            if len(frame) == capacity:
                frame.pop(0)
            faults += 1
        else:
            print(f"Page {page}: Hit")
            frame.remove(page)
            hits += 1
        frame.append(page)

    print(f"\nTotal Page Faults: {faults}")
    print(f"Total Page Hits: {hits}")
    print(frame)
    return faults

# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4]
lru(pages, 3)

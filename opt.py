def optimal(pages, capacity):
    frame = []
    faults = 0
    hit = 0

    for i in range(len(pages)):
        page = pages[i]
        if page in frame:
            print(f"Page {page} → HIT")
            hit += 1
        else:
            print(f"Page {page} → FAULT")
            if len(frame) < capacity:
                frame.append(page)
            else:
                # Find the page in the frame that won't be used for the longest time
                future_use = []
                for f in frame:
                    if f in pages[i+1:]:
                        next_use = pages[i+1:].index(f)
                        future_use.append(next_use)
                    else:
                        future_use.append(float('inf'))  # Not used again

                index_to_replace = future_use.index(max(future_use))
                frame[index_to_replace] = page
            faults += 1

    print("Total Page Faults:", faults)
    print("Total Page Hits:", hit)
    print("Frame:", frame)
    return faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4]
optimal(pages, 3)

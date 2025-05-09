def sjf(prs):
    total_waiting = 0
    total_turnaround = 0
    waiting = 0
    
    prs.sort(key = lambda x: x[1])
    
    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for p in prs:
        tat = waiting + p[1] 
        print(f"{p[0]}\t\t{p[1]}\t\t{waiting}\t\t{tat}")  # Process ID, Burst Time, Waiting Time, Turnaround Time
        total_waiting += waiting
        total_turnaround += tat
        waiting += p[1]
    
    avg_waiting = total_waiting / len(prs)
    avg_turnaround = total_turnaround / len(prs)
    
    print('\nAvg Waiting Time:', avg_waiting)
    print('Avg Turnaround Time:', avg_turnaround)

sjf([(1, 6), (2, 8), (3, 7), (4, 3)])








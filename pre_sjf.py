def preemptive_sjf(prs):
    n = len(prs)
    total_waiting = 0
    total_turnaround = 0
    
    prs.sort(key = lambda x: x[0])  
    
    remaining_burst = [p[1] for p in prs] 
    waiting = [0] * n 
    finish_time = [0] * n  
    
    time = 0  
    completed = 0  
    
    while completed < n:
        min_time = float('inf')
        idx = -1
        for i in range(n):
            if prs[i][0] <= time and remaining_burst[i] > 0 and remaining_burst[i] < min_time:
                min_time = remaining_burst[i]
                idx = i
        
        if idx != -1:
            remaining_burst[idx] -= 1
            time += 1
            
            if remaining_burst[idx] == 0:
                completed += 1
                finish_time[idx] = time
                waiting[idx] = finish_time[idx] - prs[idx][0] - prs[idx][1]
                total_waiting += waiting[idx]
                total_turnaround += waiting[idx] + prs[idx][1]
        else:
            time += 1  
    
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n
    
    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{prs[i][0]}\t\t{prs[i][1]}\t\t{waiting[i]}\t\t{waiting[i] + prs[i][1]}")
    
    print('\nAvg Waiting Time:', avg_waiting)
    print('Avg Turnaround Time:', avg_turnaround)

preemptive_sjf([(0, 6), (1, 8), (2, 7), (3, 3)])

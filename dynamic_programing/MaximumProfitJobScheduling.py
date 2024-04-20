def job_scheduling(start_time, end_time, profit):
    n = len(start_time)
    jobs = sorted(list(zip(start_time, end_time, profit)), key = lambda x: x[1])
    profit_table = [0] * n
    for current_job_index in range(n):
        current_job_profit = jobs[current_job_index][2]
        previous_job_profit = profit_table[current_job_index - 1] if current_job_index > 0 else 0
        previous_job_index = binary_search(current_job_index, jobs)
        if previous_job_index != -1:
            profit_table[current_job_index] = max(current_job_profit + profit_table[previous_job_index], previous_job_profit)
        else:
            profit_table[current_job_index] = max(current_job_profit, previous_job_profit)
    return profit_table[-1]
      

def binary_search(current_job_index, jobs):
    left = 0
    right = len(jobs) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if jobs[mid][1] <= jobs[current_job_index][0]:
            index = mid
            left = mid + 1
        else:
            right = mid - 1
    return index

      



# Driver Code
def main():
    start_times = [[1, 2, 3], 
                    [2, 4, 6, 8, 10],
                    [15, 20, 25, 30, 35],
                    [1, 4],
                    [2, 5, 1, 8, 3, 7, 6, 10, 4, 9]]
    end_times = [[3, 4, 5], 
                 [5, 7, 9, 11, 13],
                 [18, 23, 28, 33, 38],
                 [5, 7],
                 [7, 10, 4, 11, 6, 9, 8, 12, 5, 13]]

    profits = [[50, 10, 40],
               [40, 20, 50, 70, 30],
               [80, 60, 90, 110, 70],
               [1000, 3],
               [80, 50, 60, 90, 30, 70, 40, 100, 20, 110]]
  
    print("Input data for 'n' jobs")
    print("-" * 100)

    for i in range(len(start_times)):
        print(i+1, ".\tStart times: ", start_times[i])
        print("\tEnd times  : ", end_times[i])
        print("\tProfits    : ", profits[i])
        
        max_profit = job_scheduling(start_times[i], end_times[i], profits[i])
        
        print("\n\tMaximum profit: ", max_profit)
        print("-" * 100)

if __name__ == '__main__':
  main()
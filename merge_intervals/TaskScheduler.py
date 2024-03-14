
'''
Statement
We’re given a character array, tasks, where each character represents a unique task. These tasks need to be performed by a single CPU, with each task taking one unit of time. The tasks can be performed in any order. At any given time, a CPU can either perform some task or stay idle.
For the given tasks, we are also provided with a positive integer value, n, which represents the cooling period between any two identical tasks. This means that the CPU must wait for at least n units of time before it performs the same task again. For example, if we have the tasks
[A,B,A,C] and n = 2, then after performing the first
A task, the CPU will wait for at least 2 units of time to perform the second A task. During these 2 units of time, the CPU can either perform some other task or stay idle.
Given the two input values, tasks and n, find the least number of units of time the CPU will take to perform the given tasks.
'''
from collections import Counter

def least_time(tasks, n):
    c = Counter(tasks).most_common()
    cool_off_time = dict()
    max_freq = c.pop(0)[1]
    idle_time = (max_freq - 1) * n
    while c and idle_time > 0:
        idle_time -= min(max_freq -1, c.pop(0)[1])
    idle_time = max(0, idle_time)
    return len(tasks) + idle_time



# Driver code
def main():
    all_tasks = [['A', 'A', 'B', 'B'],
                  ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
                  ['S', 'I', 'V', 'U', 'W', 'D', 'U', 'X'],
                  ['M', 'A', 'B', 'M', 'A', 'A', 'Y', 'B', 'M'],
                  ['A', 'K', 'X', 'M', 'W', 'D', 'X', 'B', 'D', 'C', 'O', 'Z', 'D', 'E', 'Q'],
                  ["A","B","C","O","Q","C","Z","O","X","C","W","Q","Z","B","M","N","R","L","C","J"]]
    all_ns = [2, 1, 0, 3, 3, 10]

    for i in range(len(all_tasks)):
        print(i+1, '.', '\tTasks: ', all_tasks[i], sep='')
        print('\tn: ', all_ns[i], sep='')
        min_time = least_time(all_tasks[i], all_ns[i])
        print('\tMinimum time required to execute the tasks: ', min_time)
        print('-' * 100)

if __name__ == '__main__':
    main()
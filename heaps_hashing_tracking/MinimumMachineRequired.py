'''
We are given an input array, tasks, which contains the start and end times of tasks.
Your task is to find the minimum number of machines required to complete these n tasks.
'''
import heapq

def tasks(task_list):
    heapq.heapify(task_list)
    num_machine = 0
    list_of_machine  = []
    end_time = []
    while task_list:
        t = heapq.heappop(task_list)
        task_assigned = False
        if end_time:
            if end_time[0] <= t[0]:
                heapq.heapreplace(end_time, t[1])
            else:
                num_machine += 1
                heapq.heappush(end_time, t[1])
        else:
            num_machine += 1
            heapq.heappush(end_time, t[1])
    return num_machine


def main():

    input_tasks_list = [[(1, 1), (5, 5), (8, 8), (4, 4),
                        (6, 6), (10, 10), (7, 7)],
                        [(1, 7), (1, 7), (1, 7),
                        (1, 7), (1, 7), (1, 7)],
                        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
                        [(1, 3), (3, 5), (5, 9), (9, 12),
                        (12, 13), (13, 16), (16, 17)],
                        [(12, 13), (13, 15), (17, 20),
                        (13, 14), (19, 21), (18, 20)]]

    for i in range(len(input_tasks_list)):
        print(i + 1, ".\t Tasks = ", input_tasks_list[i], sep="")

        print("\t Optimal number of machines = ",
              tasks(input_tasks_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
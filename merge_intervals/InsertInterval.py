'''
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval into the correct position
while ensuring that the resulting list of intervals remains sorted and nonoverlapping.
Each interval is a pair of nonnegative numbers, the first being the start time and the second being the end time of the interval.
'''


def insert_interval(existing_intervals, new_interval):
    output = []
    new_interval_merged = False
    for interval in existing_intervals:
        if not new_interval_merged and interval[1] < new_interval[0]:
            output.append(interval)
        elif not new_interval_merged:
            output.append([min(interval[0], new_interval[0]), max(interval[1], new_interval[1])])
            new_interval_merged = True
        else:
            if output[-1][1] < interval[0]:
                output.append(interval)
            else:
                item = output.pop()
                output.append([min(item[0], interval[0]), max(item[1], interval[1])])
    if not new_interval_merged:
        output.append(new_interval)
    return output

# Driver code
def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]

    for i in range(len(new_interval)):
        print("Exiting intervals: ", existing_intervals[i], sep="")
        print("New interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print(f'After insertion: {output}')
        print("-"*100)


if __name__ == "__main__":
    main()
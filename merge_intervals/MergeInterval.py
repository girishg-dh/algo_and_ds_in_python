'''
We are given an array of closed intervals, intervals, where each interval has a start time and an end time. The input array is sorted with respect to the start times of each interval. For example, intervals =
[[1,4],[3,6],[7,9]]
[[1,4], [3,6], [7,9] ] is sorted in terms of start times 1, 3 and 7.
Your task is to merge the overlapping intervals and return a new output array consisting of only the non-overlapping intervals.
'''

def merge_intervals(intervals):
    output = [intervals[0]]
    for interval in intervals:
        if interval[0] > output[-1][1]:
            output.append(interval)
        else:
            item = output.pop()
            output.append([min(item[0], interval[0]), max(item[1], interval[1])])
    return output


def main():

    all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", result)
        print("-"*100)

if __name__ == '__main__':
    main()
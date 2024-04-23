
from sliding_windows.minimum_sliding_window import min_window
# Driver code
def main():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
              t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
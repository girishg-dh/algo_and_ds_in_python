from time_stamp import TimeStamp
import random

# Driver code
def main():
    ts = TimeStamp()
    num = 1
    random_value = 0
    input = (
            ("course", "OOP", 3),
            ("course", "PF", 5),
            ("course", "OS", 7),
            ("course", "ALGO", 9),
            ("course", "DB", 10)
        )

    for i in input:
        print(num, ".\tAdd value: (", '"', i[0], '"',
                   ", ", '"', i[1], '"', ", ", i[2], ")", sep="")
        ts.set_value(i[0], i[1], i[2])
        random_value = random.randint(0, 10)
        print("\n\tGet value for:")
        print("\t\tKey = course  \n\t\tTimestamp = ", random_value, sep="")
        print("\n\tReturned value = ", '"',
              ts.get_value("course", random_value), '"', sep="")
        num += 1
        print("-" * 100, sep="")
    ts.set_value("foo", "bar", 7)
    ts.set_value("foo", "baz", 9)
    print(ts.get_value("foo", 8))
    print(ts.get_value("foo", 9))

if __name__ == "__main__":
    main()
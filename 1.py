
def part1():

    num_zero = 0

    value = 50

    with open("input/1_1.txt") as f:
        for line in f:
            print(line.strip())

            num = int(line[1:])

            if line[0] == "R":
                value += num
            elif line[0] == "L":
                value -= num

            while value < 0:
                value += 100
            while value > 99:
                value -= 100

            print(f"Value: {value}")

            if value == 0:
                num_zero += 1
                
    print(f"\nNum zero: {num_zero}")


def part2():
    num_zero = 0

    value = 50

    with open("input/1_1.txt") as f:
        for line in f:
            print(line.strip())

            num = int(line[1:])

            passes = 0

            if line[0] == "R":
                passes = (value + num) // 100
                if passes:
                    print(f"Passes R: {passes}")
                num_zero += passes

                value = (value + num) % 100

            elif line[0] == "L":
                if value == 0:
                    passes = num // 100
                else:
                    if num < value:
                        passes = 0
                    else:
                        passes = 1 + (num - value) // 100

                if passes:
                    print(f"Passes L: {passes}")
                num_zero += passes

                value = (value - num) % 100

            print(f"Value: {value} Zeroes: {num_zero}\n")

                
    print(f"\nNum zero: {num_zero}")
    # 6312 too high

#part1()
part2()
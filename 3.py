

def part1():

    with open("input/3.txt") as f:
        

        total = 0

        for line in f:
            battery_bank = line.strip()

            max_j = 0

            for i, first in enumerate(battery_bank):

                first = int(first) * 10

                for second in battery_bank[i+1:]:
                    second = int(second)

                    if first + second > max_j:
                        max_j = first + second
            #print(max_j)
            total += max_j
        print(total)
            

def part2():

    with open("input/3.txt") as f:
        

        total = 0

        for line in f:
            battery_bank = line.strip()

            num_str = ""

            index = 0
            num_left = 10

            # Pick first digit
            max_val = 0
            for i, value in enumerate(battery_bank[:-num_left]):

                value = int(value)

                if value > max_val:
                    index = i   
                    max_val = value

            print(f"Start {max_val} at index {index}")

            num_str += str(max_val)
            max_val = 0

            for i in range(11):

                if num_left == 0:
                    num_left = -len(battery_bank)

                #print(index, num_left)
                #print(f"{index+1} to {-num_left}")
                #print(f"Nums to pick from: {battery_bank[index+1:-num_left]}  ")

                for i, value in enumerate(battery_bank[index+1:-num_left], start=index+1):

                    value = int(value)

                    if value > max_val:
                        index = i
                        max_val = value
            
                print(f"Next {max_val} at index {index}")
            
                num_left -= 1
                num_str += str(max_val)
                max_val = 0

            print(num_str, "\n")
            total += int(num_str)

        print(total)


part2()
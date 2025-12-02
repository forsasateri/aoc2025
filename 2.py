
def part1():
    with open("input/2.txt") as f:
        data = f.read().split(",")

        total = 0

        for d in data:
            print(d.strip())

            first, last = d.split("-")
            first = int(first)
            last = int(last)

            for num in range(first, last + 1):
                str_num = str(num)

                # Only care about even for split in two
                if len(str_num) % 2 != 0:
                    continue

                half_len = len(str_num) // 2

                if str_num[:half_len] != str_num[half_len:]:
                    continue

                print(f"Invalid: {str_num}")
                total += num

            print("\n")

        print(f"Total: {total}")


def part2():
    with open("input/2.txt") as f:
        data = f.read().split(",")

        total = 0

        for d in data:
            print(d.strip())

            first, last = d.split("-")
            first = int(first)
            last = int(last)

            for num in range(first, last + 1):
                str_num = str(num)



                for part_len in range(1, len(str_num)):

                    # Needs to fir x times precisely
                    if len(str_num) % part_len != 0:
                        continue

                    part = str_num[:part_len]
                    
                    match = True

                    for i, c in enumerate(str_num[part_len:]):
                        if c != part[i % part_len]:
                            match = False
                            break

                    if match:
                        print(f"Invalid: {str_num} Part: {part}")
                        total += num
                        break

                    


            print("\n")

        print(f"Total: {total}")


#part1()
part2() 
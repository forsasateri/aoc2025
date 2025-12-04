
def part1():

    matrix = []

    reachable = 0

    with open("input/4.txt") as f:
        for line in f:
            line = line.strip()
            matrix.append([c for c in line])

    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    

    for i, row in enumerate(matrix):
        for j, c in enumerate(row):

            if c == ".":
                continue

            neighbour_count = 0
            
            for di, dj in neighbours:
                ni, nj = i + di, j + dj

                if 0 <= ni < len(matrix) and 0 <= nj < len(row):
                    if matrix[ni][nj] == "@" or matrix[ni][nj] == "x":
                        neighbour_count += 1
            
            if neighbour_count < 4:
                reachable += 1
                matrix[i][j] = "x"
    print(reachable)

    for row in matrix:
        print("".join(row))



def part2():
    matrix = []

    reachable = 0

    with open("input/4.txt") as f:
        for line in f:
            line = line.strip()
            matrix.append([c for c in line])

    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    while True:

        old_reachable = reachable

        for i, row in enumerate(matrix):
            for j, c in enumerate(row):

                if c == ".":
                    continue

                if c == "x":
                    continue

                neighbour_count = 0
                
                for di, dj in neighbours:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < len(matrix) and 0 <= nj < len(row):
                        if matrix[ni][nj] == "@":
                            neighbour_count += 1
                
                if neighbour_count < 4:
                    reachable += 1
                    matrix[i][j] = "x"

        # Stop when no updates
        if old_reachable == reachable:
            break
        else:
            print(f"{old_reachable} -> {reachable}")
            print("Updates made, continuing...")

    for row in matrix:
        print("".join(row))
    print(reachable)


part2()
for in_file in ["A", "B"]:
    divisible_by_7 = 0
    not_divisible_by_7 = 0
    with open(in_file + ".txt") as f:
        while True:
            n = int(f.readline().strip())
            if n == 0:
                if divisible_by_7 and not_divisible_by_7:
                    print(divisible_by_7 * not_divisible_by_7)
                else:
                    print(1)
                break
            if n % 7 == 0:
                if n % 49 != 0:
                    divisible_by_7 = max(divisible_by_7, n)
            else:
                not_divisible_by_7 = max(not_divisible_by_7, n)

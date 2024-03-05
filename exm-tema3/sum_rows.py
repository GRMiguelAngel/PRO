# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    rsum = []
    with open(data_path, 'r') as file:
        for row in file:
            nums = []
            splitted_nums = row.strip().split(' ')
            for num in splitted_nums:
                nums.append(int(num))
            nums = sum(nums)
            rsum.append(nums)
        rsum = tuple(rsum)

    return rsum


if __name__ == '__main__':
    run('data/sum_rows/data1.txt')

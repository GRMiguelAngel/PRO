# *************************
# SIMULANDO EL COMANDO HEAD
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    lines = ''
    with open(file, 'r') as f:
        for nline, line in enumerate(f):
            if nline < n:
                lines += line
            else:
                break
        lines = lines.rstrip()
    return lines


if __name__ == '__main__':
    run('data/head/nba_season22.txt', 3)

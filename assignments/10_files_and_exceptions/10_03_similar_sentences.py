from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
for line in contents.splitlines():
    print(line)
for line in lines:
    print(line)
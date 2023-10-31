with open ('src\passwd') as f:
    lines = f.read().splitlines()

shells = {}
for line in lines:
    *_, shell = line.split(":")
    if shell not in shells:
        shells[shell] = 0
    shells[shell] += 1
for shell, count in shells.items():
    if len(shell.strip())> 0:
        print(f"{shell:20} : {count}")
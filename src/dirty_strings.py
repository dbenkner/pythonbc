DIRTY_STRINGS = [
    "  mud   ",
    "grime  ",
    "   filth    ",
    "     messy messy     ",
    "DIRT	",
    "       FILTH and grime    ",
    "Dirt",
    "   Filth,    dirt, grime,    grime, grime, filth, and mud      ",
]

def main():
    for old_string in DIRTY_STRINGS:
        new_string = cleanup(old_string)
        print(f"Before: >{old_string}<\nAfter:  >{new_string}<\n")

def cleanup(old_str):
    strArr = []
    strArr = old_str.split()
    new_str = ""
    for s in strArr:
        s.lower()
        s.strip
        new_str += s + " "
    return new_str

main()

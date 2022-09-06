def inatorInator(x):
    if x[-1] in "aeiou":
        return(f"{x}-inator {len(x)*1000}")
    else:
        return(f"{x}inator {len(x)*1000}")
print(inatorInator("Shrink"))
print(inatorInator("EvilClone"))
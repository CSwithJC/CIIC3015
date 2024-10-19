# Print Numbers 0 through 99 recursively.
def recursive_print_aux(i, n):
    if i == n:
        return
    print(i)
    recursive_print_aux(i + 1, n)

def recursive_print(n):
    recursive_print_aux(0, n)

recursive_print(100)
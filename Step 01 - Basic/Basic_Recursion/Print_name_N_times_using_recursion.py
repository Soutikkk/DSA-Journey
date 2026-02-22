

def print_name(N):
    if N == 0:
        return
    
    print("Soutik")
    print_name(N - 1)


print_name(100)

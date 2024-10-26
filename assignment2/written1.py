def permutations(n):
    permutationsList = []
    if n == 1: return [[1]]
   
    for i in range(n):
        for perm in permutations(n-1):
            perm.insert(i, n)
            permutationsList.append(perm)

    return permutationsList

def main():
    n = 5
    print(permutations(n))

if __name__ == "__main__":
    main()
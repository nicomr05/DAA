# Mixture algorithms
def MixtureDP (A:str|list, B:str|list, C:str|list)->bool:
    n = len(A)
    m = len(B)
    s = len(C)

    sol = ""

    if (n + m) != s:
        return False

    t = [[False for _ in range(m+1) ] for _ in range(n+1) ]
    t[0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            t[i][j] = t[max(0, i-1)][j] or t[i][max(0, j-1)]
            if t[i][j] and (i < n or j < m):
                k = i + j
                t[i][j] = False

                if i < n:
                    cond = A[i] == C[k]
                    t[i][j] = t[i][j] or cond
                    if cond:
                        sol += "A"

                if j < m:
                    cond = B[j] == C[k]
                    t[i][j] = t[i][j] or cond
                    if cond:
                        sol += "B"

    return sol


def MixtureCX(A:str|list, B:str|list, C:str|list) -> bool: 
    n = len(A)
    m = len(B)
    s = len(C)

    sol = ""

    if n + m != s:
        return False
    
    Known = {(0,0)} # Set
    Trial = [(0,0)] # Stack

    while len(Trial) > 0:
        (i,j) = Trial.pop()
        k = i + j

        if k >= s:
            return sol

        if i < n and A[i] == C[k] and (i+1,j) not in Known:
            sol += "A"
            Trial.append((i+1,j))
            Known.add((i+1,j))

        if j < m and B[j] == C[k] and (i,j+1) not in Known:
            sol += "B"
            Trial.append((i,j+1))
            Known.add((i,j+1))

    return False


if __name__ == "__main__":
    a = "Hello"
    b = "World"
    c = "WorHellold"

    print(MixtureCX(a,b,c))
    print(MixtureDP(a,b,c))
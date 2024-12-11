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
                    t[i][j] = t[i][j] or A[i] == C[k]

                if j < m:
                    t[i][j] = t[i][j] or B[j] == C[k]

    # TODO : Recorrer tabla hacia atrás desde el final
    for i in range(n,1,-1):
        for j in range(m,-1,-1):
            if t[i][j] :
                if B[j-1]==C[i+j-1]:
                    sol+="B"
                    continue
                if A[i-1]==C[i+j-1] :
                    sol+="A"
                    
                
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
    c = "HelloWorld"

    print(MixtureCX(a,b,c))
    print(MixtureDP(a,b,c))

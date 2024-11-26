def isMisxtureDP(A:str|list, B:str|list, C:str|list) -> list[list]:
    n = len(A)
    m = len(B)
    s = len(C)

    t = [[False for j in range(m + 1)] for i in range(n + 1)]


def isMixtureCX(A:str|list, B:str|list, C:str|list) -> None: 
    n = len(A)
    m = len(B)
    s = len(C)

    if n + m != s:
        return False
    
    Known = {(0,0)} # Set
    Trial = [(0,0)] # Stack

    while len(Trial) > 0:
        (i,j) = Trial[-1]
        Trial.pop(-1)
        k = i+j - 1

        if k > s:
            return True

        if i <= n and A[i] == C[k] and (i+1,j) not in Known:
            Trial = Trial.append((i+1,j));
            Known = Known.add((i+1,j));

        if j <= m and B[j] == C[k] and (i,j+1) not in Known:
            Trial = Trial.append((i,j+1));
            Known = Known.add((i,j+1));

    return False


if __name__ == "__main__":
    a = "Hello"
    b = "World"
    c = "HelloWorld"

    print(isMixtureCX(a,b,c))

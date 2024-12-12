#!env/bin/python


# Backtracking function
def Backtrack(T:list[list], n:int, m:int) -> str:
    '''
    Description
    -----------
    Searches for a valid path inside a table `T`.

    Parameters
    ----------
    T : `list[list]`
        Table in which to search.
    n : `int`
        Number of rows of T.
    m : `int`
        Number of columns of T.    

    Returns
    -------
    `str`
        Valid path inside the table 
    '''
    idx, jdx = -1
    while (idx, jdx) != (-n,-m): # TODO : Desbordamiento de la tabla por accesos a elementos fuera de ella
        if T[idx - 1][jdx]:
            idx += -1
            sol += "A"

        if T[idx][jdx - 1]:
            jdx += -1
            sol += "A"

    return sol


# Mixture algorithms
def MixtureDP (A:str|list, B:str|list, C:str|list)->bool:
    '''
    Description
    -----------
    Outputs a valid solution for mixing the strings A and B such that it forms
    a string C given via a Dynamic Programming algorithm.

    Parameters
    ----------
    A : `str|list`
        First string to mix.
    B : `str|list`
        Second string to mix.
    C : `str|list`
        Mixed string.
    
    Returns
    -------
    str
        String formed by As or Bs depending of which string it belonged to.
    '''
    n = len(A)
    m = len(B)
    s = len(C)

    sol = ""

    if (n + m) != s:
        return False

    T = [[False for _ in range(m+1) ] for _ in range(n+1) ]
    T[0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            T[i][j] = T[max(0, i-1)][j] or T[i][max(0, j-1)]
            if T[i][j] and (i < n or j < m):
                k = i + j
                T[i][j] = False

                if i < n:
                    T[i][j] = T[i][j] or A[i] == C[k]

                if j < m:
                    T[i][j] = T[i][j] or B[j] == C[k]

    return Backtrack(T, n, m)


def MixtureCX(A:str|list, B:str|list, C:str|list) -> bool:
    '''
    Description
    -----------
    Outputs a valid solution for mixing the strings A and B such that it forms
    a string C given via another algorithm.

    Parameters
    ----------
    A : `str|list`
        First string to mix.
    B : `str|list`
        Second string to mix.
    C : `str|list`
        Mixed string.
    
    Returns
    -------
    str
        String formed by As or Bs depending of which string it belonged to.
    '''
    n = len(A)
    m = len(B)
    s = len(C)

    T = [[False for _ in range(m+1) ] for _ in range(n+1) ]

    if n + m != s:
        return False
    
    Known = {(0,0)} # Set
    Trial = [(0,0)] # Stack

    while len(Trial) > 0:
        (i,j) = Trial.pop()
        k = i + j

        if k == s:
            return Backtrack(T, n, m) # Returns a valid path searching through the DP table 

        if i < n and A[i] == C[k] and (i+1, j) not in Known:
            Trial.append((i+1, j))
            Known.add((i+1, j))

        if j < m and B[j] == C[k] and (i, j+1) not in Known:
            Trial.append((i, j+1))
            Known.add((i, j+1))

    else:
        return False



if __name__ == "__main__":
    a = "aa"
    b = "aaa"
    c = "aaaaa"

    print(MixtureDP(a,b,c))
    print(MixtureCX(a,b,c))

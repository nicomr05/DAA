#!env/bin/python


# Backtracking function
def Backtrack(T:list[list]) -> str:
    '''
    Description
    -----------
    Searches for a valid path inside a table `T`.

    Parameters
    ----------
    T : `list[list]`
        Table in which to search.

    Returns
    -------
    `str`
        Valid path inside the table.
    '''
    n = len(T)
    m = len(T[0])

    sol = ""
    i, j = n-1, m-1

    while i > 0 or j > 0:

        if T[i-1][j] and i > 0:
            sol += "A"
            i -= 1

        if T[i][j-1] and j > 0:
            sol += "B"
            j -= 1

    return sol[::-1]


# Mixture algorithms
def MixtureDP (A:str|list, B:str|list, C:str|list) -> bool:
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

    return Backtrack(T)


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

    if n + m != s:
        return False
    
    Known = {(0,0)} # Set
    Trial = [(0,0)] # Stack
    Sol = ""

    while len(Trial) > 0:
        AddedA = False
        (i,j) = Trial.pop()
        k = i + j

        if k == s:
            return Sol


        if i < n and A[i] == C[k] and (i+1, j) not in Known:
            Trial.append((i+1, j))
            Known.add((i+1, j))
            Sol += "A"
            AddedA = True

        if j < m and B[j] == C[k] and (i, j+1) not in Known and not AddedA:
            Trial.append((i, j+1))
            Known.add((i, j+1))
            Sol += "B"

    else:
        return False



if __name__ == "__main__":
    a = "Hello"
    b = "World"
    c = "HWeolrllod"

    print(MixtureDP(a,b,c))
    print(MixtureCX(a,b,c))

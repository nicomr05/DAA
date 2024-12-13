#!env/bin/python


# Table backtracking function
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
        Valid path inside the table 
    '''
    n = len(T)
    m = len(T[0])

    sol = ""
    i, j = n-1, m-1
    
    while i > 0 or j > 0:
        if T[i-1][j]:
            sol += "A"
            i -= 1

        if T[i][j-1]:
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

<<<<<<< HEAD
    # TODO : Recorrer tabla hacia atrás desde el final
    if t[n][m]==False:
        return False
    else:
        cnt=0
        for i in range(s):
            if cnt<n:
                if C[i]==A[cnt]:
                    sol+="A"
                    cnt+=1 
                else:
                    sol+="B"      
            else:
                if len(sol)<s:
                    for i in range(s-len(sol)):
                        sol+="B"
        return sol
=======
    return Backtrack(T)
>>>>>>> 431d6f56f03f996e86cb0836962951d946126d02


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

    sol = ""

    if n + m != s:
        return False
    
    Known = {(0,0)} # Set
    Trial = [(0,0)] # Stack

    while len(Trial) > 0:
        (i,j) = Trial.pop()
        k = i + j

<<<<<<< HEAD
        if k >= s:
            cnt=0
            for i in range(s):
                if cnt<n:
                    if C[i]==A[cnt]:
                        sol+="A"
                        cnt+=1 
                    else:
                        sol+="B"      
                else:
                    if len(sol)<s:
                        for i in range(s-len(sol)):
                            sol+="B"
            return sol
    
        if i < n and A[i] == C[k] and (i+1,j) not in Known:
            Trial.append((i+1,j))
            Known.add((i+1,j))

        if j < m and B[j] == C[k] and (i,j+1) not in Known:
            Trial.append((i,j+1))
            Known.add((i,j+1))

    return False
    
=======
        if k == s:
            for tup in Trial: # TODO : Recopilar y devolver solución CX
                print(tup)

            return sol


        if i < n and A[i] == C[k] and (i+1, j) not in Known:
            Trial.append((i+1, j))
            Known.add((i+1, j))

        if j < m and B[j] == C[k] and (i, j+1) not in Known:
            Trial.append((i, j+1))
            Known.add((i, j+1))

    else:
        return False


>>>>>>> 431d6f56f03f996e86cb0836962951d946126d02

if __name__ == "__main__":
    a = "Hello"
    b = "World"
    c = "WHorldello"

    print(MixtureDP(a,b,c))
    print(MixtureCX(a,b,c))

#!env/bin/python


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
    

if __name__ == "__main__":
    a = "Hello"
    b = "World"
    c = "WHorldello"

    print(MixtureDP(a,b,c))
    print(MixtureCX(a,b,c))

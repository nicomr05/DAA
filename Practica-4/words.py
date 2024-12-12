#!env/bin/python

import numpy as np


# Word-creating function
def create_word(n:int, alphabet=(0, 1)) -> list:
    '''
    Description
    -----------
    Creates a word (`string`) of length `n` with possible symbols `alphabet`.

    Parameters
    ----------
    n : `int`
        Length of the word being created.
    alphabet : `tuple`
        Characters that may be used to form the word.

    Returns
    -------
    `list`
        Random word created
    '''
    a = np.random.randint(low=0, high=len(alphabet), size=(n,))
    word = np.array(alphabet)[a].tolist()

    return word


# Word-mixing function
def mix_words(a, b, valid=True) -> list:
    '''
    Description
    -----------
    Mixes a word (`string`) of length `n` with possible symbols `alphabet`.

    Parameters
    ----------
    a : `any kind of array`
        First word to mix.
    b : `any kind of array`
        Second word to mix.
    valid : `bool`
        Indicates wheter the output is going to be valid or not.

    Returns
    -------
    `list`
        Mixed word.
    '''
    new_word = []
    a_array = np.array(a)
    b_array = np.array(b)

    if not valid:
        np.random.shuffle(a_array)
        np.random.shuffle(b_array)

    a_index = 0
    b_index = 0

    while len(new_word) < len(a) + len(b):
        p = np.random.randint(2)
        if (p and a_index < len(a_array)) or b_index >= len(b_array):
            new_word.append(a_array[a_index])
            a_index += 1
        else:
            new_word.append(b_array[b_index])
            b_index += 1

    return new_word


if __name__ == "__main__":
    P1 = create_word(2)
    P2 = create_word(3)
    print(P1, P2)
    wd = mix_words(create_word(2),create_word(3), valid=True)
    print(wd)

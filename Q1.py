def minSubsequences(src: str, tar: str) -> int:
    num_sub = 1 # min subsequences needed if task possible
    len_src, len_tar = len(src), len(tar)
    
    # record index of each char's occurrence, 26 characters in total
    not_found = -1 # all not found by default
    occurrence  = [[ not_found for i in range(len_src)] for i in range(26)]
    
    for i in range(len_src):
        occurrence[ord(src[i]) - ord('a')][i] = i
        
    # characters not found in certain indexs in src but occurred later, 
    # index before that should not be "not found" but tells where it was found later
    for i in range(26):
        for j in range(len_src-2, -1, -1):
            occur_index = occurrence[i][j]
            if (occur_index == not_found):
                occur_index = occurrence[i][j + 1]

    i = 0 # index in target
    j = 0 # index in src's subsequence
    
    while (i < len_tar):
        current_char_occur = occurrence[ord(tar[i]) - ord('a')][j]
        # tar has characters src does not have --> task impossible
        if (j == 0 and current_char_occur == not_found):
            return -1
        # character occurs at j or later in src --> possible element to form subsequence for tar
        elif (j < len_src and current_char_occur > not_found) :
            j = current_char_occur + 1
            i += 1
        # When string formed by adding current character in tar makes it no longer src's subsequence:
        # 1. j = len_src
        # 2. curent character in tar does not occur at or after j in src
        # reset j, increment num_sub since it has to take another number of subsequence if task possible
        else :
            num_sub += 1
            j = 0
    return num_sub

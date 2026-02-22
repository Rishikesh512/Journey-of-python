def pallindrome(st):
    rev=""

    # for i in range(len(st)-1,-1,-1):

        # rev = rev +st[i]
    rev = st[: : -1]
    if rev  == st:
        print(f"{st} is a pallindrome")
    else:
        print(f"{st} is not a pallindrome")

pallindrome("nayan")
pallindrome("soham")
pallindrome("aba")
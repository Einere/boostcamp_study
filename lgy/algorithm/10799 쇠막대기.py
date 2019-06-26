def main():
    ans = 0
    mystack = []
    intstack = []
    flag = False
    paren = input()
    for idx, ch in enumerate(paren):  # O(n)
        if ch == '(':
            mystack.append(ch)
            intstack.append(1)
            flag = True

        if ch == ')':
            mystack.pop()
            if flag:
                if len(mystack) == 0:
                    intstack.pop()
                    continue
                intstack.pop()
                for j in range(len(intstack)): # O(n)
                    intstack[j] += 1
            else:
                ans += intstack[-1]
                intstack.pop()
            flag = False
    print(ans)


main()
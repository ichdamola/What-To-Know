s = "deeedbbcccbdaa"
k = 3

def remove_duplicates(s, k):
    stack = []

    for c in s:
        if stack and stack[-1][0]==c:
            stack[-1][1] += 1
        else:
            stack.append([c,1])
        
        if stack and stack[-1][1]==k:
            stack.pop()
    return "".join([c*n for c,n in stack])
    
print (remove_duplicates(s,k))
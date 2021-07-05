def decodeString(s: str) -> str:

        stack = []
        for i in range(len(s)):
            
            if s[i] != "]":
                stack.append(s[i])
            	
            else: # everytime I see a closing bracket -> I go and parse the word and multiplier and remove opening brackets in the process
                word = ""
                while stack[-1] != "[":
                    word += stack.pop()
                stack.pop() # pop open bracket
                
                multi = ""
                while stack and stack[-1].isdigit():
                    multi += stack.pop()
                multi = int(multi[::-1]) # consider case where mult is more than one digit : ex 23 -> 32 (100 -> 001)
                
                # push back to stack in reversed order
                decoded = multi*word
                for ch in reversed(decoded):
                    stack.append(ch)
 
                
        return "".join(stack)
# Driven code 
if __name__ == '__main__':
    Str = "3[a2[b]]"
    print(decodeString(Str))

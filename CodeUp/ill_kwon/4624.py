#4624
import sys
s = list(input())
stack = []
result = 0

for i in s:
    if i == ')':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if t == 0:
                    stack.append(2)
                else:
                    stack.append(2 * t)
                break
            elif top == '[':    #입력이 올바르지 못한 괄호열이면("[)") 반드시 0을 출력하고 종료. 
                print(0)
                sys.exit(0)
            else:
                t = t + int(top)  #곱해질 값을 저장 하는 부분
 
    elif i == ']':
        t = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if t == 0:
                    stack.append(3)
                else:
                    stack.append(3 * t)
                break
            elif top == '(':    #입력이 올바르지 못한 괄호열이면("(]") 반드시 0을 출력하고 종료. 
                print(0)
                sys.exit(0)
            else:
                t = t + int(top)
 
    else:
        stack.append(i)
 
for i in stack:
    if i == '(' or i == '[':  #괄호 짝이 안 맞을때"(((("" 이면 반드시 0을 출력하고 종료.
        print(0)
        sys.exit(0)
    else:
        result += i

 
print(result)
st = []
L = list(input())
#print(L)
#L.reverse()
#print(L)
count = 0
while count < len(L):
    st.append(L[count])
    if L[count] == ']' or L[count] == ')':
        if st[len(st)-2] == '[':
            st.pop()
            st.pop()
            st.append(3)
        elif st[len(st)-2] == '(':
            st.pop()
            st.pop()
            st.append(2)
        elif type(st[len(st)-2]) == int:
            if L[count] ==']' and st[len(st)-3] == '[':
                st.pop()
                num = st.pop()
                st.pop()
                num = num*3
                st.append(num)
            elif L[count] == ')' and st[len(st)-3] == '(':
                st.pop()
                num = st.pop()
                st.pop()
                num = num*2
                st.append(num)
            else:
                st[0] = 0
                break
    if len(st) == 1:
        count+=1
        continue
    else:
        if type(st[len(st)-1]) == int:
            if type(st[len(st)-2]) == int:
                #print(st)
                a = st.pop()
                b = st.pop()
                num = a+b
                st.append(num)
    if count == len(L)-1:
        if type(st[0]) != int:
            st[0]=0
    count+=1
print(st[0])

from re import S


s=["D","E","S","K"]

# b=s[3]
# s[3]=s[0]
# s[0]=b

# b=s[len(s)-2]
# s[len(s)-2]=s[1]
# s[1]=b


for i in range(int(len(s)/2)):
    b=s[len(s)-(i+1)]
    s[len(s)-(i+1)] = s[i]
    s[i]=b

print(s)

# def Reverse(s):
#     for i in s:
#         b = s[len(s)]




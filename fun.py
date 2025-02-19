
#functions 03/02/2025
def func(*n):
    #print("hiii "+n)
    for i in n:
        print(f"hii {i}")
func("a","B","c")

# def info_det(**info):
#     for key,value in info.item():
#         print(f"{key}:{value}")
# info_det({"a":1,"b":2})

def message(msg):
    if(len(msg)==0):
        print("you have not entered any message")
        return
    word=msg.split()
    print(word)
    l=len(word)
    print(f"word count {l}")
    s=c=0
    for i in word:
        if(i.startswith('#')):
            c=c+1
        s=len(i)+s
    print(sum(len(i) for i in word)/l)
    print(f"avg {s/l}")
    print(f"hash_per {(c/l)*100}") 
inp=input()
message(inp)

lst=[1,2,3,4]
lst1=[i*2 for i in lst]
print(lst1)
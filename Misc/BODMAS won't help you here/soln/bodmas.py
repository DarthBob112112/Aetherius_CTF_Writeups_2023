from pwn import *

r=remote("iitmandi.co.in",10002)
r.recvline()
r.recvline()
r.recvline()
exp=r.recvline().strip()
print(exp)
ans=eval(exp)
r.sendline(bytes(str(ans),'utf-8'))
# r.sendline('hello')
while True:
    exp=str(r.recvline().strip())
    if 'aetherius' in exp:
        print(exp[4:-1])
        break
    exp=exp[4:-1]
    ans=eval(exp)
    print(exp,'=',ans)
    r.sendline(bytes(str(ans),'utf-8'))
# result=r.recvline()
# print(result)
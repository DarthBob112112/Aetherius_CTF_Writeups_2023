Hill Cipher is encrypted by modularly multiplying every 3 letters from the plaintext with the its key
It is decrypted by modularly multiplying every 3 letters from the ciphertext with the inverse of its key

This should be easy given that we have the keys in the form of a matrix with each key being the first 9 elements of each row. Unfortunately for us though, the i<sup>th</sup> element of the i<sup>th</sup> rox has been hidden with an x. This only affects the first 9 keys though, as only the first 9 elements are used

But we are also given a helper string which is just `ctf` repeated over and over for the length of the plaintext.

This makes it easy as we can now brute force the missing value from each key by checking if it gives `ctf` when decrypted.
After filling in the value of all the x's, decrypting the ciphertext gives us the message which we wrap with `aetherius{}`

# Flag

```aetherius{ouradventureswithhillcipherbeginherehopefullyweshallmeetagainnextyear}```
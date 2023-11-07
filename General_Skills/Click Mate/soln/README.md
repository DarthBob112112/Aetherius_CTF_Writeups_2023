The webpage consists of a button that moves along with the cursor, always just far enough that you can't click it.

I ran the following on the console to manually trigger the click on the button:
```
let a=document.getElementById('item') 
a.click() 
```
But when this did not work I decided to inspect the page source once again.
There I noticed the problem- button has an attribute called `disabled`.
I deleted that attribute and ran the above commands again to get a popup with the flag.

# Flag
```aetherius{Console-ations-and-congrats-56428a8e-178d-4348-b6c5-5737bd44d360}```

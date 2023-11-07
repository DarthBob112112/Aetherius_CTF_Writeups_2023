Opening the website, we see that we need to figure out which quadrant the picture of chandler are in.
So first i downloaded the image and cropped out chandler from it to give me the [template](./chandler.jpg) image to match to.

Then I made a script to automatically detect the quadrants and pass it as an array to the input. It keeps doing this until it gets the flag

I used the selenium webdriver to open the link in a browser and download the image.
Then I used opencv to read and split the image into four quadrants. I then passed each quadrant and the template to sift to create keypoints and descriptors. Then these are passed to the opencv BruteForce Matcher with KNN that matches features between images. Then we filter the good matches only.

I found this gives me perfect matches every time.

The [script](./automate.py)

# Flag

`aetherius{Machine-Learning-is-Fun-aa9a9240-cb61-4936-8f62-d9b61ec0f636}`
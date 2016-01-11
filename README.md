# mosaic

This is a simple script to create mosaics using vonronia diagrams in D3.
All this does is loads an image, runs a k-means with a custom distance function, and uses those
center locations/colors to autogenerate an html page with the json.

The fun things to play around with are the weights.

If you just cluster based off of color using
weights = [1,1,1,0,0]
you get results like that in rainbow_color

If you use strong geographical clusters
weights = [1,1,1,300,300]
you will get results like that in warhol or rainbow_mosaic

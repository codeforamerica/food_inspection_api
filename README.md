Restaurant Inspection API
=========================


This is an API to get restaurant inspection information.


### Businesses

    /foodInspection/v1/businesses.json
    
    optional params:
    
    near=lat,lon 
    radius=100  (in meters)


    Bounding Box
    nw=lat,lon  # top left
    se=lat,lon  # bottom right

    query=   # text to query by, ex "Subway"

    page=0  # the page number
    page_size  # number of reseults to return



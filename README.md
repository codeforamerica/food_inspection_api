Restaurant Inspection API
=========================

This is an API to get restaurant inspection information.

It is written in Python, and run as a
[WSGI application](http://wsgi.readthedocs.org/en/latest/what.html).

Install
-------

Prepare a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs.html)
to hold the Python packages listed in `requirements.txt`:

    make venv-food

Activate the virtual environment:

    source venv-food/bin/activate (in bash shell)
    source venv-food/bin/activate.csh (in csh or tcsh shell)

**TODO**: explain Elastic Search setup.

Set an `ELASTICSEARCH_URL` environment variable.

Run the application with [gunicorn](http://gunicorn.org/) on `localhost:8000`:

    gunicorn api:app

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



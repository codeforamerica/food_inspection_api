import json, os
from flask import Flask, request, Response, make_response
from pyelasticsearch import *

import apiModel

es = ElasticSearch(os.environ['ELASTICSEARCH_URL'])
app = Flask(__name__)
app.config['DEBUG'] = True

def cors_response(data):
    response = make_response(data)
    if 'Origin' in request.headers:
        origin = request.headers['Origin']
        response.headers['Access-Control-Allow-Origin'] = origin
    return response

@app.route("/")
def index():
    return "Hello Api"


@app.route("/foodInspection/v1/businesses.json")
def businesses():
    query = request.args.get('query', '')
    nw = request.args.get('nw', '')
    se = request.args.get('se', '')
    page = request.args.get('page', '0')
    page_size = request.args.get('page_size', '100')

    near = request.args.get("near", "")
    radius = request.args.get("radius", "100")

    es_query = {"from" : int(page), "size" : int(page_size)}

    if(query != ""):
        es_query["query"] = {"term":{"name" : query}}
    else:
        es_query["query"] = {"match_all": {}}

    if(nw != "" and se != ""):
        es_query["filter"] =  {
            "geo_bounding_box" : {
                "business.location" : {
                    "top_left" : nw,
                    "bottom_right" : se
                    }
                }
            }
    elif(near != ""):
        es_query["filter"] =  {
            "geo_distance" : {
                "distance" : str(int(radius)/100)+"km",
                "business.location" : {
                    "lat" : near.split(",")[0],
                    "lon" : near.split(",")[1],
                }
            }
        }

    print es_query

    results = es.search(es_query, index='foodinspection')

    return cors_response(Response(json.dumps(apiModel.format_businesses(results)), mimetype='application/json'))




if __name__ == "__main__":
    app.run()

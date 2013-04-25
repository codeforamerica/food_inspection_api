

# Since the model lives in ES, this is to
# format the what we should retern in the API

def format_businesses(es):

    output = {"results":[], "total":es["hits"]["total"]}

    for biz in es["hits"]["hits"]:
        output["results"].append(biz["_source"])

    return output

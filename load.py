import csv, os
from pyelasticsearch import *
es = ElasticSearch(os.environ['ELASTICSEARCH_URL'])

businesses = []
inspections =[]
violations = []

with open('data/businesses.csv', 'rb') as csvfile:
    breader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for b in breader:
        if(b[0] != "business_id"):
            businesses.append(b)
with open('data/inspections.csv', 'rb') as csvfile:
    ireader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i in ireader:
        if(i[0] != "business_id"):
            inspections.append(i)

with open('data/violations.csv', 'rb') as csvfile:
    vreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for v in vreader:
        if(v[0] != "business_id"):
            violations.append(v)


business_objs = []
ic = 0
vc = 0
try:
    es.delete_index("foodinspection")
except ElasticHttpNotFoundError:
    pass

es.create_index("foodinspection")

es.put_mapping(index="foodinspection", doc_type="business", mapping={"business":{"properties":{"location" : {"type" : "geo_point", "store" : "yes"}}}})


for b in businesses:
    biz = {"id":b[0],
           "name":unicode(b[1], errors='ignore'),
           "address":b[2],
           "city":b[3],
           "state":b[4],
           "postal_code":b[5],
           "location":{"lat":(b[6] if b[6] != "" else  0),
                       "lon":(b[7] if b[7] != "" else 0)},
           "phone_number":b[8],
           "inspections":[],
           "violations":[]}

    #print inspections[ic][0]
    print b[0]

    while int(inspections[ic][0]) <= int(b[0])  and ic < len(inspections)-1:

        if(b[0] == inspections[ic][0]):
            biz["inspections"].append({"score":inspections[ic][1],
                                       "date":inspections[ic][2],
                                       "type":inspections[ic][3]})
        ic+=1

    while int(violations[vc][0]) <= int(b[0]) and vc < len(violations)-1:
        if(b[0] == violations[vc][0]):
            biz["violations"].append({"date":violations[vc][1],
                                      "code":violations[vc][2],
                                      "description":unicode(violations[vc][3], errors='ignore')})
        vc+=1

    es.index("foodinspection", "business", biz, id=str(biz["id"]))
    #business_objs.append(biz)
es.put_mapping(index="foodinspection", doc_type="business", mapping={"business":{"properties":{"location" : {"type" : "geo_point", "store" : "yes"}}}})

print "done"
#print business_objs

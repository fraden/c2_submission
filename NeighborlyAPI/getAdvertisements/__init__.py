import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://c2azurecosmosdbaccountname:x2KVfOLSrh7JoTcs2sBdh8B9Xs5x3Lv6G1IpUkBvVl0ikmLnMufiQuGGekj6YuMReJBfYXTvRq0wACDbBXSpPw==@c2azurecosmosdbaccountname.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@c2azurecosmosdbaccountname@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['c2database']
        collection = database['advertisement']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)


import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://c2azurecosmosdbaccountname:x2KVfOLSrh7JoTcs2sBdh8B9Xs5x3Lv6G1IpUkBvVl0ikmLnMufiQuGGekj6YuMReJBfYXTvRq0wACDbBXSpPw==@c2azurecosmosdbaccountname.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@c2azurecosmosdbaccountname@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['c2database']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
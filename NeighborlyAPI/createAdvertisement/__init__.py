import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://c2azurecosmosdbaccountname:x2KVfOLSrh7JoTcs2sBdh8B9Xs5x3Lv6G1IpUkBvVl0ikmLnMufiQuGGekj6YuMReJBfYXTvRq0wACDbBXSpPw==@c2azurecosmosdbaccountname.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@c2azurecosmosdbaccountname@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['c2database']
            collection = database['advertisement']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
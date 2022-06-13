from app.services.mongodb import MongoDb
from app.config import Config


class Model:
    def __init__(self, coll_name, db_name):
        self.mdb = MongoDb()
        self.db_name = db_name if db_name else Config.MONGODB['database']
        self.db = self.mdb.connection[self.db_name]
        self.coll_name = coll_name
        self.coll = self.db[self.coll_name]

    def add(self, body):
        try:
            model_response = self.coll.insert_one(body)
            results = {
                "_id": model_response.inserted_id,
                "success": model_response.acknowledged
            }
            # logger.info(f'[MONGODB] Successfully inserted the data in database. results = {results}')
            return results
        except Exception as e:
            id = body['_id']
            # logger.error(f'[MONGODB] Could not insert data in database for id = {id}, error={e}')
            raise e

    def delete_all(self):
        model_response = self.coll.delete_many({})
        return model_response.deleted_count

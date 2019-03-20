from models import mongo_connection
import logging as log
collection = "jobs"
class JobObject:
    def __init__(self, name, link, frequency=0, id=0):
        self.id = id;
        self.name = name
        self.link = link
        self.frequency = frequency
    def to_document(self):
        return {
            '_id': self.id,
            'name': self.name,
            'link': self.link,
            'frequency': self.frequency
        }
    @staticmethod
    def cursor_to_document(cursor):
        return {
            "_id": cursor['_id'],
            "name": cursor["name"],
            "link": cursor["link"],
            "frequency": cursor["frequency"]
        }
class JobStore:
    def __init__(self, collection_name):
        self.collection = mongo_connection()[collection_name]
        pass

    def insert_one(self, name, link, frequency=0):
        try:
            job_object = JobObject(name, link, frequency)
            result = self.collection.insert_one(job_object)
            log.info('One post: {0}'.format(result.inserted_id))
            return job_object.to_document()
        except Exception as e:
            log.info('Could not create new job: [{}]'.format(e))
            return None

    def find_by_name(self, name):
        try:
            cursor = self.collection.find_one({'name': name})
            job_found = JobObject.cursor_to_document(cursor)
            log.info("Found job: [{}]".format(job_found))
            return job_found
        except Exception as e:
            log.info("could not found job: [{}]".format(e))
            return None

    def find_by_id(self, id):
        try:
            cursor = self.collection.find_one({'_id': id})
            job_found = JobObject.cursor_to_document(cursor)
            log.info("Found job: [{}]".format(job_found))
            return job_found
        except Exception as e:
            log.info("could not found job: [{}]".format(e))
            return None

    def update(self, id, name, link, frequency):
        try:
            self.collection.update({'_id': id}, {
                '$set': {'name': name, 'link': link, 'frequency': frequency}
            })
            return JobObject(name, link, frequency).to_document()
        except Exception as e:
            log.info("Error updating: [{}]".format(e))

    def find_all_jobs(self):
        jobs = self.collection.find({})
        all_jobs = list(map(lambda job: JobObject.cursor_to_document(job), jobs))
        log.info("All job information: [{}]".format(all_jobs))
        return all_jobs




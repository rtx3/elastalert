# -*- coding: utf-8 -*-
from enhancements import BaseEnhancement
from util import elastalert_logger
from alerts import BasicMatchString, DateTimeEncoder
from pymongo import MongoClient
import json


class MyEnhancement(BaseEnhancement):

    def __init__(self,rule):
        super(self.__class__, self).__init__(rule)
        self.dbclient = MongoClient('localhost', 27017)
        self.db = self.dbclient['elastalert']

    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        try:
            db_collection = self.db[self.rule['name']]
            corrected_match = dict()
            for key, value in match:
                if '.' in key:
                    corrected_match[key.replace('.','_')] = corrected_match.pop(key)
                corrected_match[key] = str(value)
            db_ret = db_collection.insert_one(corrected_match).inserted_id
        except Exception as e:
            elastalert_logger.warn("Store to DB aborted: %s" % (e))
            elastalert_logger.warn(corrected_match)
            return
        match_json = json.dumps(match, cls=DateTimeEncoder) + '\n'
        elastalert_logger.info(match_json)
        elastalert_logger.info(self.rule['name'] + " Mongo DB return:" + str(db_ret))
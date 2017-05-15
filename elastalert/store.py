# -*- coding: utf-8 -*-
from enhancements import BaseEnhancement
from util import elastalert_logger
from alerts import BasicMatchString, DateTimeEncoder
from pymongo import MongoClient
import json


class MyEnhancement(BaseEnhancement):


    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        self.dbclient = MongoClient('localhost', 27017)
        self.db = client['elastalert']
        match_json = json.dumps(match, cls=DateTimeEncoder) + '\n'
        db_ret = db.alerts.insert_one(match_json).inserted_id
        elastalert_logger.info(match_json)
        elastalert_logger.info("Mongo DB return:" + str(db_ret))
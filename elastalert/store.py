# -*- coding: utf-8 -*-
from enhancements import BaseEnhancement
from util import elastalert_logger
from alerts import BasicMatchString, DateTimeEncoder
import json

class MyEnhancement(BaseEnhancement):

    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        match_json = json.dumps(match, cls=DateTimeEncoder) + '\n'
        elastalert_logger.info(match_json)
# -*- coding: utf-8 -*-
from enhancements import BaseEnhancement

class MyEnhancement(BaseEnhancement):

    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        logging.warning(str(match))

import urllib2
import json
import ConfigParser as confp

FILE_CONF = "/var/www/whosyourdistrict.org/application.conf"

SECTION_USCENSUSAPI = "USCensusAPI"

API_URL = "http://api.census.gov/data/2011/acs1_cd113"

API_VAR_POP_TOTAL                 = "DP05_0001E"
API_VAR_POP_SEX_MALE              = "DP05_0002E"
API_VAR_POP_SEX_FEMALE            = "DP05_0003E"

API_DATA_INDEX_INNER = 1
API_DATA_INDEX_OUTER = 0

STATE_CODES = { "CO":"08" }

class USCensus_API_CD():
    def __init__(self):
        config = confp.ConfigParser()
        config.read(FILE_CONF)
        self.api_key = config.get(SECTION_USCENSUSAPI, 'Key')
    
    def getRawData(self, var, state = None, district = "*"):
        
        req_url = API_URL + "?" + \
            "key=" + self.api_key + \
            "&get=" + var + \
            "&for=" + "congressional+district:" + district + \
            (("&in=" + "state:" + state) if state else "")

        req = urllib2.Request(req_url)
        res = urllib2.urlopen(req);
        res_obj = json.load(res);

        return res_obj
    
    def getFirstDataPoint(self, var, state = None, district = "*"):
        return self.getRawData(var, state, district)[API_DATA_INDEX_INNER][API_DATA_INDEX_OUTER]

    def getPopTotal(self, state, district):
        data = {}
        data["POP_TOTAL"] = self.getFirstDataPoint(API_VAR_POP_TOTAL, STATE_CODES[state], district)
        return data

    def getPopSex(self, state, district):
        data = {}
        data["POP_SEX_MALE"] = self.getFirstDataPoint(API_VAR_POP_SEX_MALE, STATE_CODES[state], district)
        data["POP_SEX_FEMALE"] = self.getFirstDataPoint(API_VAR_POP_SEX_FEMALE, STATE_CODES[state], district)
        return data

if __name__ == "__main__":

    usc = USCensus_API_CD()
    print(usc.getRawData(API_VAR_POP_TOTAL, "08", "01"))
    print(usc.getFirstDataPoint(API_VAR_POP_TOTAL, "08", "01"))
    print(usc.getPopTotal("CO", "01"))
    print(usc.getPopSex("CO", "01"))

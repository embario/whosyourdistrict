import urllib2
import json
import ConfigParser as confp

FILE_CONF = "/var/www/whosyourdistrict.org/application.conf"

SECTION_USCENSUSAPI = "USCensusAPI"

API_URL = "http://api.census.gov/data/2011/acs1_cd113"

API_VAR_POP_TOTAL                 = "DP05_0001E"
OUT_KEY_POP_TOTAL                 = "POP_TOTAL"
OUT_STR_POP_TOTAL                 = "Total Population"
API_VAR_POP_SEX_MALE              = "DP05_0002E"
OUT_KEY_POP_SEX_MALE              = "POP_SEX_MALE"
OUT_STR_POP_SEX_MALE              = "Male"
API_VAR_POP_SEX_FEMALE            = "DP05_0003E"
OUT_KEY_POP_SEX_FEMALE            = "POP_SEX_FEMALE"
OUT_STR_POP_SEX_FEMALE            = "Female"
API_VAR_POP_AGE_UNDER5            = "DP05_0004E"
OUT_KEY_POP_AGE_UNDER5            = "POP_AGE_UNDER5"
OUT_STR_POP_AGE_UNDER5            = "Under 5"
API_VAR_POP_AGE_05TO09            = "DP05_0005E"
OUT_KEY_POP_AGE_05TO09            = "POP_AGE_05TO09"
OUT_STR_POP_AGE_05TO09            = "5 to 9"
API_VAR_POP_AGE_10TO14            = "DP05_0006E"
OUT_KEY_POP_AGE_10TO14            = "POP_AGE_10TO14"
OUT_STR_POP_AGE_10TO14            = "10 to 14"
API_VAR_POP_AGE_15TO19            = "DP05_0007E"
OUT_KEY_POP_AGE_15TO19            = "POP_AGE_15TO19"
OUT_STR_POP_AGE_15TO19            = "15 to 19"
API_VAR_POP_AGE_20TO24            = "DP05_0008E"
OUT_KEY_POP_AGE_20TO24            = "POP_AGE_20TO24"
OUT_STR_POP_AGE_20TO24            = "20 to 24"
API_VAR_POP_AGE_25TO34            = "DP05_0009E"
OUT_KEY_POP_AGE_25TO34            = "POP_AGE_25TO34"
OUT_STR_POP_AGE_25TO34            = "25 to 34"
API_VAR_POP_AGE_35TO44            = "DP05_0010E"
OUT_KEY_POP_AGE_35TO44            = "POP_AGE_35TO44"
OUT_STR_POP_AGE_35TO44            = "35 to 44"
API_VAR_POP_AGE_45TO54            = "DP05_0011E"
OUT_KEY_POP_AGE_45TO54            = "POP_AGE_45TO54"
OUT_STR_POP_AGE_45TO54            = "45 to 54"
API_VAR_POP_AGE_55TO59            = "DP05_0012E"
OUT_KEY_POP_AGE_55TO59            = "POP_AGE_55TO59"
OUT_STR_POP_AGE_55TO59            = "55 to 59"
API_VAR_POP_AGE_60TO64            = "DP05_0013E"
OUT_KEY_POP_AGE_60TO64            = "POP_AGE_60TO64"
OUT_STR_POP_AGE_60TO64            = "60 to 64"
API_VAR_POP_AGE_65TO74            = "DP05_0014E"
OUT_KEY_POP_AGE_65TO74            = "POP_AGE_65TO74"
OUT_STR_POP_AGE_65TO74            = "65 to 74"
API_VAR_POP_AGE_75TO84            = "DP05_0015E"
OUT_KEY_POP_AGE_75TO84            = "POP_AGE_75TO84"
OUT_STR_POP_AGE_75TO84            = "75 to 85"
API_VAR_POP_AGE_85OVER            = "DP05_0016E"
OUT_KEY_POP_AGE_85OVER            = "POP_AGE_85OVER"
OUT_STR_POP_AGE_85OVER            = "85 and Over"

OUT_KEY_POP_AGE_DEC_4UNDER        = "POP_AGE_4UNDER"
OUT_STR_POP_AGE_DEC_4UNDER        = "4 and Under"
OUT_KEY_POP_AGE_DEC_05TO14        = "POP_AGE_05TO14"
OUT_STR_POP_AGE_DEC_05TO14        = "5 to 14"
OUT_KEY_POP_AGE_DEC_15TO24        = "POP_AGE_15TO24"
OUT_STR_POP_AGE_DEC_15TO24        = "15 to 24"
OUT_KEY_POP_AGE_DEC_25TO34        = "POP_AGE_25TO35"
OUT_STR_POP_AGE_DEC_25TO34        = "25 to 34"
OUT_KEY_POP_AGE_DEC_35TO44        = "POP_AGE_35TO44"
OUT_STR_POP_AGE_DEC_35TO44        = "35 to 44"
OUT_KEY_POP_AGE_DEC_45TO54        = "POP_AGE_45TO54"
OUT_STR_POP_AGE_DEC_45TO54        = "45 to 54"
OUT_KEY_POP_AGE_DEC_55TO64        = "POP_AGE_55TO64"
OUT_STR_POP_AGE_DEC_55TO64        = "55 to 64"
OUT_KEY_POP_AGE_DEC_65TO74        = "POP_AGE_65TO74"
OUT_STR_POP_AGE_DEC_65TO74        = "65 to 74"
OUT_KEY_POP_AGE_DEC_75TO84        = "POP_AGE_75TO84"
OUT_STR_POP_AGE_DEC_75TO84        = "75 to 84"
OUT_KEY_POP_AGE_DEC_85OVER        = "POP_AGE_85OVER"
OUT_STR_POP_AGE_DEC_85OVER        = "85 and Over"

API_VAR_POP_RACE_ANY_WHITE        = "DP05_0059E"
OUT_KEY_POP_RACE_ANY_WHITE        = "POP_RACE_ANY_WHITE"
OUT_STR_POP_RACE_ANY_WHITE        = "White"
API_VAR_POP_RACE_ANY_BLACK        = "DP05_0060E"
OUT_KEY_POP_RACE_ANY_BLACK        = "POP_RACE_ANY_BLACK"
OUT_STR_POP_RACE_ANY_BLACK        = "Black"
API_VAR_POP_RACE_ANY_NATAM        = "DP05_0061E"
OUT_KEY_POP_RACE_ANY_NATAM        = "POP_RACE_ANY_NATAM"
OUT_STR_POP_RACE_ANY_NATAM        = "Native American"
API_VAR_POP_RACE_ANY_ASIAN        = "DP05_0062E"
OUT_KEY_POP_RACE_ANY_ASIAN        = "POP_RACE_ANY_ASIAN"
OUT_STR_POP_RACE_ANY_ASIAN        = "Asian"
API_VAR_POP_RACE_ANY_PACIS        = "DP05_0063E"
OUT_KEY_POP_RACE_ANY_PACIS        = "POP_RACE_ANY_PACIS"
OUT_STR_POP_RACE_ANY_PACIS        = "Pacific Islander"
API_VAR_POP_RACE_ANY_OTHER        = "DP05_0064E"
OUT_KEY_POP_RACE_ANY_OTHER        = "POP_RACE_ANY_Other"
OUT_STR_POP_RACE_ANY_OTHER        = "Other"

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
        data[OUT_KEY_POP_TOTAL] = (self.getFirstDataPoint(API_VAR_POP_TOTAL, STATE_CODES[state], district), OUT_STR_POP_TOTAL)
        return data

    def getPopSex(self, state, district):
        data = {}
        data[OUT_KEY_POP_SEX_MALE]   = (self.getFirstDataPoint(API_VAR_POP_SEX_MALE, STATE_CODES[state], district), OUT_STR_POP_SEX_MALE)
        data[OUT_KEY_POP_SEX_FEMALE] = (self.getFirstDataPoint(API_VAR_POP_SEX_FEMALE, STATE_CODES[state], district), OUT_STR_POP_SEX_FEMALE)
        return data

    def getPopAge(self, state, district):
        data = {}
        data[OUT_KEY_POP_AGE_UNDER5] = (self.getFirstDataPoint(API_VAR_POP_AGE_UNDER5, STATE_CODES[state], district), OUT_STR_POP_AGE_UNDER5)
        data[OUT_KEY_POP_AGE_05TO09] = (self.getFirstDataPoint(API_VAR_POP_AGE_05TO09, STATE_CODES[state], district), OUT_STR_POP_AGE_05TO09)
        data[OUT_KEY_POP_AGE_10TO14] = (self.getFirstDataPoint(API_VAR_POP_AGE_10TO14, STATE_CODES[state], district), OUT_STR_POP_AGE_10TO14)
        data[OUT_KEY_POP_AGE_15TO19] = (self.getFirstDataPoint(API_VAR_POP_AGE_15TO19, STATE_CODES[state], district), OUT_STR_POP_AGE_15TO19)
        data[OUT_KEY_POP_AGE_20TO24] = (self.getFirstDataPoint(API_VAR_POP_AGE_20TO24, STATE_CODES[state], district), OUT_STR_POP_AGE_20TO24)
        data[OUT_KEY_POP_AGE_25TO34] = (self.getFirstDataPoint(API_VAR_POP_AGE_25TO34, STATE_CODES[state], district), OUT_STR_POP_AGE_25TO34)
        data[OUT_KEY_POP_AGE_35TO44] = (self.getFirstDataPoint(API_VAR_POP_AGE_35TO44, STATE_CODES[state], district), OUT_STR_POP_AGE_35TO44)
        data[OUT_KEY_POP_AGE_45TO54] = (self.getFirstDataPoint(API_VAR_POP_AGE_45TO54, STATE_CODES[state], district), OUT_STR_POP_AGE_45TO54)
        data[OUT_KEY_POP_AGE_55TO59] = (self.getFirstDataPoint(API_VAR_POP_AGE_55TO59, STATE_CODES[state], district), OUT_STR_POP_AGE_55TO59)
        data[OUT_KEY_POP_AGE_60TO64] = (self.getFirstDataPoint(API_VAR_POP_AGE_60TO64, STATE_CODES[state], district), OUT_STR_POP_AGE_60TO64)
        data[OUT_KEY_POP_AGE_65TO74] = (self.getFirstDataPoint(API_VAR_POP_AGE_65TO74, STATE_CODES[state], district), OUT_STR_POP_AGE_65TO74)
        data[OUT_KEY_POP_AGE_75TO84] = (self.getFirstDataPoint(API_VAR_POP_AGE_75TO84, STATE_CODES[state], district), OUT_STR_POP_AGE_75TO84)
        data[OUT_KEY_POP_AGE_85OVER] = (self.getFirstDataPoint(API_VAR_POP_AGE_85OVER, STATE_CODES[state], district), OUT_STR_POP_AGE_85OVER)
        return data

    def getPopAgeDec(self, state, district):
        data = {}

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_UNDER5, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_4UNDER] = (str(total),
                                            OUT_STR_POP_AGE_DEC_4UNDER)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_05TO09, STATE_CODES[state], district)) + 
                 int(self.getFirstDataPoint(API_VAR_POP_AGE_10TO14, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_05TO14] = (str(total),
                                            OUT_STR_POP_AGE_DEC_05TO14)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_15TO19, STATE_CODES[state], district)) + 
                 int(self.getFirstDataPoint(API_VAR_POP_AGE_20TO24, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_15TO24] = (str(total),
                                            OUT_STR_POP_AGE_DEC_15TO24)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_25TO34, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_25TO34] = (str(total),
                                            OUT_STR_POP_AGE_DEC_25TO34)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_35TO44, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_35TO44] = (str(total),
                                            OUT_STR_POP_AGE_DEC_35TO44)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_45TO54, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_45TO54] = (str(total),
                                            OUT_STR_POP_AGE_DEC_45TO54)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_55TO59, STATE_CODES[state], district)) + 
                 int(self.getFirstDataPoint(API_VAR_POP_AGE_60TO64, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_55TO64] = (str(total),
                                            OUT_STR_POP_AGE_DEC_55TO64)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_65TO74, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_65TO74] = (str(total),
                                            OUT_STR_POP_AGE_DEC_65TO74)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_75TO84, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_75TO84] = (str(total),
                                            OUT_STR_POP_AGE_DEC_75TO84)

        total = (int(self.getFirstDataPoint(API_VAR_POP_AGE_85OVER, STATE_CODES[state], district)))
        data[OUT_KEY_POP_AGE_DEC_85OVER] = (str(total),
                                            OUT_STR_POP_AGE_DEC_85OVER)

        return data

    def getPopRaceAny(self, state, district):
        data = {}
        data[OUT_KEY_POP_RACE_ANY_WHITE] = (self.getFirstDataPoint(API_VAR_POP_RACE_ANY_WHITE, STATE_CODES[state], district), OUT_STR_POP_RACE_ANY_WHITE)
        data[OUT_KEY_POP_RACE_ANY_BLACK] = (self.getFirstDataPoint(API_VAR_POP_RACE_ANY_BLACK, STATE_CODES[state], district), OUT_STR_POP_RACE_ANY_BLACK)
        data[OUT_KEY_POP_RACE_ANY_NATAM] = (self.getFirstDataPoint(API_VAR_POP_RACE_ANY_NATAM, STATE_CODES[state], district), OUT_STR_POP_RACE_ANY_NATAM)
        data[OUT_KEY_POP_RACE_ANY_PACIS] = (self.getFirstDataPoint(API_VAR_POP_RACE_ANY_PACIS, STATE_CODES[state], district), OUT_STR_POP_RACE_ANY_PACIS)
        data[OUT_KEY_POP_RACE_ANY_OTHER] = (self.getFirstDataPoint(API_VAR_POP_RACE_ANY_OTHER, STATE_CODES[state], district), OUT_STR_POP_RACE_ANY_OTHER)
        return data

if __name__ == "__main__":

    usc = USCensus_API_CD()
    print(usc.getPopTotal("CO", "01"))
    print(usc.getPopSex("CO", "01"))
    print(usc.getPopAge("CO", "01"))
    print(usc.getPopAgeDec("CO", "01"))
    print(usc.getPopRaceAny("CO", "01"))

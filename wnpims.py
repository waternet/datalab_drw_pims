import requests
import pandas as pd
import ww #temp to hide urls

class API:
    def get_curr_val(self, tagname):
        url = ww.URL_GET_CURR_VAL
        params = "?tagnaam=%s" % tagname
        resp = requests.get(url)

        for line in resp.text.split('\n'):
            args = line.split('\t')
            print args

if __name__=="__main__":
    api = API()
    api.get_curr_val("PLV-SB-001_85")

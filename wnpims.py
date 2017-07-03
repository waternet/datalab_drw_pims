import requests, urllib, datetime
import pandas as pd
import ww #temp to hide urls

class API:
    def __init__(self):
        self._logbook = []
        self._log("initialized myself")

    def _log(self, msg):
        """Log a message to the logbook, timekeeping is done in this function

        INPUT
        msg: the message you want to log in string format
        """
        self._logbook.append("%s: %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg))

    def _get_request_result(self, url, params, output='pandas'):
        """This function sends a request and return the text of the response. It deals in a uniform way with possible errors.

        INPUT
        url:    url of the website to retrieve data from
        params: a dictionary of parameters
        output: output format of the result (default pandas)

        OUTPUT
        Pandas DataFrame or none in case of error

        TODO: implement other formats for the result
        """
        finalurl = url + "?%s" % urllib.urlencode(params)

        self._log("starting request to %s" % finalurl)

        resp = requests.get(finalurl)
        if resp.status_code != 200:
            self._log("Got statuscode %s" % resp.status_code)
            return None

        if resp.text.find('<title>Error</title>') > -1:
            self._log("Got error status from the server")
            return None

        if output=="pandas":
            return self._response_text_to_pandas(resp.text)
        else:
            return None

    def _response_text_to_pandas(self, text):
        """Convert the response text to a pandas DataFrame

        INPUT
        text: the response text

        OUTPUT
        Pandas Dataframe or None in case of error

        NOTES
        Expects the text to be formated like
        column1  column2  column3 ...
        value1   value2   value3 ...
        and seperated by tabs (which is the current format of the server)"""
        data = []
        lines = text.split('\n')
        header = lines[0].split('\t')

        for i in range(1,len(lines)):
            args = lines[i].split('\t')
            if args[-1]=="Bad":
                self._log("Got error status on data, probably caused by a wrong tagname")
                return None
            data.append(args)

        result = pd.DataFrame(data, columns=header)
        return result

    def get_curr_val(self, tagname):
        """Wrapper on the get current value url

        INPUT
        tagname: tagname according to the available taglist

        OUTPUT
        Pandas dataframe or None in case of error
        """
        url = ww.URL_GET_CURR_VAL
        params = {'tagnaam':tagname}
        return self._get_request_result(url, params)

    def print_log(self):
        """Prints the logbook as seperated lines"""
        for line in self._logbook:
            print line

# EXAMPLES
if __name__=="__main__":
    api = API()
    df = api.get_curr_val("VVZ1GA01GM00__VD")
    if df is None:
        print "Fout bij de aanroep, hieronder zie je de log"
        api.print_log()
    else:
        print df        

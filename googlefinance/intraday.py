
class IntradayRecord(object):
    def __init__(self,text):
        pass

    @property
    def date(self):
        return self._date
    
    @property
    def close(self):
        return self._close

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high

    @property
    def open(self):
        return self._open
    
    @property
    def volume(self):
        return self._volume
    


    

class IntradayData(object):
    def __init__(self,raw_data):
        pass
    

    def getRange(self):
    """
    """
        pass

    def getPrice(year,month,day,hour,minute):
        pass
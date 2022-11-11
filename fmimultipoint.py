
import datetime as dt
from fmiopendata.wfs import download_stored_query

def endtime():
    """
    End time as UTC
    """
    return  dt.datetime.utcnow()

def starttime(endtime,days:int):
    """
    Create start time as 'days' before 'endtime'
    """
    return endtime - dt.timedelta(days=days)
    
def toisoformat(date:dt):
    return date.isoformat(timespec="seconds") + "Z"


def multipointcoverage(start_time:str,end_time:str):
    """
    Create start_time and end_time as ISO format  
    Observation (multipoint) query
    Seems to return dates queried
    Bounding box 'bbox' close to Jyväskylä airport
    """
    obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                                args=["bbox=25,62,26,63",
                                      "starttime=" + start_time,
                                      "endtime=" + end_time])
    #Return the observations
    return obs

def sample_query():
    """
    Sample query to collect 7 days from Jyväskylä airport
    """
    endutc = endtime()
    startutc = starttime(endutc,7)
    endiso = toisoformat(endutc)
    startiso = toisoformat(startutc)
    #Multipoint coverage query
    obs = multipointcoverage(startiso,endiso)
    ls = sorted(obs.data.keys())
    print("First date:",ls[0],"Last date:", ls[-1])
    return  obs




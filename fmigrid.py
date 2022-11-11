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


def griddata(start_time:str,end_time:str):
    """
    Grid data query
    Seems to return a few days only
    Bounding box 'bbox' as in fmimultipoint close to Jyvöskylä airport
    """
    model_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                   args=["starttime="+start_time,
                                         "endtime="+end_time,
                                         "bbox=25,62,26,62"])
    #Return the model data
    return model_data

def sample_query():
    """
    Sample query to collect 7 days from Jyväskylä airport
    """
    endutc = endtime()
    startutc = starttime(endutc,7)
    endiso = toisoformat(endutc)
    startiso = toisoformat(startutc)
    #Grid data query
    model_data = griddata(startiso,endiso)
    latest_date = max(model_data.data.keys())
    first_date = min(model_data.data.keys())
    print("First date:",first_date,"Latest date:",latest_date)
    return model_data  

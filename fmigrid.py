import datetime as dt
from fmiopendata.wfs import download_stored_query

def endtime():
    return  dt.datetime.utcnow()

def starttime(endtime,days:int):
    return endtime - dt.timedelta(days=days)

def toisoformat(date:dt):
    return date.isoformat(timespec="seconds") + "Z"


def griddata(start_time:str,end_time:str):
    """
    Grid data query
    Seems to return a few days only
    Bounding box 'bbox' as in fmimultipoint
    """
    model_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                   args=["starttime="+start_time,
                                         "endtime="+end_time,
                                         "bbox=25,62,26,62"])
    #Return the model data
    return model_data

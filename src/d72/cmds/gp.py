from d72.cmds.attributes import Status, InternalGPS 

class GP:
    cmd="GP"
    description = "Internal GPS mode"
    # desc, return, format, example response
    getExample= ["Get internal GPS mode", "Returns: internal GPS status", "GP", "GP 1,0"]
    # desc, format, example response
    setExample= ["Set internal GPS mode", "GP x,y", "GP 1,0"]

    status = Status.OFF
    igps = InternalGPS.IGPS

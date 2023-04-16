from d72.cmds.attributes import TNC

class TC:
    cmd="TC"
    description = "TNC control"
    # desc, return, format, example response
    getExample= []
    # desc, format, example response
    setExample= ["Set the TNC control ON or OFF", "TC x", "TC 0"]

    tnc= TNC.OFF
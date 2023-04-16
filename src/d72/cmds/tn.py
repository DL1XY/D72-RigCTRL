from d72.cmds.attributes import TNC, Band

class TN:
    cmd="TN"
    description = "TNC mode"
    # desc, return, format, example response
    getExample= []
    # desc, format, example response
    setExample= ["Set the TNC mode", "TN x,y", "TN 0,0"]

    tnc= TNC.OFF
    band=Band.BAND_A

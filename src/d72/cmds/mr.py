from d72.cmds.attributes import Band

class MR:
    cmd="MR"
    description = "Memory channel"
    # desc, return, format, example response
    getExample= ["Get memory channel", "Returns: memory channel number (3 digit) of band", "MR x", "MS 0,001"]
    # desc, format, example response
    setExample= ["Set memory channel by band and channel number", "MR x,yyy", "MR 0,001"]

    channel = "100"
    band = Band.BAND_A

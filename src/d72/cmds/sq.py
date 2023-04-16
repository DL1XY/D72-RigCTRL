from d72.cmds.attributes import Band, Squelch

class SQ:
    cmd="SQ"
    description = "Squelch"
    # desc, return, format, example response
    getExample= ["Get squelch of band", "Returns: squelch given band", "SQ x", "SQ 0,5"]
    # desc, format, example response
    setExample= ["Set squelch of band", "SQ x,y", "SQ 0,5"]

    band = Band.BAND_A
    squelch = Squelch.VAL_0

from d72.cmds.attributes import Band

class BY:
    cmd="BY"
    description = "Squelch status"
    # desc, return, format, example response
    getExample= ["Get the squelch status for given band", "Returns: squelch status (0: close, 1:open)", "BY x", "BY 1,0"]
    # desc, format, example response
    setExample= []

    band = Band.BAND_B

from d72.cmds.attributes import Band, Power

class PC:
    cmd="PC"
    description = "Output power"
    # desc, return, format, example response
    getExample= ["Get output power", "Returns: band and power of given band", "PC x", "PC 0,1"]
    # desc, format, example response
    setExample= ["Set output power by band", "PC x,y", "PC 0,1"]

    band = Band.BAND_A
    power = Power.HIGH

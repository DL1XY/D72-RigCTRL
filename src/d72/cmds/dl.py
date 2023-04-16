from d72.cmds.attributes import BandMode

class DL:
    cmd="DL"
    description = "Dual band/single band mode"
    # desc, return, format, example response
    getExample= ["Get band mode", "Returns: band mode (0:Dual band, 1:Single band)", "DL", "DL 1"]
    # desc, format, example response
    setExample= ["Set band mode (0:Dual band, 1:Single band)", "DL x", "DL 0"]

    bandMode = BandMode.SINGLE

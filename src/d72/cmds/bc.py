from d72.cmds.attributes import Band

class BC:
    cmd="BC"
    description = "PTT and CTRL band"
    # desc, return, format, example response
    getExample= ["Get the PTT/CTRL band", "Returns: band as number (0:Band A, 1:Band B)", "BC", "BC 0"]
    # desc, format, example
    setExample= ["Set the PTT/CTRL band", "BC x", "BC 0"]

    band= Band.BAND_A

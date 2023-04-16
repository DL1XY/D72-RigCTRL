class MN:
    cmd="MN"
    description = "Memory name"
    # desc, return, format, example response
    getExample= ["Get memory name", "Returns: message", "MN 001", "MN 001,DL1XY"]
    # desc, format, example response
    setExample= ["Set memory name", "MN xxx,yyyyyyyy", "MN 001,DL1XY"]

    channel = "100"
    name = "DL1XY"

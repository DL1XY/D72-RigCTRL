from d72.cmds.attributes import Reset

class SR:
    cmd="SR"
    description = "Reset the radio"
    # desc, return, format, example response
    getExample= []
    # desc, format, example response
    setExample= ["Reset the radio", "SR y", "N"]

    reset = Reset.VFO
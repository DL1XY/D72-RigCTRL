from d72.cmds.attributes import RadioGPSMode

class GM:
    cmd="GM"
    description = "Radio/GPS mode"
    # desc, return, format, example response
    getExample= ["Get radio/GPS mode", "Returns: radio/GPS status", "GM", "GM 0"]
    # desc, format, example response
    setExample= ["Set radio/GPS mode", "GP x", "GP 0"]

    radioGpsMode = RadioGPSMode.RADIO_ON_GPS_OFF
    


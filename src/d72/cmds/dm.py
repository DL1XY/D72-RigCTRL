class DM:
    cmd="DM"
    description = "DTMF memory"
    # desc, return, format, example response
    getExample= ["Get the 16 digit DTMF memory of channel 0-9", "Returns: DTMF code of channel", "DM x", "DM 1,0123456789ABCDEF"]
    # desc, format, example response
    setExample= ["Set the 16 digit DTMF memory. For codes with fewer digits, replace the remaning digits with SPACE", "DM x,yyyyyyyyyyyyyyyy", "DM 1,0123456789ABCDEF"]

    channel="0"
    dtmf="0123456789ABCDEF"


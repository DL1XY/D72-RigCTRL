from d72.cmds.attributes import BurstTone

class BT:
    cmd="BT"
    description = "Burst tone"
    # desc, return, format, example response
    getExample= ["Get the burst tone frequency", "Returns: burst tone frequency (0-3)", "BT", "BT 2"]
    # desc, format, example response
    setExample= ["Set the burst tone frequency", "BT x", "BT 2"]

    burstTone = BurstTone.FREQ_HZ_1750

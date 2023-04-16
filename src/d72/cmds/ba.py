from d72.cmds.attributes import BatteryType

class BA:
    cmd="BA"
    description = "Battery type"
    # desc, return, format, example response
    getExample= ["Get the battery type", "Returns: battery type as number (0:Lithium, 1:Alkaline)", "BA x", "BA 0"]
    # desc, format, example
    setExample= ["Set the battery type", "BA x", "BA 0"]

    batteryType = BatteryType.LITHIUM

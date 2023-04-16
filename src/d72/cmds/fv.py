from d72.cmds.attributes import FirmwareType

class FV:
    cmd="FV"
    description = "Firmware version"
    # desc, return, format, example response
    # TODO analyze all response values
    getExample= ["Get firmware version", "Returns: firmware version depending on input (0:Main, 1:TNC)", "FV x", "FV 0,1.00,1.10,A,1"]
    # desc, format, example response
    setExample= []

    firmwareType=FirmwareType.MAIN

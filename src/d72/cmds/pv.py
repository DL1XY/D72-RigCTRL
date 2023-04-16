from d72.cmds.attributes import ProgrammableVFOBand

class PV:
    cmd="PV"
    description = "Programmable VFO"
    # desc, return, format, example response
    getExample= ["Get programmable VFO", "Returns: VFO band, lower and upper frequency", "PV x", "PV 0,0136,0173"]
    # desc, format, example response
    setExample= ["Set programmable VFO", "PV p1, nnnn, mmmm", "PV 0,0136,0173"]

    vfoBand = ProgrammableVFOBand.A_BAND_136
    lowerFrequency = '0136'
    upperFrequency = '0173'

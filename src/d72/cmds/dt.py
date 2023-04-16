from d72.cmds.attributes import DTMF

class DT:
    cmd="DT"
    description = "DTMF (radio has to be in TX)"
    # desc, return, format, example response
    getExample= []
    # desc, format, example response
    setExample= ["Set DTMF", "DT x,y", "DT 0,1"]

    dtmf=DTMF.DTMF_0

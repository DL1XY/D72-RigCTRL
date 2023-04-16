from d72.cmds.attributes import Band, MemoryVFOMode

class VM:
    cmd="VM"
    description = "Memory VFO mode"
    # desc, return, format, example response
    getExample= ["Get the memory VFO mode", "Returns: band and mode", "VM x", "VM 0,1"]
    # desc, format, example response
    setExample= ["Set the memory VFO mode", "VM x,y", "VM 0,0"]

    band=Band.BAND_A
    memoryVFOMode = MemoryVFOMode.VFO

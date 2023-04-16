from d72.cmds.attributes import Band, StepSize, Shift, Status, ToneCTCSS, DCS, CrossTone, Mode

class FO:
    cmd="FO"
    description = "VFO channel"
    # desc, return, format, example response
    getExample= ["Get the VFO channel", "Returns: the configuration of VFO channel", "FO x","FO 1,0430000000,7,0,0,0,0,0,0,08,08,000,0,01600000,0"]
    # desc, format, example response
    setExample= ["Set the VFO channel","FO p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15","FO 1,0430000000,7,0,0,0,0,0,0,08,08,000,0,01600000,0"]

    band = Band.BAND_B
    frequency = "0430000000"
    stepSize = StepSize.KHZ_25
    shift = Shift.SIMPLEX
    reverse = Status.OFF
    toneStatus=Status.OFF
    ctcssStatus=Status.OFF
    dcsStatus=Status.OFF
    splitTone =Status.OFF 
    toneFrequency=ToneCTCSS.FREQ_HZ_85_4
    ctcssFrequency=ToneCTCSS.FREQ_HZ_85_4
    dcsFrequency=DCS.DEFAULT
    crossTone = CrossTone.OFF
    offsetFrequency ="01600000"
    mode = Mode.FM

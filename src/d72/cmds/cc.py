from d72.cmds.attributes import Band, StepSize, Shift, Status, ToneCTCSS, DCS, CrossTone, Mode

class CC:
    cmd="CC"
    description = "CALL channel"
    # desc, return, format, example response
    getExample= ["Get the CALL channel", "Returns: CALL channel configuration", "CC x", "CC 1,0"]
    # desc, format, example response
    setExample= ["Set the CALL channel", "CC p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17", "CC 2"]

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
    txFrequency = "0000000000"
    lockout=Status.OFF

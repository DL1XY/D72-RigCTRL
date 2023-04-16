from d72.cmds.attributes import Band, StepSize, Shift, Status, ToneCTCSS, DCS, CrossTone, Mode

class ME:
    cmd="ME"
    description = "Memory channel"
    # desc, return, format, example response
    getExample= ["Get the memory channel", "Returns: memory channel configuration", "ME 021", "ME 020,0430100000,4,0,0,0,0,0,0,08,08,000,0,00025000,0,0000000000,0,0"]
    # desc, format, example response
    setExample= ["Set the memory channel", "ME p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18", "ME 020,0430100000,4,0,0,0,0,0,0,08,08,000,0,00025000,0,0000000000,0,0"]

    channel = '020'
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
    unknown='0'
    lockout=Status.OFF


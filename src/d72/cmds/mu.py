from d72.cmds.attributes import LampTimer, BatterySaver, APO, AudioRadioGPS, Status, VOXDelay, BeatShift, Balance, Recall, ScanResume, Time

class MU:
    cmd="MU"
    description = "Menu"
    # desc, return, format, example response
    getExample= ["Get menu configuration", "Returns: menu configuration", "MU", "MU 2,7,6,2,0,0,0,0,4,1,0,0,0,2,0,0,5,2,1"]
    # desc, format, example response
    setExample= ["Set the memory channel", "ME p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19", "MU 7,7,6,2,0,0,0,0,4,1,0,0,0,2,0,0,5,2,1"]

    lampTimer = LampTimer.SEC_7
    contrast = '7'
    batterySaver = BatterySaver.VAL_1
    apo =  APO.MIN_30
    audioRadioGPS = AudioRadioGPS.AUDIO_OFF
    vhfAIP = Status.OFF
    uhfAIP = Status.OFF
    vox=Status.OFF
    voxGain = '4'
    voxDelay = VOXDelay.MS_500
    voxOnBusy = Status.OFF
    beatShift = BeatShift.TYPE_1
    txInhibit = Status.OFF
    balance = Balance.CENTER
    recall = Recall.ALL_BAND
    scanResume = ScanResume.TIME
    timeRestart = Time.SEC_5
    carrierRestart = Time.SEC_2
    autoOffset = Status.ON





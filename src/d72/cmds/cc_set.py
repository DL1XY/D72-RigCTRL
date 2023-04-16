import re
from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band, Shift, StepSize, Status, ToneCTCSS, DCS, CrossTone, Mode
from d72.cmds.cc import CC

class CCSet(SerialCommand):

    config = CC()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band not in Band:
            raise ValueError (f"Band {self.config.band} outside valid range, should be between {Band.BAND_A.value} and {Band.TXB_RXA.value}")
        if not re.match('^[0-9]{10}$', self.config.frequency):
            raise ValueError (f"Frequency {self.config.frequency} is invalid")
        if self.config.stepSize not in StepSize:
            raise ValueError (f"Step size {self.config.stepSize} outside valid range, should be between {StepSize.KHZ_5.value} and {StepSize.KHZ_100.value}")
        if self.config.shift not in Shift:
            raise ValueError (f"Shift {self.config.shift} outside valid range, should be between {Shift.SIMPLEX.value} and {Shift.SPLIT.value}")        
        if self.config.reverse not in Status:
            raise ValueError (f"Reverse {self.config.reverse} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.toneStatus not in Status:
            raise ValueError (f"Tone status {self.config.toneStatus} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.ctcssStatus not in Status:
            raise ValueError (f"CTCSS status {self.config.ctcssStatus} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.dcsStatus not in Status:
            raise ValueError (f"DCS status {self.config.dcsStatus} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.splitTone not in Status:
            raise ValueError (f"Split tone {self.config.splitTone} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        if self.config.toneFrequency not in ToneCTCSS:
            raise ValueError (f"Tone frequency {self.config.toneFrequency} outside valid range, should be between {ToneCTCSS.FREQ_HZ_67.value} and {ToneCTCSS.FREQ_HZ_254_1.value}")
        if self.config.ctcssFrequency not in ToneCTCSS:
            raise ValueError (f"CTCSS frequency {self.config.ctcssFrequency} outside valid range, should be between {ToneCTCSS.FREQ_HZ_67.value} and {ToneCTCSS.FREQ_HZ_254_1.value}")
        if self.config.dcsFrequency not in DCS:
            raise ValueError (f"DCS frequency {self.config.dcsFrequency} outside valid range, should be between {DCS.DEFAULT.value} and {DCS.FREQ_HZ_104.value}")
        if self.config.crossTone not in CrossTone:
            raise ValueError (f"Cross tone {self.config.crossTone} outside valid range, should be between {CrossTone.OFF.value} and {CrossTone.TONE_CTCSS.value}")
        if not re.match('^[0-9]{8}$', self.config.offsetFrequency):
            raise ValueError (f"Offset frequency {self.config.offsetFrequency} is invalid")
        if self.config.mode not in Mode:
            raise ValueError (f"Mode {self.config.mode} outside valid range, should be between {Mode.FM.value} and {Mode.AM.value}")
        if not re.match('^[0-9]{10}$', self.config.txFrequency):
            raise ValueError (f"TX frequency {self.config.txFrequency} is invalid")                
        if self.config.lockout not in Status:
            raise ValueError (f"Lock out {self.config.lockout} outside valid range, should be {Status.OFF.value} or {Status.ON.value}")
        
        return self._receiver.action(f"{self.config.cmd} {self.config.band},"+
                              f"{self.config.frequency},"+
                              f"{self.config.stepSize},"+
                              f"{self.config.shift},"+
                              f"{self.config.reverse},"+
                              f"{self.config.toneStatus},"+
                              f"{self.config.ctcssStatus},"+
                              f"{self.config.dcsStatus},"+
                              f"{self.config.splitTone},"+
                              f"{self.config.toneFrequency},"+
                              f"{self.config.ctcssFrequency},"+
                              f"{self.config.dcsFrequency},"+
                              f"{self.config.crossTone},"+
                              f"{self.config.offsetFrequency},"+
                              f"{self.config.mode},"+
                              f"{self.config.txFrequency},"+
                              f"{self.config.lockout}"
                              ) 
    

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = CCSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()  

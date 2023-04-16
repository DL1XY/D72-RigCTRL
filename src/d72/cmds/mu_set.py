from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import LampTimer, BatterySaver, APO, AudioRadioGPS, Status, VOXDelay, BeatShift, Balance, Recall, ScanResume, Time
import re
from d72.cmds.mu import MU

class MUSet(SerialCommand):

    config = MU()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.lampTimer not in LampTimer:
            raise ValueError (f"Lamp timer {self.config.lampTimer} outside valid range, should be between {LampTimer.SEC_2.value} and {LampTimer.SEC_A.value}")
        if not re.match('^[A-F0-9 ]{1}$', self.config.contrast):
            raise ValueError (f"Contrast {self.config.contrast} is invalid, should be 0 to F")    
        if self.config.batterySaver not in BatterySaver:
            raise ValueError (f"Battery saver {self.config.batterySaver} outside valid range, should be between {BatterySaver.OFF.value} and {BatterySaver.VAL_5.value}")
        if self.config.apo not in APO:
            raise ValueError (f"APO {self.config.apo} outside valid range, should be between {APO.OFF.value} and {APO.MIN_60.value}")
        if self.config.audioRadioGPS not in AudioRadioGPS:
            raise ValueError (f"Audio/Radio/GPS {self.config.audioRadioGPS} outside valid range, should be between {AudioRadioGPS.AUDIO_OFF.value} and {AudioRadioGPS.GPS_ONLY.value}")
        if self.config.vhfAIP not in Status:
            raise ValueError (f"VHF AIP {self.config.vhfAIP} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        if self.config.uhfAIP not in Status:
            raise ValueError (f"UHF AIP {self.config.uhfAIP} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        if self.config.vox not in Status:
            raise ValueError (f"VOX {self.config.vox} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        if not re.match('^[0-9]{1}$', self.config.voxGain):
            raise ValueError (f"VOX gain {self.config.voxGain} is invalid, should be 0 to 9")    
        if self.config.voxDelay not in VOXDelay:
            raise ValueError (f"VOX delay {self.config.voxDelay} outside valid range, should be between {VOXDelay.MS_250.value} and {VOXDelay.MS_3000.value}")
        if self.config.voxOnBusy not in Status:
            raise ValueError (f"VOX on busy {self.config.voxOnBusy} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        if self.config.beatShift not in BeatShift:
            raise ValueError (f"Beat shift {self.config.beatShift} outside valid range, should be between {BeatShift.TYPE_1.value} and {BeatShift.TYPE_8.value}")
        if self.config.txInhibit not in Status:
            raise ValueError (f"TX inhibit {self.config.txInhibit} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        if self.config.balance not in Balance:
            raise ValueError (f"Balance {self.config.balance} outside valid range, should be between {Balance.A.value} and {Balance.B.value}")
        if self.config.recall not in Recall:
            raise ValueError (f"Recall {self.config.recall} invalid, should be {Recall.ALL_BAND.value} or {Recall.CURRENT_BAND.value}") 
        if self.config.scanResume not in ScanResume:
            raise ValueError (f"Scan resume {self.config.scanResume} outside valid range, should be between {ScanResume.TIME.value} and {ScanResume.SEEK.value}")
        if self.config.timeRestart not in Time:
            raise ValueError (f"Time restart {self.config.timeRestart} outside valid range, should be between {Time.SEC_1.value} and {Time.SEC_10.value}")
        if self.config.carrierRestart not in Time:
            raise ValueError (f"Carrier restart {self.config.carrierRestart} outside valid range, should be between {Time.SEC_1.value} and {Time.SEC_10.value}")
        if self.config.autoOffset not in Status:
            raise ValueError (f"Auto offset {self.config.autoOffset} invalid, should be {Status.OFF.value} or {Status.ON.value}") 
        
        return self._receiver.action(f"{self.config.cmd} "
                                +f"{self.config.lampTimer},"                              
                                +f"{self.config.contrast},"
                                +f"{self.config.batterySaver},"
                                +f"{self.config.apo},"
                                +f"{self.config.audioRadioGPS},"
                                +f"{self.config.vhfAIP},"
                                +f"{self.config.uhfAIP},"
                                +f"{self.config.vox},"
                                +f"{self.config.voxGain},"
                                +f"{self.config.voxDelay},"
                                +f"{self.config.voxOnBusy},"
                                +f"{self.config.beatShift},"
                                +f"{self.config.txInhibit},"
                                +f"{self.config.balance},"
                                +f"{self.config.recall},"
                                +f"{self.config.scanResume},"
                                +f"{self.config.timeRestart},"
                                +f"{self.config.carrierRestart},"
                                +f"{self.config.autoOffset}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = MUSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()

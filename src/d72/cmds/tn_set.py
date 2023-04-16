from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import TNC,Band
from d72.cmds.tn import TN

class TNSet(SerialCommand):

    config = TN()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band not in Band:
            raise ValueError (f"Band {self.config.band} outside valid range, should be between {Band.BAND_A.value} and {Band.TXB_RXA.value}")
        if self.config.tnc not in TNC:
            raise ValueError (f"TNC {self.config.tnc} outside valid range, should be between {TNC.OFF.value} and {TNC.TNC.value}")
        self._receiver.action(f"{self.config.cmd} {self.config.tnc},{self.config.band}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = TNSet(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
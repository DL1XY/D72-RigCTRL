
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.ae_get import AEGet
from d72.cmds.id_get import IDGet
from d72.cmds.fv_get import FVGet
from d72.cmds.cs_get import CSGet
from kivy.uix.screenmanager import Screen
Builder.load_file("view/rig.kv")

class Rig(Screen):   

    def __init__(self, **kw): 
        super(Rig, self).__init__(**kw)
        self.rcv = SerialReceiver()
        self.inv = SerialInvoker()

        # Model
        self.cmd_id_get = IDGet(self.rcv)
        self.inv.store_command(self.cmd_id_get)   

        # Radio Serial
        self.cmd_ae_get = AEGet(self.rcv)
        self.inv.store_command(self.cmd_ae_get)   
        
        # Firmware MAIN
        self.cmd_fv_get = FVGet(self.rcv)
        self.inv.store_command(self.cmd_fv_get)   
        
        # Callsign
        self.cmd_cs_get = CSGet(self.rcv)
        self.inv.store_command(self.cmd_cs_get) 
        self.sendCmds()
        self.render()


    def sendCmds(self):        
        self.rcvd = self.inv.execute_commands()         
        
        self.id = self.rcvd.get('ID')
        self.ae = self.rcvd.get('AE')
        self.fv = self.rcvd.get('FV')  
        self.cs = self.rcvd.get('CS')
        
    def render(self):
        print(f'render')
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Name", dp(30)),
                ("Cmd", dp(30)),
                ("Value", dp(30)),
                ("Edit", dp(30)),
            ],
            row_data=[
                ('Model', 'ID', self.id,  ("pencil-off-outline", [0.2, 0.2, 0.2, 1],"")),
                ('Serialnumber', 'AE', self.ae,  ("pencil-off-outline", [0.2, 0.2, 0.2, 1],"")),
                ('Firmware MAIN', 'FV', self.fv,  ("pencil-off-outline", [0.2, 0.2, 0.2, 1],"")),
                ('Callsign', 'CS', self.cs,  ("pencil-outline", [1, 1, 1, 1],"")),
            ],
        )
        self.ids.data_layout.add_widget(self.data_tables)
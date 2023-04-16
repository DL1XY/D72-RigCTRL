from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder
from math import cos, sin, radians
from view.tle_handler import TleHandler
from skyfield.api import load, wgs84
from kivy.graphics import Color, Bezier, InstructionGroup
from view.sat_event import SatEvent
from kivy.uix.label import Label
import datetime

Builder.load_file("view/polarview.kv")      


class PolarView(Screen):

    points = []
    satevents = []
    circle = "\u2B24"      
    yolo = None
    def __init__(self, **kw):  
        super(PolarView, self).__init__(**kw)

        self.loadSatData()
        self.renderBezier()
        self.renderEvent()
        self.renderBullets()
        
    def loadSatData(self):  
        tleHandler = TleHandler()
        ts = load.timescale()
        qth = wgs84.latlon(+52.6437, 13.1882)
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        t0 = ts.utc(today.year, today.month, today.day)
        t1 = ts.utc(tomorrow.year, tomorrow.month, tomorrow.day)
        satellite = tleHandler.getSatelliteByNoradId(25544)
        altDeg = 30.0
        t, events = satellite.find_events(qth, t0, t1, altitude_degrees=altDeg)
        i=0
        for ti, event in zip(t, events):
            name = ('Rise', 'culminate', 'Set')[event]
            difference = satellite - qth
            topocentric = difference.at(ti)
            alt, az, distance = topocentric.altaz()
            azMod = (-az.degrees+90)%360         
            center_x = self.center_x
            center_y = self.center_y
            
            offsetRawX = cos(radians(azMod))
            offsetRawY = sin(radians(azMod))
            offsetX = offsetRawX * center_x
            offsetY = offsetRawY * center_y
            x =  center_x + offsetX/2
            y =  center_y + offsetY/2        
            self.points.append(x)
            self.points.append(y)
            print (f'centerX:{center_x} centerY:{center_y} offsetRawX:{offsetRawX} offsetRawY:{offsetRawY} offsetX:{offsetX} offsetY:{offsetY} x:{x} y:{y}')
            satEvent = SatEvent()
            satEvent.satName = satellite.name
            satEvent.satNorad = satellite.model
            satEvent.name = name
            satEvent.time = ti.utc_strftime('%Y-%m-%d %H:%M:%S UTC')
            satEvent.az = az 
            satEvent.alt = alt
            self.satevents.append(satEvent)
            i=i+1
            if i == 3:
                break    

    def renderBezier(self):
       
        print(self.points)
        Color(1.0, 0.0, 0.0)
        self.bezier = Bezier(
                points=self.points,
                segments=100,                
                loop=False)
       
    
        #self.add_widget(self.ig)
        #self.ids.layout.add_widget(self.bezier)
        
    def renderEvent(self):
       
        sat_rise_event = self.satevents[0]
        sat_max_event = self.satevents[1]
        sat_set_event = self.satevents[2]       
        sat_info_txt = f'[font=Roboto-Bold][size=18]{sat_rise_event.satName}[/size][/font]'
        sat_rise_txt = f'\n\n[font=DejaVuSans][size=16][color=00ff00]{self.circle}[/color][/size][/font] {sat_rise_event.time} at {sat_rise_event.az.degrees:.1f}°'
        sat_max_txt = f'\n\nMax: {sat_max_event.alt.degrees:.1f}°'
        sat_set_txt = f'\n\n[font=DejaVuSans][size=16][color=FF0000]{self.circle}[/color][/size][/font] {sat_set_event.time} at {sat_set_event.az.degrees:.1f}°'            
        self.ids.sat_event_info.text = sat_info_txt + sat_rise_txt + sat_max_txt + sat_set_txt

    def renderBullets(self):
       
        rise_x = self.points[0]
        rise_y = self.points[1]
        set_x = self.points[len(self.points)-2]
        set_y = self.points[len(self.points)-1]
        
        rise_lbl = Label(text=f'[font=DejaVuSans][size=16][color=00ff00]{self.circle}[/color][/size][/font]', markup=True)
        rise_lbl.pos = (rise_x,rise_y)


        set_lbl = Label(text=f'[font=DejaVuSans][size=16][color=ff0000]{self.circle}[/color][/size][/font]', markup=True)
        set_lbl.pos = (set_x,set_y)
        self.add_widget(rise_lbl)
        self.add_widget(set_lbl)
    
    def rscale(self, size, *args):
        print(size)
        return self.points
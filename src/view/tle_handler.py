from skyfield.api import load, wgs84
import datetime

class TleHandler():
    def __init__(self):
        print("TLE")
        pass

    def getSatellitesFromTle(self):
        stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
        satellites = load.tle_file(stations_url)
        return satellites
    
    def getISS(self):
        satellites = self.getSatellitesFromTle()
        by_number = {sat.model.satnum: sat for sat in satellites}
        satellite = by_number[25544]
        return satellite
    
    def getSatelliteByNoradId(self, noradId):
        satellites = self.getSatellitesFromTle()
        by_number = {sat.model.satnum: sat for sat in satellites}
        satellite = by_number[noradId]
        return satellite
    
    def getRiseAndSet(self, noradId):
        ts = load.timescale()
        qth = wgs84.latlon(+52.6437, 13.1882)
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        t0 = ts.utc(today.year, today.month, today.day)
        t1 = ts.utc(tomorrow.year, tomorrow.month, tomorrow.day)
        satellite=self.getSatelliteByNoradId(noradId)
        t, events = satellite.find_events(qth, t0, t1, altitude_degrees=30.0)
        for ti, event in zip(t, events):
            name = ('rise above 30°', 'culminate', 'set below 30°')[event]
            print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
            difference = satellite - qth
            topocentric = difference.at(ti)
            alt, az, distance = topocentric.altaz()
            if alt.degrees > 0:
                print('The ISS is above the horizon')
                print('Altitude:', alt)
                print('Azimuth:', az)
                print('Distance: {:.1f} km'.format(distance.km))    
        
        return t, events
    

if __name__ == '__main__':
    app = TleHandler()
    app.getRiseAndSet(25544)
    

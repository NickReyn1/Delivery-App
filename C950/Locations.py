from location import location
import csv
class Locations:
    def __init__(self):
        self.distanceData = []
        self.locationData = []
# imports the distances one location to another from the provided .csv file
        with open('Distance_Formatted.csv') as csv_file:
            distanceReader = csv.reader(csv_file)

            for row2 in distanceReader:
                self.distanceData.append(row2)

# imports location data from the provided .csv file
        with open('WGUPS Distance Table_Formatted.csv') as csv_file:
            locReader = csv.reader(csv_file)
            i = 0
            for row2 in locReader:
                h = location(row2[0], row2[1], row2[2], row2[3])
                self.locationData.append(h)

# searches through the location data for a specific address and returns that address id O(n) where n is the number of locations
    def searchLoc(self, address):
        for x in self.locationData:
            if x.locationAddress == address:
                return int(x.locationID)
# returns the distance between any two addresses O(2n) because it calls searchLoc
    def distance(self, address1, address2):
        locID1 = self.searchLoc(address1)
        locID2 = self.searchLoc(address2)
        if locID1 >= locID2:
            return float(self.distanceData[locID1][locID2])
        else:
            return float(self.distanceData[locID2][locID1])

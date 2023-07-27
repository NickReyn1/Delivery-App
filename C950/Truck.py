from Package import packageHashTable
from Locations import Locations
import datetime



class Truck:
    def __init__(self):
        self.averageSpeedPerSecond = .005
        self.packageMax = 16
        self.currentPackages = 0
        self.driver = ""
        self.currentLocation = "4001 South 700 East"
        self.nextLocation = self.currentLocation
        self.packages = []
        self.startTime = datetime.timedelta(hours=7)
        self.miles = 0
        self.currentTime = self.startTime
        self.endTime = self.startTime

# inserts a package into the trucks package list
    def insert(self,packageID ,package):
        self.packages.insert(packageID, package)

# removes a package from the trucks package list
    def remove(self, packageID):
        self.packages.remove(packageID)

# returns the turcks package list object. This could be refactored to just print out the id of each package in the truck.
    def getPackageList(self):
        return self.packages

# calls loads all of the packages in the list that is passed to the function onto the truck O(n)
    def loadPackages(self, packagelist):
        for x in packagelist:
            self.insert(x, packageHashTable.lookup(x))

# calculates the distance between two locations using the Location classes distance function
    def distanceBetween(self, address1, address2):
        l1 = Locations()
        return l1.distance(address1, address2)

# greedy nearest neighbor algorithm that returns the next location that is closest to the current one. O(2*n*l) where n is the number of packages and l is the number of locations.
    def minDistance(self, currentAddress):
        smallest = 1000.00
        nextLoc = currentAddress
        for x in self.packages:
            # print currentAddress
            # print x.deliveryAddress
            i = float((self.distanceBetween(currentAddress, x.deliveryAddress)))
            if i < smallest and i != 0:
                smallest = i
                nextLoc = x.deliveryAddress
        return nextLoc

# delivers the packages in the trucks package List O(2*n^3*l) calls
    def deliverPackages(self):
        for x in self.packages:
            x.departureTime = self.currentTime
        while len(self.packages) > 0:
            print(self.currentTime)
            self.miles += self.distanceBetween(self.currentLocation, self.nextLocation)
            self.currentTime = self.currentTime + datetime.timedelta(0, (self.distanceBetween(self.currentLocation, self.nextLocation) / self.averageSpeedPerSecond))
            self.currentLocation = self.nextLocation
            if self.currentLocation == "4001 South 700 East":
                self.nextLocation = self.minDistance(self.currentLocation)

            else:
                tempPackages = []
                for x in self.packages:
                    if x.deliveryAddress == self.currentLocation:
                        tempPackages.append(x)
                for y in tempPackages:
                    for x in self.packages:
                        if x.deliveryAddress == y.deliveryAddress:
                            packageHashTable.lookup(int(x.packageID)).deliveryStatus = "Delivered"
                            packageHashTable.lookup(int(x.packageID)).timeDelivered = self.currentTime
                            print(x.packageID)
                            self.packages.remove(x)
                self.nextLocation = self.minDistance(self.currentLocation)

        self.nextLocation = "4001 South 700 East"
        self.miles += self.distanceBetween(self.currentLocation, self.nextLocation)
        self.currentTime = self.currentTime + datetime.timedelta(0, (self.distanceBetween(self.currentLocation, self.nextLocation) / self.averageSpeedPerSecond))
        self.currentLocation = self.nextLocation
        self.endTime = self.currentTime

        print(self.currentLocation)
        print(self.endTime)
        print(self.miles)

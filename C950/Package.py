import datetime
from chaining_hash_table import chaining_hash_table
import csv
class Package:
    def __init__(self, package_ID, delivery_Address, delivery_City, delivery_State, delivery_Zip, delivery_Deadline,
                 package_Weight, required_Truck, required_Package1, required_Package2, notes):
        self.packageID = package_ID
        self.deliveryAddress = delivery_Address
        self.deliveryCity = delivery_City
        self.deliveryState = delivery_State
        self.deliveryZip = delivery_Zip
        self.deliveryDeadline = delivery_Deadline
        self.packageWeight = package_Weight
        self.requiredTruck = required_Truck
        self.requiredPackage1 = required_Package1
        self.requiredPackage2 = required_Package2
        self.notes = notes
        self.deliveryStatus = "Waiting to be loaded"
        self.timeDelivered = datetime.timedelta(hours=24)
        self.departureTime = None   # datetime.timedelta(hours=0)


    def __call__(self):
        print(self.packageID)

# creates an instance of the chaining hash table data structure to contain all of the package objects
packageHashTable = chaining_hash_table()

# Creates an iterable array to contain just the id's of each package that was imported
PackageList = []

# Imports data from the provided package file and creates package objects containing the data.
def loadPackageData(file):
    with open(file) as csvfile:
        fileReader = csv.reader(csvfile)

        for row in fileReader:
            p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            packageHashTable.insert(int(p.packageID) ,p)
            PackageList.append(row[0])



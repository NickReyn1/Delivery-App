# Nicholas Reynolds 011147415

import chaining_hash_table
from Package import PackageList
from Truck import Truck
from Package import loadPackageData
import datetime
import tkinter
from Package import packageHashTable

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    truckList = chaining_hash_table.chaining_hash_table()

# initializes a truck. the start time for that truck is determined based on the truck's ID to account for packages that are arriving later
    def start_Truck(truck_id, startTime = datetime.timedelta(hours=8, minutes=30), currentTime = datetime.timedelta(hours=8, minutes=30)):
        truck = Truck()
        if truck_id == 2:
            truck.startTime = datetime.timedelta(hours=9, minutes=5)
            truck.currentTime = datetime.timedelta(hours=9, minutes=5)
        else:
            truck.startTime = startTime
            truck.currentTime = currentTime

        truckList.insert(truck_id, truck)
        outputBox.insert(tkinter.END, "\nTruck "+ str(truck_id) + " started")

# loads a specific grouping of packages onto a specific truck. If the third package list is the one being loaded the
# trucks start time is set to 10:30 or later to account for the one package that's address is being changed later on.
    def load_Packages(truck_id, packageList):
        if truckList.lookup(truck_id) is not None:
            if packageList == 1:
                truckList.lookup(truck_id).loadPackages(packages1)
            elif packageList == 2:
                truckList.lookup(truck_id).loadPackages(packages2)
            else:
                if truckList.lookup(truck_id).endTime > datetime.timedelta(hours=10, minutes=30):
                    truckList.lookup(truck_id).startTime = truckList.lookup(truck_id).endTime
                else:
                    truckList.lookup(truck_id).startTime = datetime.timedelta(hours=10, minutes=30)
                packageHashTable.lookup(int("9")).deliveryAddress = "410 S State St"
                truckList.lookup(truck_id).miles = 0
                truckList.lookup(truck_id).loadPackages(packages3)
            outputBox.insert(tkinter.END, "\nTruck " + str(truck_id)+ " loaded with package group " + str(packageList))
        else:
            outputBox.insert(tkinter.END, "\n You must select a truck and start it before loading packages.")

# begins delivering the packages on a specific truck and returns the amount of miles the truck drove.
    def deliver_Packages(truck_id):
        if truckList.lookup(truck_id) is not None:
            truckList.lookup(truck_id).deliverPackages()
            outputBox.insert(tkinter.END, "\nTruck " + str(truck_id) + " has delivered its packages.")
            return truckList.lookup(truck_id).miles
        else:
            outputBox.insert(tkinter.END, "\nYou must start a truck and load it before you can deliver packages.")

# provides an update on where packages were at a specific time
    def packageUpdate(time="00:00:00"):
        try:
            (h, m, s) = time.split(":")
            dtime = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
            for x in PackageList:
                #outputBox.insert(tkinter.END, "\n timedelivered" + str(packageHashTable.lookup(int(x)).timeDelivered) + " departuretime " + str(packageHashTable.lookup(int(x)).departureTime))
                if packageHashTable.lookup(int(x)).timeDelivered < dtime:
                    outputBox.insert(tkinter.END, "\nPackageID: "  +str(packageHashTable.lookup(int(x)).packageID) +" Delivery Status: Delivered"+" Current Time: "+ str(dtime))
                elif packageHashTable.lookup(int(x)).departureTime != None and packageHashTable.lookup(int(x)).departureTime < dtime :
                    outputBox.insert(tkinter.END, "\nPackageID: " + str(packageHashTable.lookup(int(x)).packageID) + " Delivery Status: Out for Delivery" + " Current Time: " + str(dtime))
                else:
                    outputBox.insert(tkinter.END, "\nPackageID: " + str(packageHashTable.lookup(int(x)).packageID) + " Delivery Status: Waiting to be loaded" + " Current Time: " + str(dtime))
        except ValueError:
            outputBox.insert(tkinter.END, "\nYou need to enter a time in the correct format.")



# prints out the delivery status of all packages and the total miles that have been traveled
    def print_AllStatusMileage():
        for x in PackageList:
            outputBox.insert(tkinter.END, "\nPackageID: "  +str(packageHashTable.lookup(int(x)).packageID) +" Delivery Status: "+ str(packageHashTable.lookup(int(x)).deliveryStatus))
            if(packageHashTable.lookup(int(x)).timeDelivered != datetime.timedelta(hours=24)):
               outputBox.insert(tkinter.END, " Delivery Time: " + str(packageHashTable.lookup(int(x)).timeDelivered))
        outputBox.insert(tkinter.END, "\n Total mileage: " + str(totalMiles) )

# prints the package status and the time the package was delivered for a specific packageID
    def print_PackageStatusTime(pid, truck_id):
        if truckList.lookup(truck_id.get()) is not None:
            outputBox.insert(tkinter.END, "\nPackageID: "+ str(pid) + " Delivery Status: " + str(packageHashTable.lookup(int(pid)).deliveryStatus) + " Time Delivered: " + str(packageHashTable.lookup(int(pid)).timeDelivered) + " Current Time:" +str(truckList.lookup(truck_id.get()).currentTime))
        else:
            outputBox.insert(tkinter.END, "\nPackageID: " +str(packageHashTable.lookup(int(pid)).packageID) +" Delivery Status: " + str(packageHashTable.lookup(int(pid)).deliveryStatus))

# prints a list of all package ID's, their delivery status, and the current time for a specific truck
    def print_AllPackageStatusTime(truck_id):
        if truckList.lookup(truck_id.get()) is not None:
            for x in PackageList:
                outputBox.insert(tkinter.END, "\nPackageID: " +str(packageHashTable.lookup(int(x)).packageID) +" Delivery Status: " + str(packageHashTable.lookup(int(x)).deliveryStatus) + " Current Time: " + str(truckList.lookup(truck_id.get()).currentTime))
        else:
            for x in PackageList:
                outputBox.insert(tkinter.END, "\nPackageID: " +str(packageHashTable.lookup(int(x)).packageID) +" Delivery Status: " + str(packageHashTable.lookup(int(x)).deliveryStatus) + " Current Time: 00:00:00")

 # Adds a trucks mileage to the total mileage
    def AddMileage(miles):
        global totalMiles
        if miles is not None:
            totalMiles += miles

    def _exit():
        top.quit()

        # groups of packages to be loaded on trucks
    packages1 = [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40]
    packages2 = [3, 5, 6, 18, 25, 26, 27, 28, 32, 35, 36, 38]
    packages3 = [2, 4, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 33, 39]
    totalMiles = 0
    loadPackageData('WGUPS Package File_Formatted.csv')

    #Creates UI elements
    top = tkinter.Tk()
    top.geometry("900x900")
    buttonsFrame = tkinter.Frame(top, width=450, height=900, bg="white")
    outputFrame = tkinter.Frame(top, width=450, height=900, bg="yellow")

    var = tkinter.IntVar()
    truck1 = tkinter.Radiobutton(master = buttonsFrame, width=50, text = "truck1", variable=var, value=1)
    truck2 = tkinter.Radiobutton(master=buttonsFrame, width=50, text = "truck2", variable=var, value=2)
    truck3 = tkinter.Radiobutton(master=buttonsFrame, width=50, text = "truck3", variable=var, value=3)
    var2 = tkinter.IntVar()
    packageList1 = tkinter.Radiobutton(master=buttonsFrame, width=50, text="packageList1", variable=var2, value=1)
    packageList2 = tkinter.Radiobutton(master=buttonsFrame, width=50, text="packageList2", variable=var2, value=2)
    packageList3 = tkinter.Radiobutton(master=buttonsFrame, width=50, text="packageList3", variable=var2, value=3)

    label = tkinter.Label(master = buttonsFrame, text="Select Package: Default 1")
    IDtext = tkinter.StringVar()
    IDtext.set("1")
    packageID = tkinter.Entry(master = buttonsFrame, textvariable=IDtext)

    label2 = tkinter.Label(master=buttonsFrame, text="Enter Time(HH:MM:SS): ")
    timeText = tkinter.StringVar()
    timeText.set("00:00:00")
    lookupTime = tkinter.Entry(master=buttonsFrame,textvariable= timeText)

    outputBox = tkinter.Text(master=outputFrame, height = 900)
    startTruck = tkinter.Button(master=buttonsFrame, width=50, text= "Start a truck", command=lambda: start_Truck(var.get()))
    loadPackages = tkinter.Button(master=buttonsFrame, width=50, text=" Begin loading packages", command=lambda: load_Packages(var.get(),var2.get()))
    deliverPackages = tkinter.Button(master=buttonsFrame, width=50, text= "Begin delivering packages", command=lambda: AddMileage(deliver_Packages(var.get())))
    printAllStatusMileage = tkinter.Button(master=buttonsFrame, width=50, text= "All Package Status + Total Mileage", command= print_AllStatusMileage)
    printPackageStatusTime = tkinter.Button(master=buttonsFrame, width=50, text= "Single Package status + Current Time", command=lambda: print_PackageStatusTime(int(packageID.get()), var) )
    printAllPackageStatusTime = tkinter.Button(master=buttonsFrame, width=50, text= "All Package Status + Current Time", command=lambda: print_AllPackageStatusTime(var))
    printPackageUpdate = tkinter.Button(master=buttonsFrame, width=50,text="All Package Status at a Specific Time",command=lambda: packageUpdate(lookupTime.get()))
    exit = tkinter.Button(master=buttonsFrame, text="Exit Program", width=50, command= _exit)

    buttonsFrame.pack(fill=tkinter.X, side=tkinter.LEFT)
    outputFrame.pack(fill=tkinter.Y, side=tkinter.RIGHT)
    truck1.pack()
    truck2.pack()
    truck3.pack()
    packageList1.pack()
    packageList2.pack()
    packageList3.pack()
    label2.pack()
    lookupTime.pack()
    label.pack()
    packageID.pack()
    outputBox.pack()
    startTruck.pack()
    loadPackages.pack()
    deliverPackages.pack()
    printAllStatusMileage.pack()
    printPackageStatusTime.pack()
    printAllPackageStatusTime.pack()
    printPackageUpdate.pack()
    exit.pack()

    top.mainloop()


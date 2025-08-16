class Vehicle:
    def __init__(self,vtype,model,no_plate,price_per_day,availability):
        self.vtype=vtype
        self.model=model
        self.no_plate=no_plate
        self.price_per_day=price_per_day
        self.availability=availability
    def __str__(self):
        return f"{self.vtype}\t{self.model}\t{self.no_plate}\t{self.price_per_day}\t\t\t{self.availability}"
    def __mul__(self,days):
        return int(self.price_per_day)*days

class Booking:
    def __init__(self,vehicle,customer,rental_days,price):
        self.vehicle=vehicle
        self.customer=customer
        self.rental_days=rental_days
        self.price_per_day=price
    def __str__(self):
        return f"{self.vehicle}\t{self.customer}\t\t{self.rental_days}\t\t{self.price_per_day}"

class Rental_Service:
    def __init__(self):
        self.vehicles=[]
        self.bookings=[]
    def add_vehicle(self,vtype,model,no_plate,price_per_day,availability):
        for i in self.vehicles:
            if no_plate==i.no_plate:
                print("Vehicle Already Exists!\n")
                return
        else:
            self.vehicles.append(Vehicle(vtype,model,no_plate,price_per_day,availability))
            print("Vehicle Added Succesfully!\n")
    def remove_vehicle(self,no_plate):
        for i in self.vehicles:
            if i.no_plate==no_plate:
                self.vehicles.remove(i)
                print(f"Vehicle Removed Succesfully!\n")
                return
        print("Vehicle Not Found!\n")
    def update_price(self,no_plate,price_per_day):
        for i in self.vehicles:
            if i.no_plate==no_plate:
                print(True)
                i.price_per_day=price_per_day
                print("Price Updated Successfully!\n")
                return
        print("Vehicle Not Found!\n")
    def fare_calc(self,no_plate,rent_for_days):
        for i in self.vehicles:
            if no_plate==i.no_plate:
                return i.price_per_day*rent_for_days
    def book_vehicles(self,customer,no_of_vehicles,no_plates: list,rent_for_days: list):
        if no_of_vehicles==len(no_plates)==len(rent_for_days):
            total_fare=0
            for i in range(no_of_vehicles):
                for j in self.vehicles:
                        if j.no_plate==no_plates[i]:
                            if j.availability=="No":
                                print(f"Dear {customer} \"{j.no_plate}\" is Not Available!\nTry Booking Available Vehicles\n")
                                return
            for i in range(no_of_vehicles):
                x=self.fare_calc(no_plates[i],rent_for_days[i])
                if str(x).isdigit():
                    self.bookings.append(Booking(no_plates[i],customer,rent_for_days[i],next((self.vehicles[k].price_per_day for k in range(len(self.vehicles)) if self.vehicles[k].no_plate==no_plates[i]),None)))
                    for j in self.vehicles:
                        if j.no_plate==no_plates[i]:
                            j.availability="No"
                    total_fare+=x
                else:
                    print(f"\"{no_plates[i]}\" Not Available\n")
                    return
            print(f"Succesfully Booked {no_plates}\nYour Total Fare: {total_fare}\n")
        else:
            print("Booking Failed!\nEnter valid data\n")
    def return_vehicle(self,no_plate,late_days=0):
        total=0
        for i in self.bookings:
            if i.vehicle==no_plate:
                for j in self.vehicles:
                    if j.no_plate==no_plate:
                        j.availability="Yes"
                print(f"{i.vehicle} Was Succesfully Returned!\n")
                total+=(i.price_per_day*i.rental_days)+(late_days*i.price_per_day)
                self.bookings.remove(i)
        if total==0:
            print("Enter Valid Data!\n")
            return
        return total
    def __str__(self):
        s=""
        if len(self.vehicles)>0:
            s+=f"--> Vehicles List\n"
            s+="Type\tModel\t\tNumber_plate\tRental Price/Day\tAvailability\n"
            for i in range(len(self.vehicles)):
                s+=f"{self.vehicles[i]}\n"
        else:
            s+=f"No Vehicles Present!\n"
        if len(self.bookings)>0:
            s+="\n--> Bookings:\n"
            s+="Vehicle\t\tCustomer\tRental Days\tPrice Per Day\n"
            for i in range(len(self.bookings)):
                s+=f"{self.bookings[i]}\n"
        else:
            s+=f"No Bookings Present!\n"
        return s

# -----Example-----
# console=Rental_Service()
# console.add_vehicle("Bike","Honda Activa","KA05 AB 1234",300,"Yes")
# console.add_vehicle("Bike","Honda Activa","KA05 AB 1234",1500,"Yes")
# console.update_price("KA05 AB 1234",500)
# print(console)
# console.remove_vehicle("KA05 AB 1234")
# print(console)
# console.add_vehicle("Bike","Bajaj Pulsar","AP09 EF 2468",300,"Yes")
# console.book_vehicles("Ghouse",2,["KA05 AB 1234","AP09 EF 2468"],[2,3])
# print(console)
# console.add_vehicle("Bike","Royal Enfield","MH12 XY 9876",800,"Yes")
# console.book_vehicles("Deepak",2,["MH12 XY 9876","AP09 EF 2468"],[3,5])
# print(console) 
# console.return_vehicle("KA05 AB 1234",0)
# print(console)
# console.return_vehicle("AP09 EF 2468",5)
# print(console)



class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
   
    def getInfo(self):
        print(f"The name of the train is {self.name}")
        print(f"The available seats is {self.seats}")
    
    def fareInfo(self):
        print(f"The fare is Rs.{self.fare}")

    def bookTicket(self,ticket):
        if self.seats>0:
            a=input("Would you like to book ticket (Y/N)?\n")
            if a.capitalize()=="Y":
                print("Available tickets are ", ticket)
                ans=int(input("Which ticket no. would you like to book?" ))
                if ans not in ticket:
                    print("Invalid")
                else:
                    print(f"The ticket is booked. Your seat no. is {ans}")
                    print("******")
                    self.seats-=1 
                    ticket.remove(ans)
            elif a.capitalize()=="N":
                print("Thank you for visiting")
            else:
                print("Invalid")
        else:
            print("Sorry. No available tickets")  
         
    
    def status(self):
        print(f"The available seats are {self.seats}")
    
    def cancelTicket(self,ticket_list):
        ques=input("Would you like to cancel your ticket?(Y/N)\n")
        
        if ques.capitalize()=="Y":
            q=int(input("Which ticket would you like to cancel?\n"))
            if q not in ticket_list:
                print("Invalid")
            else:
                cancel_ticket=q
                self.seats+=1
                ticket_list.append(q)
                ticket_list.sort()
                print(f"The available tickets are {self.seats} that is {ticket_list} and the new ticket number available is {cancel_ticket}")

            print("********")
        elif ques.capitalize()=="N":
            print("Thank You. The available ticket is same i.e. ", self.seats)
            print("********")
        else:
            print("Invalid")
    

city=Train("Rajdhani Express", 90, 4)
ticket_list=[2,4,6,8]
city.getInfo()
city.fareInfo()
city.bookTicket(ticket_list)
city.status()
c=input("Do you want to access regarding Cancellation? (Y/N) \n")
if c.capitalize()=="Y":
    city.cancelTicket(ticket_list)
elif c.capitalize()=="N":
    print("You are ready for the travel. Happy Journey")
else:
    print("Invalid answer")

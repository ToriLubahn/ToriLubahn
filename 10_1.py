#Tori Lubahn's 10_1.py program

#class Cafe that can set 2 different drinks and their prices,
#it also includes 2 options that can reduce the price if you should choose to use them
class Cafe:
    #PRIVATE VARIABLES
    #This private variable includes each of the drink options and their prices in a dictionary
    drink_dict = {
    "Frappuccino" : 3.75,
    "Latte" : 4.25,
    "Cappuccino" : 4.75,
    "Hot Chocolate" : 3.25
    }
    #A private variable that is the empty string for mydrink1
    mydrink1 = ""
    #A private variable that is the empty string for mydrink2
    mydrink2 = ""

    #GET SET VARIABLES
    #This methods sets what the first drink is. Within the function, it sets the originally 
    #empty variable mydrink1 to the input drink.
    def set_mydrink1(self, drink):
        self.mydrink1 = drink
    #This methods sets what the second drink is. Within the function, it sets the originally 
    #empty variable mydrink2 to the input drink.
    def set_mydrink2(self, drink):
        self.mydrink2 = drink
    #This method gets the drink that was set in set_mydrink1 and returns the private variable mydrink1.
    def get_mydrink1(self):
        return self.mydrink1
    #This method gets the drink that was set in set_mydrink2 and returns the private variable mydrink2.
    def get_mydrink2(self):
        return self.mydrink2

    #2 OTHER METHODS
    #This function can derve as a buy one drink get the other 30% off
    #It has to input arguments: drink1 and drink2
    def deal_1(self, drink1, drink2):
        #it starts the total counter at 0 
        total = 0
        #sets the drink1_price to the price in the dictionary at drink1
        drink1_price = self.drink_dict[drink1]
        #If there is no second drink, the price of the second drink is 0
        if drink2 == 0:
            drink2_price = 0
        #sets the drink2_price to the price in the dictionary at drink2
        else: 
            drink2_price = self.drink_dict[drink2]
        #the total is equal to the sum of the first drink plus 30% off the price of the second drink
        total = drink1_price + (drink2_price) * 0.7
        #return the total number
        return total
    
    #this function is if the costumer is part of the memeber program, then they get 10% off their overall order
    #There are 2 imput arguments: drink1 and drink2
    def member_program(self, drink1, drink2):
        #The new_total is what was the result of the deal1 total with 10% less cost
        total = self.deal_1(drink1, drink2)
        new_total = total * 0.9
        #return the new_total
        return new_total



#DEMO
#this demo program is meant to simulate how the Cafe class would be utilized to take an order at a Cafe
def main():
        #storibucks is the name of the cafe that utilizes class Cafe()
        storibucks = Cafe()

        #Asks the user for an input for drink1 and gives them the options to type out
        drink1 = input("Welcome to S-tori-bucks! \nOut of these options: Frappuccino, Cappuccino, Latte, or Hot Chocolate (case sensitive), \nWhat drink would you like: ")
        #sets the input drink into the set drink1 function
        storibucks.set_mydrink1(drink1)

        #Tells the costumer that there is a sale today that is buy one get one 30% off
        print("We have a sale today that is buy a drink get the second drink 30 percent off.")
        #asks the user for an imput if they would like to place an order for a 2nd drink
        deal1_ask = input("Would you like to participate? Yes or No (case sensitive): ")
        #if the user input yes then the program asks what drink they would like
        if deal1_ask == "Yes":
            drink2 = input("What is the drink you would like to add to your order?: ")
            #sets the mydrink2 to the input drink
            storibucks.set_mydrink2(drink2)
            #This is nessesary for the last line of code returning the whole order if the costumer orders a 2nd drink
            drink2_ = " and a " + str(storibucks.get_mydrink2())
            #the deal_total uses the deal1 function in the class
            deal_total = storibucks.deal_1(drink1, drink2)
        #if the user does not want to buy a second drink
        else:
            #the cose of drink2 is 0
            drink2 = 0
            #there is an empty string for drink2_
            drink2_= ""
            #sets mydrink2 to nothing
            storibucks.set_mydrink2(drink2)
            #The deal is just the cost of the first drink
            deal_total = storibucks.deal_1(drink1, drink2)
            pass
        
        #the member deal asks for an input from the costumer for if they want to join the member program for 0% off the overall order Yes or No
        memeber_deal = input("Would you like to earn 10 percent off of your order by joining the rewards program? Yes or No: ")
        #If they input yes it subtracts 10% from their total using the member program function in the class and rounds to 2 decimal places 
        if memeber_deal == "Yes":
            newtotal = storibucks.member_program(drink1, drink2)
            newtotal = (f'{newtotal:.2f}')
        #if they dont input yes, then the deal total is the newtotal rounded to 2 decimal places
        else: 
            newtotal = deal_total
            newtotal = (f'{newtotal:.2f}')
        #prints out the order that the costumer placed with the total
        print("You ordered a " + str(storibucks.get_mydrink1()) + str(drink2_) + " and your total is: $" + str(newtotal))

#runs the demo program main function
if __name__ == "__main__":
    main()





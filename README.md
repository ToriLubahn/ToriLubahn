GitHub link:


Discription of the class: 
    This class called Cafe is meant to hold a dictionary with all of the drinks and their costs in a 
private variable and return what the overall total cost is of the order. There are different modifications you can 
add to your drink order such as adding another drink, adding a sale option, and joining the members program. Each function, 
the get sets of 2 drinks, the sale option, and the member program all change what the overall cost of the order is. 

Discriptions of private variables:
drink_dict: The variable that is the dictionary that holds all of the drinks and their prices. This is accessed within the class 
    to be able to find the total cost.
mydrink1 = Origionally the empty string that the class later assigns the first drink with its associated cost to.
mydrink1 = Origionally the empty string that the class later assigns the second drink with its associated cost to.


Discriptions of the Methods:
2 get set Methods:
    def set_mydrink1(self, drink) : 
        This methods sets what the first drink is. Within the function, it sets the originally empty variable mydrink1 to the 
        input drink. The line of code for this is self.mydrink1 = drink.
    def get_mydrink1(self) :
        This method gets the drink that was set in set_mydrink1 and returns the private variable mydrink1. The line of code
        for this is: return self.mydrink1
    def set_mydrink2(self, drink) : 
        This methods sets what the second drink is. Within the function, it sets the originally empty variable mydrink2 to the 
        input drink. The line of code for this is self.mydrink2 = drink.
    def get_mydrink2(self) :
        This method gets the drink that was set in set_mydrink2 and returns the private variable mydrink2. The line of code
        for this is: return self.mydrink2

2 other methods:
    def deal_1(self, drink1, drink2) :
        This method serves as a buy one drink get the second one 30 percent off. It takes in 2 arguments, the first drink as a 
        string and the second drink as a string. It takes the cost from the dictionary for the 2 drinks and subtracts 30% from the 
        cost of the 2nd drink. It returns the total.
    def member_program(self, drink1, drink2):
        This method serves as a 10% the overall cost of the order if the costumer is part of the member program. It takes in 2 arguments, 
        the first drink as a string and the second drink as a string. It takes the cost from the new deal total and subtracts 10% from the
        overall cost. It returns the new total.


Demo Program:
    Discription:
        This demo program is meant to simulate how the Cafe class would be utilized to take an order at a Cafe. It asks for input for 
        a first drink, it offers a sale that is buy one get one 30% off with input on whether or not you want to buy a second drink, it asks 
        if you are part of the member program and would subtract 10%off the total order if you are, and finally it retuns the overall order and 
        its total. The inputs are all case sensitive. It also rounds the total to 2 decimal places. 

How to run:
        You import the 10_1.py file first. Then you open an IDE such as IDLE or terminal and type in python3 10_1.py and the demo program will run.

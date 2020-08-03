"""
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. 
The “display table” is a table whose row entries denote how many of each food item each table ordered. 
The first column is the table number and the remaining columns correspond to each food item in alphabetical order. 
The first row should be a header whose first column is “Table”, followed by the names of the food items. 
Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.
"""

class Solution:
    def displayTable(self, orders):
        ans = []
        
        # key: table number, value: order in text
        tableToOrders = {}
        
        for order in orders: 
            table = order[1]
            dish = order[2]
            
            if table not in tableToOrders: 
                tableToOrders[table] = [dish]
            else: 
                tableToOrders[table].append(dish)
            
        
        allDishes = list(tableToOrders.values())
        allDishes = list(set([item for sublist in allDishes for item in sublist]))
        allDishes.sort()
        allDishes.insert(0, "Table")
        ans.append(allDishes)
        
        #sort keys
        allKeys = [int(key) for key in tableToOrders]
        allKeys.sort()
        
        for key in allKeys: 
            curArr = [str(key)]
            for i in range(1, len(allDishes)): 
                curArr.append(str(tableToOrders[str(key)].count(allDishes[i])))
                
            
            ans.append(curArr)
        
        return ans
                
        
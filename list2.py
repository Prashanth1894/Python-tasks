#4).List1 = [äpples ,"bananas", ""pineapples""]
#Shopping list = [ apples, apples, bananas, apples, pear, pineapples, pear, apples,banana]
#count the no.of times list1 elements are present in ShoppingList
#ex: apples ==> 4 times in ShoppingList

List1 = ["apples","bananas","pineapples","pear"]
Shoppinglist = [ "apples","apples", "bananas", "apples", "pear", "pineapples", "pear", "apples","bananas"]

for i in List1:
   count = 0
   for j in Shoppinglist:
       if i==j:
           count=count+1
   print(i,":",count)
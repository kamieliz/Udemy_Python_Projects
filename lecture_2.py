# print formatting and special characters
stock_price = "1100"
#print(f"Today's price for google stock is: {stock_price}")

today_price = "1100"
yesterday_price = "1000"
print("Today's price:", today_price, "yesterday's price:", yesterday_price)
print("Today's price: {}, yesterday's price: {}".format(today_price,yesterday_price))
# print(f"Today's price: {today_price}, yesterday's price: {yesterday_price}")
print("my name is jon snow and \n\tnot only do i know nothing but \n\t\tI also do nothing")
print("the day is\\n going so well")
name_of_book = "Harry Potter"
name_of_book.upper()
name_of_book = name_of_book[::-1]
new_name_of_book = name_of_book
new_name_of_book.lower()
name_of_book = new_name_of_book.upper()
new_name_of_book = name_of_book[::-1]
print(name_of_book)
print(new_name_of_book) 

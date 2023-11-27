from main import Bored


b = Bored()

# print(b.get_activity())
# print(b.get_activity_by_type("social"))
# print(b.get_activity_by_id(key=5881028))
# print(b.get_activity_by_accessibility(1))
# print(b.get_activity_by_price(0.0))
print(b.get_activity_by_price_range(minprice=0, maxprice=0.1))

discount=int(input("enter discount value:"))
sales_tax=float(input("enter sales tax:"))
price=int(input("enter price:"))
weight_product=float(input("enter weight:"))
shipping_cost=int(input("enter shipping cost:"))
base_ship_cost=int(input("enter base cost:"))
total_price=lambda price,discount:price-((discount/100)*price)
print(f"ans1:{total_price(price,discount)}")

price_after_sales_tax=lambda price,sales_tax:price+(sales_tax*100)
print(f"ans2{price_after_sales_tax(price,sales_tax)}")

ship_cost=lambda shipping_cost,weight,base_ship_cost:base_ship_cost+(weight*shipping_cost)
print(f"ans3:{ship_cost(shipping_cost,weight_product,base_ship_cost)}")



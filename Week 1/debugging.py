def get_sale_price(original_price, percent_discount):
  original_price = float(original_price)
  percent_discount = float(percent_discount)
  original_price -= (original_price * (percent_discount / 100))
  return original_price

if __name__ == '__main__':
    item_count = int(input())
    items = []

    for i in range(item_count):
        items.append(input().split())
    for item in items:
        price, discount = item
        sale_price = get_sale_price(price, discount)
        print(int(round(sale_price, 0)))
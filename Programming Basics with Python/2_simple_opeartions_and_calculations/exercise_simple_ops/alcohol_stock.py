price_whiskey = float(input())
litres_beer = float(input())
litres_wine = float(input())
litres_rakia = float(input())
litres_whiskey = float(input())
#
price_whiskey_litres = price_whiskey * litres_whiskey
#
price_rakia = price_whiskey / 2
price_rakia_litres = price_rakia * litres_rakia
#
price_wine = price_rakia - 0.40 * price_rakia
price_wine_litres = price_wine * litres_wine
#
price_beer = price_rakia - 0.80 * price_rakia
price_beer_litres = price_beer * litres_beer
#
money = float( price_whiskey_litres + price_rakia_litres + price_beer_litres + price_wine_litres )
print(f'{money:.2f}')


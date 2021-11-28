# $ to LV.
# cover = квадратно каре $9
# garment = правоъгълна покривка $7
#
leva = float(1)
dollars = float(leva * 1.85)
#
rectangular_tables = int(input())
#
height_rectangular_tables = float(input())
height_rectangular_tables_plus60 = height_rectangular_tables + 0.60
#
width_rectangular_tables = float(input())
width_rectangular_tables_plus60 = width_rectangular_tables + 0.60
#
side_cover = height_rectangular_tables / 2 # the one side of the square
#
covers_area = side_cover * side_cover
garments_area = height_rectangular_tables_plus60 * width_rectangular_tables_plus60
# P R I C E of the garments and covers together:
price_garments = ( rectangular_tables * garments_area * 7 )
price_covers = ( rectangular_tables * covers_area * 9 )
price_all = price_covers + price_garments
price_all_leva = price_all * dollars
#
print(f'{price_all:.2f} USD')
print(f'{price_all_leva:.2f} BGN')
from ch_5_ex_1 import get_deaths, get_cheese

deaths = AnnualStats( get_deaths() )
cheese = AnnualStats( get_cheese() )

print("Year Range", deaths.min_year(), deaths.max_year())
print("Average W75 Deaths", deaths.mean())

print("Median Cheese Consumption", cheese.median())
print("Mean Cheese Consumption", cheese.mean())

print(deaths )

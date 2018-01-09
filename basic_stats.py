"""Chapter 5 example 2.
Import stats library functions from ch_5_ex_1 module.
Import data acquisition from ch_5_ex_1 module.
Compute some simple descriptive statistics.
"""
from ch_5_ex_1 import mean, mode, median
from ch_5_ex_1 import get_deaths, get_cheese

year_deaths = list( get_deaths() )
years = list( year for year, death in year_deaths )
deaths= list( death for year, death in year_deaths )
print( "Year Range", min(years), "to", max(years) )
print( "Average Deaths {:.2f}".format( mean( deaths ) ) )
year_cheese= get_cheese()

print( "Average Cheese Consumption", 
    mean( [cheese for year, cheese in year_cheese] ) )

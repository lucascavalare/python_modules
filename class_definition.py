from ch_5_ex_1 import get_deaths, get_cheese

deaths = AnnualStats( get_deaths() )
cheese = AnnualStats( get_cheese() )

print("Year Range", deaths.min_year(), deaths.max_year())
print("Average W75 Deaths", deaths.mean())

print("Median Cheese Consumption", cheese.median())
print("Mean Cheese Consumption", cheese.mean())

print(deaths )

def stddev(self):
  μ_x = self.mean()
  n = len(self.data)
  σ_x= math.sqrt( sum( (x-μ_x)**2 for x in self.data )/n 
  return σ_x
    
def stdscore(self):
  μ_x= self.mean() 
  σ_x= self.stddev()
  return [ (x-μ_x)/σ_x for x in self.data ]
        
"""Print how this function works."""
print( cheese.stdscore2() )

print(cheese.stdscore())
                 
                 

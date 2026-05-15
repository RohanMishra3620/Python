# Two Series object, Population stores the details of four metro cities
# of India and another object AvgIncome stores the total average
# income reported in four years in these cities .Calculate income per
# capita for each of these metro cities.

import pandas as pd
index=["Delhi", "Noida", "Ghaziabad", "Mumbai"]
Population = pd.Series([100000, 200000, 120000, 900000],index=index)
AvgIncome = pd.Series([100000000, 20000000, 7000000, 9000000],index=index)
print("per_capita_income\n",AvgIncome / Population)
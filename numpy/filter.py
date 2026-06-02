import numpy as np
salaries = np.array([50000, 30000,25000,12000,43000,32000,70000,120000])
average = salaries.mean()
highest_paid = salaries.max()
# highly_paid = salaries[salaries > average]
lowly_paid = salaries[salaries < average]
highly_paid = salaries[salaries > 50000]
print(average)
print(highest_paid)
print(highly_paid)
print(lowly_paid)
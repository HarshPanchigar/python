import healthutils

bp = [120, 145, 138, 150, 132, 142, 155, 128, 135, 148, 160, 118, 141, 137, 146]

high , low = healthutils.high(bp)
average = healthutils.avg(bp)
high_count = healthutils.count_high(bp)

print("Highest Blood Pressure:", high)
print("Lowest Blood Pressure:", low)
print("Average Blood Pressure:", round(average, 2))
print("Number of patients with BP greater than 140:", high_count)
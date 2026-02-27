import statistics
# measures of central tendency
numbers = [9, 7, 4, 11, 10, 15, 4, 26, 25]
# mean
mean = sum(numbers)/ len(numbers)
print(mean)

#median
median = statistics.median(numbers)
print(median)

#mode
mode = statistics.mode(numbers)
print(mode)
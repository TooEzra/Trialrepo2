import statistics

# Sample dataset (can be loaded from file)
data = [4, 5, 2, 7, 5, 6, 8, 5, 4, 6]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
variance = statistics.variance(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
# numbers =  [i  for i in range (5)]
# # Generator version:
# numbers =  (i for i in range (5))

gen =  (x*x for x in range (3))

print(next(gen))
print(next(gen))
print(next(gen))

# list(gen)
# list(gen)
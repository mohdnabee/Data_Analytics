a =  [3,5,2,21]

# b =  a 
# b[1] =  666 
#  The most  common bug  (both  a and b  change )

#  use this .copy()
b =  a.copy()
b[1] =  55
#  now changes do not effct  the a 
print(a)   
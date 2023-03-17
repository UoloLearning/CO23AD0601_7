totalCandies= 36
visitors = 8
candiesPerVistor=int(totalCandies/visitors)
print("Candies each visitor will get: ",candiesPerVistor)
candiesLeft = totalCandies - (candiesPerVistor*visitors)
print("Candies left after distributing: ",int(candiesLeft))

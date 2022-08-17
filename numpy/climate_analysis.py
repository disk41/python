import numpy as np

east =[73,67,43]
west =[91,87,64]
north =[102,43,37]
south=[63,96,70]

w1,w2,w3 =0.3 ,0.2, 0.5

weights =[w1, w2 ,w3] 

def crop_yield(region,weights):
  result =0
  for x, w in zip(region,weights):
    result +=x*w
  return result

crop_yield(east, weights)

crop_yield(west, weights)

crop_yield(north, weights)

crop_yield(south, weights)

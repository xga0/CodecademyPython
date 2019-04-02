def cost_of_ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.5 + 20
    return cost
  elif weight <= 6:
    cost = weight * 3 + 20
    return cost
  elif weight <= 10:
    cost = weight * 4 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
  return cost
# test the function
print(cost_of_ground_shipping(8.4))

cost_of_premium_ground_shipping = 125

def cost_of_drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.5
    return cost
  elif weight <= 6:
    cost = weight * 9
    return cost
  elif weight <= 10:
    cost = weight * 12
    return cost
  else:
    cost = weight * 14.25
  return cost
# test the function
print(cost_of_drone_shipping(1.5))

def cheapest_shipping_method(weight):
  cost_of_ground = cost_of_ground_shipping(weight)
  cost_of_drone = cost_of_drone_shipping(weight)
  if cost_of_ground > cost_of_premium_ground_shipping and cost_of_drone > cost_of_premium_ground_shipping:
    return "Your cheapest shipping method is Premium Ground Shipping, and your shipping fee will be ${}.".format(cost_of_premium_ground_shipping) 
  elif cost_of_drone > cost_of_ground and cost_of_premium_ground_shipping > cost_of_ground:
    return "Your cheapest shipping method is Ground Shipping, and your shipping fee will be ${}.".format(cost_of_ground) 
  elif cost_of_ground > cost_of_drone and cost_of_premium_ground_shipping > cost_of_drone:
    return "Your cheapest shipping method is Drone Shipping, and your shipping fee will be ${}.".format(cost_of_drone) 
# test the function
print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))



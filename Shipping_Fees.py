weight = 4.8
cost_ground_premium = 125.00
#Ground Shipping costs

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >= 3 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight >=7 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping: $" + str(round(cost_ground,2)))

print("Ground Shipping Premium: $" + str(round(cost_ground_premium,2)))
#Drone Shipping costs

if weight <= 2:
  cost_drone = weight * 4
elif weight >= 3 and weight <= 6:
  cost_drone = weight * 9
elif weight >= 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $" + str(round(cost_drone,2)))


#Shipping an item of 4.8lbs = $34.40 by ground shipping 
#Shipping an item of 41.5lbs = $217.12 by ground shipping








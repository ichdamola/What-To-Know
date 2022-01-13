def laptoprentals(times):
  stretch_times = []
  time_points = {}
  
  if times == [[]]:
    return 0
  
  for time in times:
    stretch_times.append([num for num in range(time[0], time[1])])
    
  for stretch_time in stretch_times:
    for time_point in stretch_time:
      if time_point in time_points.keys():
        time_points[time_point] += 1
      else:
        time_points[time_point] = 1
  
  print(time_points)
  max_laptop = 0
  
  for time_point in time_points.values():
    if time_point > max_laptop:
      max_laptop = time_point 
  
  return max_laptop

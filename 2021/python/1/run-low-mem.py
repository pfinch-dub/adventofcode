depth_file_name = 'depths.txt'

prev_depth = 0
count = 0
with open(depth_file_name) as depth_file:
  for line in depth_file:
    depth = int(line.rstrip())
    if prev_depth != 0 and depth > prev_depth:
      count += 1
    prev_depth = depth

print(count)
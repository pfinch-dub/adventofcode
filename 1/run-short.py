depth_file_name = 'depths.txt'
depths = list(map(lambda x : int(x.rstrip()), open(depth_file_name).readlines()))
count = sum([(lambda x,y: 1 if x > y else 0)(x,y) for y,x in zip(depths, depths[1:])])
print(count)
commands_file_name = 'commands.txt'

command_lookup = {
  'forward': {'position': 'horizontal', 'move': 1 },
  'up': {'position': 'depth', 'move': -1 },
  'down': {'position': 'depth', 'move': 1 }
}

position = {
  'horizontal': 0,
  'depth': 0
}

with open(commands_file_name) as commands_file:
  for line in commands_file:
    command, value = line.rstrip().split()
    position[command_lookup[command]['position']] += int(value) * command_lookup[command]['move']

print(position['horizontal'] * position['depth'])
def abbrev_name(name):
  name_list = name.split(' ')
  for index, el in enumerate(name_list):
    name_list[index] = el[0:1]
  return '.'.join(name_list)
def counting_sheep (number_int, mult, tracker):

  to_check = number_int * mult
  to_check = str(to_check)

  for char in to_check:
    if char not in tracker:
      tracker.append(char)

  if len(tracker) == 10:
    return to_check

  return counting_sheep(number_int, mult +1, tracker)



with open('result.tkt','w') as fr:
  with open("A-large-practice.in", 'r') as f:
    for line in f.readlines():
      print(line)
      for l in range(len(line)):
        number_int= int(line.replace('\n','').strip())
        mult = 1
        tracker = []
        if number_int == 0 :
          fr.write(str('INSOMNIA'))
        else:
            mult = 1
            tracker = []
            result = counting_sheep(number_int, mult, tracker)
            fr.write(str(result))
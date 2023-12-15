import math
def area(height,width,cover):
  numbe_of_cans = (height*width)/cover
  round_number_of_cans = math.ceil(numbe_of_cans)
  print(f'You\'ll need {round_number_of_cans} cans of paint.')

test_h = int(input('Height of wall (m)')) 
test_w = int(input('Width of wall (m)')) 
coverage = 5
area(height=test_h, width=test_w, cover=coverage)

result = None
num = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


result = ''
num = float(text_prompt('Digite um número'))
while num > 0:
  if num % 2 == 0:
    result = '0' + str(result)
    num = num / 2
  else:
    result = '1' + str(result)
    num = num - 1
    num = num / 2
print(result)

0 % 2 == 0

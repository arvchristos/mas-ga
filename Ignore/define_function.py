from Ellipse import Ellipse

def calculate(value):
  schema = Ellipse(c_aux = value)
  return schema.mas()



if __name__ == '__main__':
  print(calculate(0.67))
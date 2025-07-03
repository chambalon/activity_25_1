def generator_func():
  for i in range(5):
    yield i
    
for item in generator_func():
    print(item)
  
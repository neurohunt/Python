def coffee_bot():
  print('Welcome to the cafe')
  size = get_size()
  drink_type = get_drink_type()
  print(f"Alright, that's a {size} {drink_type}!")
  name = input("Can I get your name please?")
  print(f"Thanks, {name}! Your drink will be ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == "a":
    return "small"
  if res == "b":
    return "medium"
  if res == "c":
    return "large"

  
def order_latte():
  res = input("""And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
""")
  if res == "a":
    return 'latte'
  if res == "b":
    return 'non-fat latte'
  if res == "c":
    return 'soy latte'


def get_drink_type():
  res = input("""What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte
""")
  if res == "a":
    return 'brewed coffee'
  if res == "b":
    return 'mocha'
  if res == "c":
    return order_latte()

#Function end

coffee_bot()

import random
from module_for_7 import logo
# should_continue = True
# while should_continue:
game = input("Do you want to play the game? Type 'y' or 'n'")
if game == 'y':
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  a = random.choice(cards)
  b = random.choice(cards)
  c = random.choice(cards)
  d = random.choice(cards)
  l = random.choice(cards)
  m = random.choice(cards)
  n = random.choice(cards)
  o = random.choice(cards)
  p = random.choice(cards)
  q = random.choice(cards)
  r = random.choice(cards)
  s = random.choice(cards)
  t = random.choice(cards)

  ma = [l,m]
  ma_2 = [n,o,p]
  ma_3 = [q,r,s,t]

  user = [a,b]
  comp_cards = [ma,ma_2,ma_3]
  comp = list(random.choice(comp_cards))

  user_sum = sum(user)
  comp_sum = sum(comp)

  print(f"Your cards : {user}, current score: {user_sum}")
  print(f"Computer's first card: {c}")
  y_or_n = input("Do you want another card? Type 'y' or 'n':")
  if y_or_n == "y":
    e = random.choice(cards)
    user = [a,b,e]
    user_sum1 = sum(user)
    print(f"Your cards : {user}, current score: {user_sum1}")
    print(f"Computer's final hand: {comp}, final score : {comp_sum}")
    if user_sum1 > comp_sum and user_sum1 < 21:
      print("You win!")
      print("Computer loose")

    # if user_sum1 > 21:
    #   print("The score went above 21")
    #   print("You loose")
    #   print("Computer Wins")

    elif user_sum1 == comp_sum:
      print("It's a draw")

    elif comp_sum > user_sum1 and comp_sum < 21:
      print("The opponent went over you")
      print("You loose")

    elif comp_sum > 21 and user_sum1 < 21:
      print("You win")
      print("Computer loose")

    elif user_sum == comp_sum or user_sum1 > 21 and comp_sum > 21:
      print("It's a draw")

  elif y_or_n == "n":
    print(f"Computer's final hand: {comp}, final score : {comp_sum}")
    print(f"Your final hand: {user}, final score : {user_sum}")

    if comp_sum > user_sum and comp_sum < 21:
      print("The opponent went over you")
      print("Computer wins")

    elif comp_sum < user_sum and user_sum <21:
      print("You win!")
      print("Computer loose")

    elif user_sum == comp_sum or user_sum>21 and comp_sum > 21:
      print("It's a draw")

    elif comp_sum > 21 and user_sum<21:
      print("You win!")
      print("Computer went over 21")

    elif user_sum > 21 and comp_sum<21:
      print("You loose!")
      print("You went over 21")

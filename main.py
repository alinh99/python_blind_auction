from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

new_lst_bid = []
def new_infor(name_players, bid_players):
  new_dict_bid = {}
  new_dict_bid["name"] = [name_players]
  new_dict_bid["bid"] = [bid_players]
  new_lst_bid.append(new_dict_bid)
  return new_lst_bid

def other_info(name_players, bid_players):
  # append value to list
  for _ in [name]:
    [name].append(name_players)
  for _ in [bid]:
    [bid].append(bid_players)
  return [bid]
def cal_max_bid(name_players, bid_players):
  other = other_info(name_players, bid_players)
  max_bids = max(other)
  return max_bids
print(logo)
re_play = False
while not re_play:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  new_infor(name, bid)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if other_bidders == 'yes':
    other_info(name, bid)
    clear()
  else:
    cal_max = cal_max_bid(name, bid)
    print(f"The winner is {name} with a bid of ${cal_max}")
    re_play = True
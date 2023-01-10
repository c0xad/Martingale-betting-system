import requests

class Martingale:
  def __init__(self, initial_bet, goal, max_bet):
    self.initial_bet = initial_bet
    self.goal = goal
    self.max_bet = max_bet
    self.total_bet = 0
    self.total_won = 0
  
  def bet(self):
    bet = self.initial_bet
    while True:
      self.total_bet += bet
      if self.total_bet > self.goal:
        return -1, self.total_won
      result = place_bet(bet)
      if result:
        self.total_won += bet
        return bet, self.total_won
      bet = min(bet*2, self.max_bet)

def place_bet(bet):
  # Send a request to the betting system API to place a bet
  response = requests.post(
    'https://example.com/api/place_bet',
    json={'amount': bet}
  )
  # Check the response to see if the bet was successful
  if response.status_code == 200:
    return True
  else:
    return False
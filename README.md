# Neopets Sticky Snowball Auto Buyer

Added Trudy's Surprise Auto Player into this program, it'll automatically complete Trudy's Surprise for you as long as you haven't completed it for the day. This will easily give your account the funds to auto buy snowballs for each day.

To enable this Auto Player into the program, inside of client.py change "self.doTrudy = False" to "self.doTrudy = True". This will enable the Auto Player to run anytime your account has Trudy's Surprise available. It's disabled by default on the off chance you don't want to automate Trudy's Surprise in the first place.

Auto buys sticky snowballs from the healing springs at a random interval every 30 - 35 minutes, once purchased the snowball gets deposited into your SDB.

Requirements:

- Python 3.8
- pip install requests

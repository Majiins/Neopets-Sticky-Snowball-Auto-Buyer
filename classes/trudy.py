class Trudy:
    def __init__(self, neo):
        self.neo = neo

    def doTrudy(self):
        resp = self.neo.get('trudys_surprise.phtml?delevent=yes')
        if resp.find('&slt=1') > 1:
            result = self.neo.GetBetween(resp, '/trudydaily/slotgame.phtml?id=', '" name="')
            resp = self.neo.get('trudydaily/slotgame.phtml?id=%s' % result, 'http://www.neopets.com/trudys_surprise.phtml?delevent=yes')
            results = self.neo.GetBetween(resp, '\'key\': \'', '\'};')
            self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'getslotstate', 'key': results}, 'http://www.neopets.com/trudydaily/slotgame.phtml?id=%s' % result)
            self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'beginroll'}, 'http://www.neopets.com/trudydaily/ajax/claimprize.php')
            self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'prizeclaimed'}, 'http://www.neopets.com/trudydaily/ajax/claimprize.php')
            print('Done Trudy\'s Surprise')
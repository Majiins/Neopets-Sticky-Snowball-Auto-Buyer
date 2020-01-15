from classes.neo import neo
import sys
import re
import random
import time

class client:
    def __init__(self):
        self.neo = neo()

    def doLogin(self):
        with open('settings/settings.txt', 'r') as f:
            settings = f.read().rstrip()
        account = self.neo.GetBetween(settings, '[account]', '[/account]')
        account = account.split('\n')[1:-1]
        username = account[0].split(';')[1].strip()
        password = account[1].split(';')[1].strip()
        proxy = account[2].split(';')[1].strip()
        if proxy != 'ip:port':
            self.neo.proxy(proxy)
        resp = self.neo.post('login.phtml', {'destination': '', 'username': username, 'password': password}, 'http://www.neopets.com/login/')
        if resp.find('id=\'npanchor\'') > 1:
            print('Logged in as %s' % username)
            return True
        else:
            input('Unable to login as %s. Press enter to exit..' % username)
            return False

    def buyBall(self):
        while True:
            resp = self.neo.post('faerieland/springs.phtml', {'type': 'purchase'}, 'http://www.neopets.com/faerieland/springs.phtml')
            if resp.find('buy one item every 30 minutes') > 1:
                print('You have already brought a snowball, sleeping for 30 minutes..')
                time.sleep(random.uniform(1800, 2100))
            else:
                resp = self.neo.get('faerieland/process_springs.phtml?obj_info_id=8429', 'http://www.neopets.com/faerieland/springs.phtml')
                self.depositInventory()
                print('Successfully purchased Sticky Snowball, sleeping for 30 minutes..')
                time.sleep(random.uniform(1800, 2100))

    def depositInventory(self):
        arr = 1
        resp = self.neo.get('quickstock.phtml')
        items = "<TD align=\"left\">"
        results = resp.count(items)
        if results:
            item_ids = re.findall('value="(.*)"><TD', resp)
            data = {}
            data['buyitem'] = 0
            for item in item_ids:
                data['id_arr[%s]' % arr] = item
                data['radio_arr[%s]' % arr] = 'deposit'
                arr += 1
            data['checkall'] = 'on'
            self.neo.post('process_quickstock.phtml', data, 'http://www.neopets.com/quickstock.phtml')
        if results:
            print('Deposited %s items to your SDB' % results)
        else:
            print('You don\'t have any items to deposit')


    def doBot(self):
        isLogged = self.doLogin()
        if isLogged:
            self.buyBall()

        if not isLogged:
            sys.exit()

if __name__ == '__main__':
    a = client()
    a.doBot()
    
class Broker:

    name='IB'
    stock_prices={'TCS':1000,'INFY':2000,'WIPRO':3000,'HCL':4000,'TECHM':5000}

    def __init__(self, account_name,money):
        self.name=account_name
        self.wallet=money
        self.portfolio={}

    def buy(self,stock_name):
        if self.wallet>self.stock_prices.get(stock_name):
            self.wallet=self.wallet-self.stock_prices.get(stock_name)
            self.portfolio[stock_name]=self.stock_prices.get(stock_name)
            print('buying '+stock_name+' at '+str(self.stock_prices.get(stock_name)))
            print('current wallet balance is '+str(self.wallet))
            
        else:
            print('insufficient balance')

    def sell(self,stock_name):
        if stock_name in self.portfolio:
            self.wallet=self.wallet+self.stock_prices.get(stock_name)
            del self.portfolio[stock_name]
            print('selling '+stock_name+' at '+str(self.stock_prices.get(stock_name)))
            print('current wallet balance is '+str(self.wallet))
        else:
            print('stock not present in portfolio')

abhi_acct=Broker('poko',4000)
abhi_acct.buy('TCS')
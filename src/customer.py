class Customer:
    def __init__(self,name=str,wallet=float,age=int):
        self.name=name
        self.wallet=wallet
        self.age=age
        self.energy=0

    def buy(self,item_name,shop,is_drink=True):
        item=shop.sell(item_name.lower(),self,is_drink)
        if item is not None:
            self.wallet-=item.price
            if is_drink:
                self.energy+=item.caffeine
            else:
                self.energy-=item.digestion


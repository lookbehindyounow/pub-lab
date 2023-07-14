class Customer:
    def __init__(self,name=str,wallet=float,age=int):
        self.name=name
        self.wallet=wallet
        self.age=age
        self.drunkness=0

    def buy(self,item_name,pub,is_drink=True):
        item=pub.sell(item_name.lower(),self,is_drink)
        if item is not None:
            self.wallet-=item.price
            if is_drink:
                self.drunkness+=item.alcohol
            else:
                self.drunkness-=item.rejuvination


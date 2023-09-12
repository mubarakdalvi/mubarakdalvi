class Customer:
    customer_id = None
    name = None
    address = None
    phone = None
    account = None

    def customer1(self,name,customer_id,phone,address,account):
        self.name = name
        self.customer_id = customer_id
        self.phone = phone
        self.address = address
        self.account = account
        print('Thanks you For opening New Bank Account', 'Happy Banking')
    def __del__(self):
        print('This account is deleted successfully','please dont try to delete customer details if found it is under procossed for deletion')
c1 = Customer()
c1.customer1(name='Mubarak Dalvi',phone=9146755486,customer_id=420,account=32542,address='flat,125')
del c1.customer_id
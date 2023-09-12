class Customer:
    def __init__(self):
        self.customer_id = None
        self.name = None
        self.address = None
        self.phone = None
        self.account = []

    def open_account(self,name,customer_id,phone,address,account):
        self.account.append(account)
        print(f'Thanks you For opening New Bank Account with name:- {name} phone number:- {phone} and your cust_id is :-{customer_id} and acoount number is :-{account} and your documents and furthure notices will be delivered to provided address {address} please confirm your address {address}  Happy Banking!')
    def delete_account(self,name,customer_id,phone,address,account):
        if account in self.account:
            self.account.remove(account)
            self.name.remove(name)
            self.address.remove(address)
            self.customer_id.remove(customer_id)
            self.phone.remove(phone)
            print(f'The account is {name}{address}{account}{customer_id}{phone} is deleted successfully, if you try to place a delete requested again it will be denied')
        else:
            print('Account does not exist')
    def __del__(self):
        print('This account is deleted successfully','please dont try to delete customer details if found it is under procossed for deletion')
c1 = Customer()
c1.open_account(name='Mubarak Dalvi',phone='9146755486',customer_id='420',account='32542',address='flat,125')
c1.delete_account('Mubarak Dalvi',420,9146755486,'flat,125',32542)
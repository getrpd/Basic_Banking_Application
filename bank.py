class Bank:
    name = 'National Bank'
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, account_number):
        for i in range(len(self.clients)):
            if name in self.clients[i].account.values() and account_number in self.clients[i].account.values():
                print("Authentication Successful ", self.clients[i])
                return self.clients[i]

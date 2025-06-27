import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        # Abre o arquivo e itera em cada linha
        with open(self.filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # separa pelos pontos-e-vírgulas
                parts = line.split(';')
                if len(parts) != 4:
                    # pula linhas mal formatadas
                    continue
                email, password, name, created = parts
                self.users[email] = (password, name, created)        

        
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
    
    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print('Email já existente')
            return -1
    
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
        
    def save (self):
        with open(self.filename, 'w') as f:
            for user in self.users:
                f.write(user+ ';' + self.users[user][0] + ';'+ self.users[user][1] + ';'+ self.users[user][2] + '\n')
    
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split('')[0]
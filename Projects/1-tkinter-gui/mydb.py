import json, os

class Database:

    def add_data(self,name,email,password):
        base_path = os.path.dirname(__file__)
        db_path = os.path.join(base_path, 'db.json')

        print("opening the db")
        with open(db_path,'r') as rf:
            database = json.load(rf)
            print("db opened and loaded")

        if email in database:
            print("email already exists")
            return 0
            
        else:
            database[email] = [name,password]
            with open(db_path,'w') as wf:
                json.dump(database,wf)
                print("new email dumped")
            return 1

    def search(self,email,password):
        base_path = os.path.dirname(__file__)
        db_path = os.path.join(base_path, 'db.json')

        with open(db_path,'r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0



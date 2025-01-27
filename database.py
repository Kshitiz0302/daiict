from firebase import firebase
import hashlib


class Database:

    def __init__(self):
        # self.fb = 'http://127.0.0.1:27017/'
        self.fb = firebase.FirebaseApplication(
            'https://daiict-db.firebaseio.com/', None)

    def get_data(self, category):
        data = self.fb.get('/{}'.format(category), None)
        print("===============================l==l==l=ll=l=l=l=l================"+data);
        return data

    def write_data(self, category, data, flag=False):
        if not flag:
            gen = data['name']
            hash_object = hashlib.sha1(gen.encode())
            hex_dig = hash_object.hexdigest()
        else:
            hex_dig = flag
        result = self.fb.put('/' + category, hex_dig[-15:], data)
        return True


if __name__ == '__main__':
    db = Database()
    db.write_data('enterprises', {
        'name': 'P&G Inc.',
    })

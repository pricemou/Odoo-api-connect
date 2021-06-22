import xmlrpc.client

#https://gist.github.com/ilyasProgrammer/cf6647356c9a3722f597f72b7685a4c3
#https://www.odoo.com/fr_FR/forum/aide-1/how-do-you-create-and-update-one2many-and-many2many-records-with-python-3-142796


#connection details
server_url = 'http://172.17.0.1:8069'
db = 'Telemedecine'
login = 'scameleons3@gmail.com'
password = '123'

#endpoints
common_ep = xmlrpc.client.ServerProxy(server_url+'/xmlrpc/2/common')
object_ep = xmlrpc.client.ServerProxy(server_url+'/xmlrpc/2/object')


#login
uid = common_ep.authenticate(db, login, password,{})

def create_utilisateur():
    #define new Partner
    new_contact = {
    'name': 'Jane Smith',
    'ref': '54321',
    }

    #create New Contact, under New Partner
    new_contact_id = object_ep.execute_kw(db, uid, password, 'res.partner', 'create', [new_contact])
    print(new_contact_id)


def odoo_update():
    #define new Partner
    updated_information = {
        'phone': '555 123 1234',
        }
    existing_contact_id = object_ep.execute_kw(db, uid, password, 'res.partner', 'search', [[['ref','=','54321']]])
    teste  = object_ep.execute_kw(db, uid, password, 'res.partner', 'write', [existing_contact_id, updated_information])
    print(teste)


def search():

    # ids = object_ep.execute_kw(db, uid, password,
    # 'res.partner', 'search',
    # [[['is_company', '=', True]]],
    # {'limit': 2})

    record = object_ep.execute_kw(db, uid, password,'res.partner', 'search', [[]],{'fields': ['name']},{'limit':1},)

    # count the number of fields fetched by default
    # len(record)
    #find New Contact
    # existing_contact_id = object_ep.execute_kw(db, uid, password, 'res.partner', 'search', [()], {'fields': ['name']})
    # for cpt in existing_contact_id:
    #     print('----------------:',cpt)
    print('----------------:',record)
    

search()
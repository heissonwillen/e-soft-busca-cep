from address.models import Address
import json

with open("addresses.json") as addresses_file:
    addresses_json = json.load(addresses_file)


for address in addresses_json:
    address = Address(
        street=address['street'],
        neighborhood=address['neighborhood'],
        city=address['city'],
        description=address['description'],
        complement=address['complement'],
        cep=address['cep'],
        number=address['number'],
        uf=address['uf'],
    )
    address.save()

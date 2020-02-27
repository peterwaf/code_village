customers = {
	54856: {
		'First Name ': 'Peter',
		'Last Name ': 'Wafula',
		'Mobile No. ': 722412676,
		'Id Number': 287856,
		'Unique Id': 54856,
		'Account': {
			'Account Number': 1147896545,
			'Account Type': 'Current',
			'Currency': 'KES',
			'Currency Name': 'Kenya shillings',
			'Account Balance': 10000
		}
	},
	984562: {
		'First Name ': 'John',
		'Last Name ': 'Kissinger',
		'Mobile No. ': 74574548,
		'Id Number': 28795462,
		'Unique Id': 984562,
		'Account': {
			'Account Number': 14759856,
			'Account Type': 'Savings',
			'Currency': 'USD',
			'Currency Name': 'Kenya shillings',
			'Account Balance': 1000
		}
	}
}

for a,b in customers.items():
    print('Customer Id',a)
    for c,d in b.items():
        print(c,d)
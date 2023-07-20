env_reg = env['motorcycle.registry']
# 1. Creación de registro
env_reg.create({
    'registry_number' : 'RN0003',
    'vin': 'VIM29375',
    'first_name' : 'Karla',
    'last_name' : 'Cuerso',
    'current_mileage' : 1320
})
# 2. Mileage menor igual a 1000
env_reg.read_group([('current_mileage','<=',1000)],[],['current_mileage'])
# 3. Registries with VIN but not License plate
env_reg.read_group([('vin','!=',False),('license_plate','=',False)],['registry_number','vin','license_plate','last_name'],['last_name'])
# 4.
env_reg.read_group(['|',('vin','!=',False),('license_plate','!=',False)],[],['last_name'])
# 5.
env_reg['first_name'] = 'Jhon'
env_reg['last_name'] = 'Wick'
# 6.
env_reg.browse(4).unlink()
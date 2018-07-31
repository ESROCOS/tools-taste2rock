# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2


import imp

class IvData(object):
    '''Information from an iv.py file generated by TASTE'''

    # Module to load iv.py
    iv = None
    
    def __init__(self, iv_file):
        self.iv = imp.load_source('iv', iv_file)


    def list_functions(self):
        '''Returns all functions defined in the iv.py file'''
        return [self.name_with_case(f) for f in self.iv.functions]


    def list_interfaces(self, fun):
        '''Returns all interfaces for a function defined in the iv.py file'''
        return self.iv.functions[fun.lower()]['interfaces']


    def list_pi(self, fun):
        '''Returns all PIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.PI]


    def list_ri(self, fun):
        '''Returns all RIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.RI]


    def list_cyclic_pi(self, fun):
        '''Returns all cyclic PIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.PI and ifcs[i]['rcm'] == self.iv.cyclic]


    def list_sporadic_pi(self, fun):
        '''Returns all sporadic PIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.PI and 
            (ifcs[i]['rcm'] == self.iv.sporadic or ifcs[i]['rcm'] == self.iv.variator)]


    def list_protected_pi(self, fun):
        '''Returns all protected PIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.PI and ifcs[i]['rcm'] == self.iv.protected]


    def list_unprotected_pi(self, fun):
        '''Returns all unprotected PIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.PI and ifcs[i]['rcm'] == self.iv.unprotected]


    def list_async_pi(self, fun):
        '''Returns all asyncronous (cyclic and sporadic) PIs for a function defined in the iv.py file'''
        return self.list_cyclic_pi(fun) + self.list_sporadic_pi(fun)


    def list_sync_pi(self, fun):
        '''Returns all syncronous (protected and unprotected) PIs for a function defined in the iv.py file'''
        return self.list_protected_pi(fun) + self.list_unprotected_pi(fun)


    def list_sporadic_ri(self, fun):
        '''Returns all sporadic RIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.RI and 
            (ifcs[i]['rcm'] == self.iv.sporadic or ifcs[i]['rcm'] == self.iv.variator)]


    def list_protected_ri(self, fun):
        '''Returns all protected RIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.RI and ifcs[i]['rcm'] == self.iv.protected]


    def list_unprotected_ri(self, fun):
        '''Returns all unprotected RIs for a function defined in the iv.py file'''
        ifcs = self.iv.functions[fun.lower()]['interfaces']
        return [i for i in ifcs if ifcs[i]['direction'] == self.iv.RI and ifcs[i]['rcm'] == self.iv.unprotected]


    def list_async_ri(self, fun):
        '''Returns all asyncronous (cyclic and sporadic) RIs for a function defined in the iv.py file'''
        return self.list_cyclic_ri(fun) + self.list_sporadic_ri(fun)


    def list_sync_ri(self, fun):
        '''Returns all syncronous (protected and unprotected) RIs for a function defined in the iv.py file'''
        return self.list_protected_ri(fun) + self.list_unprotected_ri(fun)


    def has_interfaces(self, fun):
        '''Checks if a function has interfaces (returns list as Boolean)'''
        return self.list_interfaces(fun)


    def has_pi(self, fun):
        '''Checks if a function has PIs (returns list as Boolean)'''
        return self.list_pi(fun)


    def has_ri(self, fun):
        '''Checks if a function has RIs (returns list as Boolean)'''
        return self.list_ri(fun)


    def has_cyclic_pi(self, fun):
        '''Checks if a function has cyclic PIs (returns list as Boolean)'''
        return self.list_cyclic_pi(fun)


    def has_sporadic_pi(self, fun):
        '''Checks if a function has sporadic PIs (returns list as Boolean)'''
        return self.list_sporadic_pi(fun)


    def has_protected_pi(self, fun):
        '''Checks if a function has protected PIs (returns list as Boolean)'''
        return self.list_protected_pi(fun)


    def has_unprotected_pi(self, fun):
        '''Checks if a function has unprotected PIs (returns list as Boolean)'''
        return self.list_unprotected_pi(fun)


    def has_sync_pi(self, fun):
        '''Checks if a function has synchronous PIs (returns list as Boolean)'''
        return self.list_sync_pi(fun)


    def has_async_pi(self, fun):
        '''Checks if a function has asynchronous PIs (returns list as Boolean)'''
        return self.list_async_pi(fun)


    def has_sporadic_ri(self, fun):
        '''Checks if a function has sporadic RIs (returns list as Boolean)'''
        return self.list_sporadic_ri(fun)


    def has_protected_ri(self, fun):
        '''Checks if a function has protected RIs (returns list as Boolean)'''
        return self.list_protected_ri(fun)


    def has_unprotected_ri(self, fun):
        '''Checks if a function has unprotected RIs (returns list as Boolean)'''
        return self.list_unprotected_ri(fun)


    def has_sync_ri(self, fun):
        '''Checks if a function has synchronous RIs (returns list as Boolean)'''
        return self.list_sync_ri(fun)


    def has_async_ri(self, fun):
        '''Checks if a function has asynchronous RIs (returns list as Boolean)'''
        return self.list_async_ri(fun)


    def get_period_seconds(self, fun, pi):
        '''Returns the activation period of a PI in seconds'''
        return self.iv.functions[fun.lower()]['interfaces'][pi]['period'] / 1000.0


    def list_all_types(self):
        '''Returns all the types used in the interfaces of a TASTE IV'''
        types = set()
        for f in self.iv.functions:
            for i in self.iv.functions[f]['interfaces']:
                for p in self.iv.functions[f]['interfaces'][i]['in']:
                    types.add(self.iv.functions[f]['interfaces'][i]['in'][p]['type'])
                for p in self.iv.functions[f]['interfaces'][i]['out']:
                    types.add(self.iv.functions[f]['interfaces'][i]['out'][p]['type'])
        return types


    def list_in_params(self, fun, iface):
        '''Returns the list of input parameters of an interface'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['paramsInOrdered']


    def list_out_params(self, fun, iface):
        '''Returns the list of input parameters of an interface'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['paramsOutOrdered']


    def has_in_params(self, fun, iface):
        '''Checks if an interface has input parameters (returns list as Boolean)'''
        return self.list_in_params(fun, iface)


    def has_out_params(self, fun, iface):
        '''Checks if an interface has output parameters (returns list as Boolean)'''
        return self.list_out_params(fun, iface)


    def get_in_param_type(self, fun, iface, param):
        '''Returns the type of an input parameter'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['in'][param]['type']


    def get_out_param_type(self, fun, iface, param):
        '''Returns the type of an output parameter'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['out'][param]['type']


    def get_in_param_idx(self, fun, iface, idx):
        '''Returns the nth input parameter of an interface'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['paramsInOrdered'][idx]


    def get_out_param_idx(self, fun, iface, idx):
        '''Returns the nth output parameter of an interface'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['paramsOutOrdered'][idx]


    def get_in_param_type_idx(self, fun, iface, idx):
        '''Returns the type of the nth input parameter'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['in'][self.get_in_param_idx(fun, iface, idx)]['type']


    def get_out_param_type_idx(self, fun, iface, idx):
        '''Returns the type of the nth output parameter'''
        return self.iv.functions[fun.lower()]['interfaces'][iface]['out'][self.get_out_param_idx(fun, iface, idx)]['type']


    def asn_header(self):
        '''Returns the default type header generated by the ASN.1 compiler'''
        return 'dataview-uniq.h'


    def asn_type_name(self, type_name):
        '''Returns the C type name as generated by from an ASN.1 type name by TASTE'''
        return ('asn1Scc' + type_name).replace('-', '_')


    def asn_type_init(self, type_name):
        '''Returns the C type initialization function name as generated by TASTE'''
        return 'asn1Scc' + type_name + '_Initialize'


    def asn_context_header(self, fun):
        '''Returns the default type header of a function context'''
        return 'Context-' + fun.lower() + '.h'


    def asn_context_field(self, fun, prop):
        '''Returns a field of a constant function context'''
        return fun.lower() + '_ctxt.' + prop.lower();


    def taste_header(self, fun):
        '''Returns the name of the TASTE .h file of a function'''
        return fun.lower() + '.h'


    def taste_vm_header(self, fun):
        '''Returns the name of the TASTE internal .h file of a function'''
        return fun.lower() + '_vm_if.h'


    def taste_vm_pi(self, fun, pi):
        '''Returns the function name for the call to an internal TASTE PI function'''
        return fun.lower() + '_' + pi


    def taste_vm_async_ri(sef, fun, ri):
        '''Returns the function name for the call to an external RI in TASTE'''
        return 'vm_async_' + fun.lower() + '_' + ri

        
    def taste_vm_sync_pi(sef, fun, pi):
        '''Returns the function name for the call to a PI in TASTE'''
        return fun.lower() + '_' + pi

        
    def taste_vm_sync_ri(sef, fun, ri):
        '''Returns the function name for the call to an external RI in TASTE'''
        return 'vm_' + fun.lower() + '_' + ri

        
    def get_iface_period_seconds(self, fun, pi):
        '''Returns the period in seconds of a periodic interface provided by a function'''
        return self.iv.functions[fun.lower()]['interfaces'][pi]['period'] / 1000.0


    def get_taste_startup_function(self, fun):
        '''Returns the name of the startup function created by TASTE for each functional block'''
        return fun.lower() + '_startup'


    def get_remote_function(self, fun, ri):
        '''Returns the functional block to which an RI is connected'''
        remoteLower = self.iv.functions[fun.lower()]['interfaces'][ri]['distant_fv']
        return self.name_with_case(remoteLower)


    def get_remote_pi(self, fun, ri):
        '''Returns the functional block to which an RI is connected'''
        return self.iv.functions[fun.lower()]['interfaces'][ri]['distant_name']


    def list_properties(self, fun):
        '''Returns the properties (functional states) of a function'''
        return [info['fullFsName'] for info in self.iv.functions[fun.lower()]['functional_states'].values()]


    def has_properties(self, fun):
        '''Checks if a function has properties (returns list as Boolean)'''
        return self.list_properties(fun)


    def get_property_type(self, fun, prop):
        '''Returns the type of an input parameter'''
        return self.iv.functions[fun.lower()]['functional_states'][prop.lower()]['typeName']


    def list_required_functions(self, fun):
        '''Returs the list of functions from which a function has required interfaces'''
        req_functions = set()
        for ri in self.list_ri(fun):
            req_functions.add(self.get_remote_function(fun, ri))
        return req_functions


    def name_with_case(self, fun):
        '''Returns the name of a function with its original capitalization'''
        return self.iv.functions[fun.lower()]['name_with_case']

        
    def is_cyclic(self, fun, iface):
        '''Checks if an interface is cyclic'''
        return (self.iv.functions[fun.lower()]['interfaces'][iface]['rcm'] == self.iv.cyclic)

        
    def is_sporadic(self, fun, iface):
        '''Checks if an interface is sporadic'''
        return (self.iv.functions[fun.lower()]['interfaces'][iface]['rcm'] == self.iv.sporadic)


    def is_protected(self, fun, iface):
        '''Checks if an interface is protected'''
        return (self.iv.functions[fun.lower()]['interfaces'][iface]['rcm'] == self.iv.protected)


    def is_unprotected(self, fun, iface):
        '''Checks if an interface is unprotected'''
        return (self.iv.functions[fun.lower()]['interfaces'][iface]['rcm'] == self.iv.unprotected)
                

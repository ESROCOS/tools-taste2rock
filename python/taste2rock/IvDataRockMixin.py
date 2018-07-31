# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2


class IvDataRockMixin(object):
    '''Creation of identifiers for Rock code. Must be mixed with IvData'''

    PrimitiveTypes = {
        'T_Boolean': 'bool', 
        'T_Int8': 'int8_t', 'T_UInt8': 'uint8_t',
        'T_Int16': 'int16_t', 'T_UInt16': 'uint16_t', 
        'T_Int32': 'int32_t', 'T_UInt32': 'uint32_t', 
        'T_Int64': 'int64_t', 'T_UInt64': 'uint64_t',
        'T_Float': 'float', 'T_Double': 'double'}

    def function_name(self, fun):
        '''C++ name of a function component'''
        return self.name_with_case(fun);

    def port_name(self, fun, iface):
        '''C++ name of a port for a PI/RI'''
        return iface;

    def function_iface_name(self, fun, pi):
        '''Contactenation of function and interface name'''
        return self.name_with_case(fun) + pi[0].upper() + pi[1:]
        
    def function_task(self, fun):
        '''Name of the function task C++ class'''
        return self.name_with_case(fun) + 'Task'

    def trigger_port(self, fun, pi):
        '''Name of the C++ method of a trigger port for a cyclic PI'''
        return self.function_iface_name(fun, pi) + 'Trigger'

    def trigger_task(self, fun, pi):
        '''Name of the C++ method of a trigger task for a cyclic PI'''
        return self.function_iface_name(fun, pi) + 'Task'

    def function_namespace(self, function):
        '''Name of the C++ namespace for the function code'''
        return function.lower();
        
    def rock_type(self, typename):
        '''Name of a Rock type corresponding to an ASN.1 type'''
        if typename in self.PrimitiveTypes:
            return self.PrimitiveTypes[typename]
        else:
            if typename.startswith('Wrappers'):
                typename = typename.replace('Wrappers', 'Base')
            return (typename[0].lower() + typename[1:]).replace('_', '/')


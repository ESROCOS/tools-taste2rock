## =====================================================================
## H2020 ESROCOS Project
## Company: GMV Aerospace & Defence S.A.U.
## Licence: GPLv2
## ..................................................................
##  Template of the component.orogen file
## Inputs: 
## - iv: the IvData object
## - function: the function name
## - package: the Rock package name
## =====================================================================
<%                                                                    %># Generated from ${context._with_template.uri}
<%                                                                    %>
<%                                                                    %>name '${iv.function_namespace(function)}'
<%                                                                    %>
##
## Import types:
## - provided by the function
## - provided by other required functions
## - the function's configuration types (if needed)
##
<%                                                                    %>import_types_from 'std'
<%                                                                    %>import_types_from 'base'
<%                                                                    %>
<%                                                                    %># Main task of the TASTE function
<%                                                                    %>task_context '${iv.function_task(function)}' do
##
## CYCLIC & SPORADIC PIs = INPUT PORTS
##
## Sporadic functions have zero or one parameters; if zero, we must add 
## a dummy one (Orocos input ports must have 1 parameter)
##
 %  for pi in iv.list_sporadic_pi(function):
<%
        num_params = len(iv.list_in_params(function,pi))
        if 0 == num_params:
            param_t = 'int'
        elif 1 == num_params:
            param = iv.get_in_param_type(function, pi, iv.get_in_param_idx(function, pi, 0))
            param_t = iv.rock_type(param)
        else:
            raise ValueError(function + '.' + pi + ': sporadic PIs should have at most one parameter')
%>\
<%                                                                    %>    input_port '${iv.port_name(function, pi)}', '${param_t}'
 %  endfor
 %  for pi in iv.list_cyclic_pi(function):
<%
        if 0 != len(iv.list_in_params(function,pi)):
            raise ValueError(function + '.' + pi + ': cyclic PIs should have zero parameters')
%>\
<%                                                                    %>    input_port '${iv.trigger_port(function, pi)}', 'int'
 %  endfor
##
## SPORADIC RIs = OUTPUT PORTS
##
## Sporadic functions have zero or one parameters; if zero, we must add 
## a dummy one (Orocos input ports must have 1 parameter)
##
 %  for ri in iv.list_sporadic_ri(function):
<%
        num_params = len(iv.list_in_params(function, ri))
        if 0 == num_params:
            param_t = 'int'
        elif 1 == num_params:
            param = iv.get_in_param_type(function, ri, iv.get_in_param_idx(function, ri, 0))
            param_t = iv.rock_type(param)
        else:
            raise ValueError(function + '.' + ri + ': sporadic RIs should have at most one parameter')
%>\
<%                                                                    %>    output_port '${iv.port_name(function, ri)}', '${param_t}'
 %  endfor
##
## SYNCHRONOUS (PROTECTED/UNPROTECTED) PIs = OPERATIONS
## Protected --> run by callee's thread (default)
## Unprotected --> run by caller's thread
##
 %  for pi in iv.list_sync_pi(function):
<%                                                                    %>    operation('${pi}')
 %      if iv.has_out_params(function,pi):
<%
        num_params = len(iv.list_out_params(function, pi))
        if 1 == num_params:
            param = iv.get_out_param_type(function, pi, iv.get_out_param_idx(function, pi, 0))
            param_t = iv.rock_type(param)
        else:
            raise ValueError(function + '.' + ri + ': synchronous RIs should have at most one output parameter')
%>\
<%                                                                    %>        .returns('${param_t}')
 %      endif
 %      if iv.has_in_params(function,pi):
<%
        num_params = len(iv.list_in_params(function, pi))
        if 0 == num_params:
            param_t = 'int'
        elif 1 == num_params:
            param = iv.get_in_param_type(function, pi, iv.get_in_param_idx(function, pi, 0))
            param_t = iv.rock_type(param)
        else:
            raise ValueError(function + '.' + pi + ': synchronous PIs should have at most one input parameter')
%>\
<%                                                                    %>        .argument('arg', '${param_t}')
 %      endif
 %      if iv.is_unprotected(function, pi):
<%                                                                    %>        .runs_in_caller_thread
 %      endif
 %  endfor
##
## Functions are port-driven tasks, if they have ports
##
 %  if iv.has_async_pi(function):
<%                                                                    %>    port_driven
 %  endif
<%                                                                    %>end
<%                                                                    %>
##
## Cyclic PIs require a trigger task
##
 %  if iv.has_cyclic_pi(function):
 %      for pi in iv.has_cyclic_pi(function):
<%                                                                    %># Trigger tasks for cyclic interfaces
<%                                                                    %>task_context '${iv.trigger_task(function, pi)}' do
<%                                                                    %>    output_port '${iv.trigger_port(function, pi)}', 'int'
<%                                                                    %>    periodic ${iv.get_iface_period_seconds(function, pi)}
<%                                                                    %>end
 %      endfor
 %  endif



## =====================================================================
## H2020 ESROCOS Project
## Company: GMV Aerospace & Defence S.A.U.
## Licence: GPLv2
## ..................................................................
## Template for a Rock start script for a system generated from TASTE.
## Inputs:
## - iv: the IvData object
## =====================================================================
<%                                                                %><%%># Generated from ${context._with_template.uri}
<%                                                                %><%%>
<%                                                                %><%%>require 'orocos'
<%                                                                %><%%>require 'readline'
<%                                                                %><%%>
<%                                                                %><%%>include Orocos
<%                                                                %><%%>Orocos.initialize
<%                                                                %><%%>
<%                                                                %><%%>
<%                                                                %><%%>Orocos.run  ${'\\'}
 %  for f in iv.list_functions():
 %      for ci in iv.list_cyclic_pi(f):
<%                                                                %><%%>           '${iv.function_namespace(f)}::${iv.trigger_task(f, ci)}' => '${iv.trigger_task(f, ci)}',
 %      endfor
<%                                                                %><%%>           '${iv.function_namespace(f)}::${iv.function_task(f)}' => '${iv.function_task(f)}' ${'do' if loop.last else ','}
 %  endfor
<%                                                                %><%%>
<%                                                                %><%%>  # Find component services  
 %  for f in iv.list_functions():
<%                                                                %><%%>  ${iv.function_task(f)} = Orocos.name_service.get '${iv.function_task(f)}'
 %      for ci in iv.list_cyclic_pi(f):
<%                                                                %><%%>  ${iv.trigger_task(f, ci)} = Orocos.name_service.get '${iv.trigger_task(f, ci)}'
 %      endfor
 %  endfor
<%                                                                %><%%>
<%                                                                %><%%>  # Connect components
 %  for f in iv.list_functions():
 %      for ri in iv.list_sporadic_ri(f):
 %          if rf != '' and rpi != '':
<%                                                                %><%%>  ${iv.function_task(f)}.${iv.port_name(f, ri)}.connect_to ${'\\'}
<%                                                                %><%%>      ${iv.function_task(iv.get_remote_function(f, ri))}.${iv.port_name(f, iv.get_remote_pi(f, ri))}
 %          endif
 %      endfor
 %      for ci in iv.list_cyclic_pi(f):
<%                                                                %><%%>  ${iv.trigger_task(f, ci)}.${iv.trigger_port(f, ci)}.connect_to ${'\\'}
<%                                                                %><%%>      ${iv.function_task(f)}.${iv.trigger_port(f, ci)}
 %      endfor
 %  endfor
<%                                                                %><%%> 
<%                                                                %><%%>
<%                                                                %><%%>  # Configure and start components
 %  for f in iv.list_functions():
<%                                                                %><%%>  ${iv.function_task(f)}.configure
<%                                                                %><%%>  ${iv.function_task(f)}.start
<%                                                                %><%%>
 %      for ci in iv.list_cyclic_pi(f):
<%                                                                %><%%>  ${iv.trigger_task(f, ci)}.configure
<%                                                                %><%%>  ${iv.trigger_task(f, ci)}.start
<%                                                                %><%%>
 %      endfor
 %  endfor
<%                                                                %><%%>  Readline::readline("Press ENTER to exit\n")
<%                                                                %><%%>
<%                                                                %><%%>end

#import pip
#
#def install(package):
#    pip.main(['install', package])
#
## Example
#if __name__ == '__main__':
#    install('websocket-client')

#def install(package):
#    pip.main(['install', package])
#
## Example
#if __name__ == '__main__':
#    install('websocket')

#def install(package):
#    pip.main(['install', package])
#
## Example
#if __name__ == '__main__':
#    install('PyJWT')


from pyqlikengine.engine_communicator import EngineCommunicator
from pyqlikengine.engine_global_api import EngineGlobalApi
from pyqlikengine.engine_app_api import EngineAppApi
from pyqlikengine.engine_communicator import SecureEngineCommunicator

host = "cloudera.qlik.com"
proxyPrefix = "jupyter"
userDirectory = "CLOUDERA"
userId = "chris"
privateKey = "./private.key"
conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
conn.ws.recv()

import pyqlikengine.engine_communicator
import pyqlikengine.engine_global_api
import pyqlikengine.engine_app_api
import pyqlikengine.engine_generic_object_api
import pyqlikengine.engine_field_api
import pyqlikengine.structs
conn = SecureEngineCommunicator(host, proxyPrefix, userDirectory, userId, privateKey)
efa = pyqlikengine.engine_field_api.EngineFieldApi(conn)
Structs = pyqlikengine.structs.Structs()
egoa = pyqlikengine.engine_generic_object_api.EngineGenericObjectApi(conn)
ega = EngineGlobalApi(conn)
eaa = EngineAppApi(conn)
conn.ws.recv()

apps = ega.get_doc_list()

for app in apps:
    print app['qTitle']
    
opened_app = ega.open_doc('8921dfe7-f46c-437c-bdb3-eb16c768793f')
app_handle = ega.get_handle(opened_app)

hc_inline_dim = Structs.nx_inline_dimension_def(["Customer"])
hc_mes_sort = Structs.nx_sort_by()
hc_inline_mes = Structs.nx_inline_measure_def("=Sum([Sales Amount])")
hc_dim = Structs.nx_hypercube_dimensions(hc_inline_dim)
hc_mes = Structs.nx_hypercube_measure(hc_mes_sort, hc_inline_mes)
nx_page = Structs.nx_page(0, 0, 100, 2)
hc_def = Structs.hypercube_def("$", [hc_dim],[hc_mes], [nx_page])
hc_response = eaa.create_object(app_handle, "CH01", "Chart", "qHyperCubeDef", hc_def)
hc_handle = ega.get_handle(hc_response)
egoa.get_layout(hc_handle)
lb_field = eaa.get_field(app_handle, "Customer")
fld_handle = ega.get_handle(lb_field)
values_to_select = [{'qText': 'Fins'}, {'qText': 'Bizmarts'}, {'qText': 'Benedict'}, {'qText': 'Earth'}, {'qText': 'Gate'}]
sel_res = efa.select_values(fld_handle,values_to_select)
hc_data = egoa.get_hypercube_data(hc_handle, "/qHyperCubeDef", [nx_page])
elems = hc_data["qDataPages"][0]['qMatrix']
dim_list = []
mes_list = []
for elem in range(len(elems)):
    dim_list.append(elems[elem][0]["qText"])
    mes_list.append(elems[elem][1]["qNum"])

conn.close_qvengine_connection(conn)
print(dim_list)
print(mes_list
      
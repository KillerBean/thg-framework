from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary:

  def __init__(self):
    self.multi_target = False
    self.target_type = None
    self.targets = []
    self.options = BaseOptions()
    self.results = BaseResult()
    name = None #nome do auxiliar
    description = None #descricao do auxiliar
    author = [] # nome do autor
    references = []#referenia do exploit
    disclosure_date = None #data de divulgacao
    service_name = None #nome do servico
    service_version = None #versao do servico
    dbinfo = ['name', 'description', 'author', 'references', 'disclosure_date', 'service_name', 'service_version']#info database
    multi_target = False#vvarios alvos
    targets = []#alvo
    target_type = None#tipo de alvo
    options = None #opcoes
    results = None #resultados

  def get_info(self):
    info = {}
    for field_name in self.dbinfo:
      info[field_name] = getattr(self, field_name)
    return info





  def register_crawler(self, timeout_value=5, threads_value=1):
    self.target_type = "http"
    BaseOption(name="RHOST", required=True, description="ip to test"),

    self.register_options([
        #Opt::RPORT(Rex::Proto::MQTT::DEFAULT_PORT)
        BaseOption(name='CLIENT_ID', [false, 'The client ID to send if necessary for bypassing clientid_prefixes']),
        BaseOption(name='READ_TIMEOUT', [true, 'Seconds to wait while reading MQTT responses', 5])
        #register_autofilter_ports([Rex::Proto::MQTT::DEFAULT_PORT, Rex::Proto::MQTT::DEFAULT_SSL_PORT])
    ])



  def thg_update_info(self, info):
    for name in info:
      if name in self.dbinfo:
        setattr(self, name, info[name])


  def register_options(self, option_array):
    for option in option_array:
      self.options.add_option(option)


  def get_missing_options(self):
    def is_missing(option):
      return option.required and option.value in [None, '']

    missing_options = filter(is_missing, self.options.get_options())
    return list(missing_options)




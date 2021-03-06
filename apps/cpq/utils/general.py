from django.urls import reverse

from htk.utils import htk_setting
from htk.utils import resolve_model_dynamically
from htk.utils.enums import get_enum_symbolic_name

def get_admin_urls():
    from htk.apps.cpq.constants.general import CPQ_APP_MODEL_NAMES
    admin_urls = []
    app_label = htk_setting('HTK_DEFAULT_APP_LABEL')
    for app_model_name in CPQ_APP_MODEL_NAMES:
        app_model = resolve_model_dynamically('%s.%s' % (app_label, app_model_name,))
        admin_url = {
            'url' : reverse('admin:%s_%s_changelist' % (app_label, app_model_name,)),
            'add_url' : reverse('admin:%s_%s_add' % (app_label, app_model_name,)),
            'name' : app_model._meta.verbose_name_plural.title(),
        }
        admin_urls.append(admin_url)
    return admin_urls

def get_reporting_urls():
    from htk.apps.cpq.constants.general import CPQ_REPORTING_URL_NAMES
    reporting_urls = []
    for reporting_url_name in CPQ_REPORTING_URL_NAMES:
        reporting_url = {
            'url' : reverse('cpq_%s' % reporting_url_name),
            'name' : ' '.join(reporting_url_name.split('_')).title(),
        }
        reporting_urls.append(reporting_url)
    return reporting_urls

def get_tools_urls():
    from htk.apps.cpq.constants.general import CPQ_TOOLS_URL_NAMES
    tools_urls = []
    for tools_url_name in CPQ_TOOLS_URL_NAMES:
        tools_url = {
            'url' : reverse('cpq_%s' % tools_url_name),
            'name' : ' '.join(tools_url_name.split('_')).title(),
        }
        tools_urls.append(tools_url)
    return tools_urls

def get_invoice_payment_terms_choices():
    from htk.apps.cpq.enums import InvoicePaymentTerm
    choices = [(payment_term.value, get_enum_symbolic_name(payment_term),) for payment_term in InvoicePaymentTerm]
    return choices

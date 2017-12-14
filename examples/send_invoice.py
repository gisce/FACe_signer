import zeep
from FACe import FACe_signer

import base64

OUR_CERT = "certs/our_cert.pem"

FACE_ENVS = {
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl"
}

client = zeep.Client(
    FACE_ENVS['prod'],
    plugins=[FACe_signer()]
)

INVOICE_FILE = 'factura-prueba-v1-2-0.xsig'

# The expected arguments by enviarFactura FACe's resource
the_invoice = {
    "correo": "devel@gisce.net",
    "factura": {
        "factura": base64.b64encode(open(INVOICE).read()),
        "nombre": "factura-prueba-v1-2-0.xsig",
        "mime": "application/xml",
    }
}

client.service.enviarFactura(the_invoice)

# -*- coding: utf-8 -*-
import zeep
from FACe_signer import FACe_signer

import os
import base64

OUR_CERT = "certs/our_cert.pem"

FACE_ENVS = {
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl"
}

client = zeep.Client(
    FACE_ENVS['staging'],
    plugins=[FACe_signer(OUR_CERT)]
)

INVOICE_FILENAME = './factura-prueba-v1-2-0.xsig'
INVOICE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    INVOICE_FILENAME)



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

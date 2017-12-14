# -*- coding: utf-8 -*-
from FACe_signer import FACe_signer
import zeep

OUR_CERT = "certs/our_cert.pem"

FACE_ENVS = {
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl"
}

client = zeep.Client(
    FACE_ENVS['staging'],
    plugins=[FACe_signer(OUR_CERT, debug=True)]
)

client.service.consultarNIFs()

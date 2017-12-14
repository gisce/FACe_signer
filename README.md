# FACe signer

It provides a Zeep plugin desired to patch SOAP envelopes providing a pseudo-X509 WS-Security integration (expected by FACe servers) signing just the soap header.

## Usage

```
from FACe_signer import FACe_signer

import zeep

FACE_ENVS = {
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl"
}
OUR_CERT = "certs/our_cert.pem"

client = zeep.Client(
    FACE_ENVS['prod'],
    plugins=[FACe_signer(OUR_CERT)]
)

# Use the expected service as usual with zeep
client.service.XXX()

```

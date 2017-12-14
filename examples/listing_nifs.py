from FACe import FACe_signer
import zeep

OUR_CERT = "certs/our_cert.pem"

FACE_ENVS = {
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl"
}

client = zeep.Client(
    FACE_ENVS['prod'],
    plugins=[FACe_signer()]
)

client.service.consultarNIFs()
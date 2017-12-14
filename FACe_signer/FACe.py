# -*- coding: utf-8 -*-
from zeep import Plugin
from lxml import etree
import soap_wsse
import logging

class FACe_signer(Plugin):
    """
    FACe signer plugin for ZEEP

    It patchs a SOAP envelope to ensure that is FACe compatible (~pseudo OASIS WS-Security 1.0 X509)

    Using default X509 Zeep's signature do not work with FACe servers... Enjoy this is aj-pain...
    """
    def __init__(self, certificate, debug=False):
        """
        Initialize a FACe Signer with the required certificate (PEM)
        """
        assert type(certificate) == str
        assert type(debug) == bool

        self.certificate = certificate
        self.debug = debug

    def log_it(self, what):
        """
        Axiliar method to log and debug it
        """
        logging.debug(what)
        if self.debug:
            print (what)

    def sign_request(self, XML):
        """
        Auxiliar method to sign a request as FACe's expect
        """
        signed_xml = soap_wsse.sign_envelope(XML, self.certificate)
        # Verify signed envelope
        assert soap_wsse.verify_envelope(signed_xml, self.certificate)
        return signed_xml

    def ingress(self, envelope, http_headers, operation):
        """
        Injected method after receive response from FACe server
        """
        # Log it
        self.log_it("Receiving response:")
        self.log_it(etree.tostring(envelope, pretty_print=True))
        return envelope, http_headers

    def egress(self, envelope, http_headers, operation, binding_options):
        """
        Method to patch the content of the envelope sended to FACe server
        """
        # Add a dummy soap:header
        SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
        head = etree.SubElement(envelope, etree.QName(SOAP_NS, 'Header'))
        envelope.append( head )

        # Sign the string using the soap_wsse simple signer
        signed_envelope_string = (self.sign_request( etree.tostring(envelope)))

        # Recreate the envelope conve   rting the signed string to an etree
        envelope = etree.fromstring(signed_envelope_string)

        # Log it
        self.log_it("Receiving response:")
        self.log_it(etree.tostring(envelope, pretty_print=True))

        return envelope, http_headers

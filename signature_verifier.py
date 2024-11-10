from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from utils import recover_address_from_signature

class SignatureVerifier:
    def __init__(self):
        pass

    def verify_signature(self, scheme_type, address, signature, signed_hash):
        if scheme_type == "ecdsa":
            return self.verify_ecdsa(address, signature, signed_hash)
        elif scheme_type == "schnorr":
            return self.verify_schnorr(address, signature, signed_hash)
        else:
            raise ValueError(f"Unsupported scheme type: {scheme_type}")

    def verify_ecdsa(self, address, signature, signed_hash):
        try:
            recovered_address = recover_address_from_signature(signature, signed_hash, "ecdsa")
            if recovered_address != address:
                return False
            return True
        except InvalidSignature:
            return False

    def verify_schnorr(self, address, signature, signed_hash):
        pass

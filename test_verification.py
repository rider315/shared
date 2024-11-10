# test_verification.py

import unittest
from signature_verifier import SignatureVerifier
from eth_account import Account
from eth_account.messages import encode_defunct

class TestSignatureVerification(unittest.TestCase):
    def setUp(self):
        self.verifier = SignatureVerifier()
        self.account = Account.create()  
        self.private_key = self.account.key
        self.expected_address = self.account.address
        self.message = b"This is a test message."

        
        encoded_message = encode_defunct(text=self.message.decode("utf-8"))
        self.signed_data = Account.sign_message(encoded_message, private_key=self.private_key)
        self.signature = self.signed_data.signature  
        self.message_hash = self.signed_data.message_hash

    def test_ecdsa_valid(self):
      
        is_valid = self.verifier.verify_signature("ecdsa", self.expected_address, self.signature, self.message_hash)
        self.assertTrue(is_valid)

    def test_ecdsa_invalid(self):
        
        invalid_signature = self.signature[:-1] + b"\x00"
        is_valid = self.verifier.verify_signature("ecdsa", self.expected_address, invalid_signature, self.message_hash)
        self.assertFalse(is_valid)

if __name__ == "__main__":
    unittest.main()

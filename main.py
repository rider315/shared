from signature_verifier import SignatureVerifier
from eth_account import Account
from eth_account.messages import encode_defunct

def main():
    verifier = SignatureVerifier()
    scheme_type = "ecdsa"
    account = Account.create()
    private_key = account.key
    expected_address = account.address
    message = b"This is a test message."
    encoded_message = encode_defunct(text=message.decode("utf-8"))
    signed_data = Account.sign_message(encoded_message, private_key=private_key)
    signature = signed_data.signature
    if len(signature) != 65:
        print(f"Unexpected signature length: {len(signature)} bytes. Expected 65 bytes.")
        return
    message_hash = signed_data.message_hash
    is_valid = verifier.verify_signature(scheme_type, expected_address, signature, message_hash)
    print(f"Signature valid: {is_valid}")

if __name__ == "__main__":
    main()

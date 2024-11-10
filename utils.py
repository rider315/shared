from eth_keys import keys
from eth_keys.exceptions import BadSignature

def recover_address_from_signature(signature, signed_hash, scheme_type):
    if scheme_type != "ecdsa":
        raise ValueError(f"Unsupported scheme type: {scheme_type}")

    try:
        if len(signature) != 65:
            raise ValueError("Invalid signature length for ECDSA. Expected 65 bytes.")

        r = int.from_bytes(signature[0:32], byteorder="big")
        s = int.from_bytes(signature[32:64], byteorder="big")
        v = signature[64]

        if v >= 27:
            v -= 27

        eth_signature = keys.Signature(vrs=(v, r, s))
        public_key = eth_signature.recover_public_key_from_msg_hash(signed_hash)
        address = public_key.to_checksum_address()
        return address
    except (BadSignature, ValueError) as e:
        print(f"Address recovery failed: {e}")
        return None

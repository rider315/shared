# charter-21BEC2315



```markdown
# Modular Signature Verification

A modular signature verification system designed to verify ECDSA signatures in an Ethereum-compatible format. This project includes a backend service for signature verification, unit tests for validation, and a modular structure that allows for future expansion to support other signature schemes (such as Schnorr or RSA).

## Features

- **Ethereum-Compatible ECDSA Verification**: Verifies signatures using Ethereum’s `(r, s, v)` format.
- **Address Recovery**: Recovers the signing address from the signature and compares it to the expected address.
- **Modular and Extensible Design**: Easily extendable to support additional signature schemes.
- **Comprehensive Unit Tests**: Tests are provided to validate the system’s functionality for both valid and invalid cases.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
    - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
4. [Usage Instructions](#usage-instructions)
5. [Example Output](#example-output)
6. [Extending the Project](#extending-the-project)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Contact](#contact)

---

## Project Structure

The project directory is structured as follows:

```plaintext
modular_signature_verification/
├── main.py                     # Main script to run the signature verification example
├── signature_verifier.py        # Core logic for signature scheme recognition and verification
├── utils.py                     # Utility functions for address recovery
├── test_verification.py         # Unit tests for signature verification
├── requirements.txt             # Required libraries
└── README.md                    # Project documentation
```

---

## Prerequisites

- **Python 3.7 or above**: Ensure that Python is installed. You can check your Python version by running `python --version`.
- **pip**: Python’s package installer. Verify that pip is installed by running `pip --version`.

### Libraries Used

The following libraries are required to run this project:
- `cryptography`: Provides cryptographic functions such as hashing.
- `eth-keys`: Used for handling Ethereum keys and signatures.
- `web3` (includes `eth-account`): Allows Ethereum-compatible account and signature operations.

These libraries will be installed through the `requirements.txt` file as part of the setup process.

---

## Setup Instructions

To get started with this project, follow these setup instructions:

### Setting Up a Virtual Environment

It’s recommended to use a virtual environment to isolate dependencies for this project. Here’s how:

1. **Navigate to the Project Directory**:
   ```bash
   cd modular_signature_verification
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   After activation, your terminal prompt should display `(venv)`, indicating that the virtual environment is active.

4. **Install Required Dependencies**:

   With the virtual environment activated, install the required libraries using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install `cryptography`, `eth-keys`, and `web3`.

---

## Usage Instructions

Once you’ve completed the setup, you can start using the project.

### Running the Main Script

The main script demonstrates signature creation, verification, and address recovery. Run it with:

```bash
python main.py
```

### Running Unit Tests

Unit tests are provided in `test_verification.py` to validate the functionality of the signature verification system. To run all tests:

```bash
python -m unittest test_verification.py
```

If the tests pass, you’ll see output like this:

```plaintext
..
----------------------------------------------------------------------
Ran 2 tests in 0.019s

OK
```

---

## Example Output

When you run `main.py`, the script will generate an Ethereum-compatible ECDSA signature for a test message, recover the signing address, and verify if it matches the expected address.

Expected output from running `main.py`:

```plaintext
Signature valid: True
```

This confirms that the signature was verified successfully.

---

## How the Code Works

1. **Signature Generation**:
   - `main.py` generates a new Ethereum-compatible ECDSA signature for a sample message.
   - It creates a 65-byte `(r, s, v)` format signature.

2. **Address Recovery**:
   - Using the `SignatureVerifier` class, the code recovers the signing address from the signature.

3. **Signature Verification**:
   - The recovered address is compared with the expected address. If they match, the signature is considered valid.

4. **Test Cases**:
   - Positive test case: Verifies a correct signature.
   - Negative test case: Modifies the signature to test for invalid verification.

---

## Extending the Project

This project is modular and can be extended to support additional signature schemes.

1. **Adding a New Verification Method**:
   - Create a new method (e.g., `verify_schnorr`) in `signature_verifier.py` for the desired signature scheme.

2. **Updating the `verify_signature` Method**:
   - Modify the `verify_signature` method in `SignatureVerifier` to call the new verification method based on the specified `schemeType`.

3. **Adding Test Cases**:
   - Add corresponding test cases in `test_verification.py` to ensure the new signature scheme functions correctly.

The modular design allows for easy integration of different schemes, and each scheme’s verification logic can be independently tested.

---

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request. Ensure that your changes pass the existing tests and adhere to the project’s code style.

---



## Acknowledgments

- **Ethereum Foundation**: For resources on ECDSA and cryptographic standards.
- **The Graph Protocol**: For modular and decentralized development inspiration.
- **OpenZeppelin**: For utilities and libraries related to Ethereum.

---

## Contact

For questions, suggestions, or feedback, please reach out to [gaurav.chaudhary.865022@gmail.com].

---

```

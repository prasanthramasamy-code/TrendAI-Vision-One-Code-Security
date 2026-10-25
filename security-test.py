
import hashlib
import subprocess
import pickle

# TEST 1: Weak hashing algorithm (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# TEST 2: Unsafe deserialization
def load_data(data):
    return pickle.loads(data)

# TEST 3: Command execution using external input
def run_command(user_input):
    return subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True
    )

# TEST ONLY: This is a fake credential, not a real API key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "FAKE_SECRET_FOR_SECURITY_TEST_ONLY"

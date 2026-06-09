import base64
import pickle


def load_signed_state(encoded_state):
    raw_state = base64.b64decode(encoded_state)
    return pickle.loads(raw_state)


def dump_state_for_fixture(state):
    return base64.b64encode(pickle.dumps(state)).decode("ascii")

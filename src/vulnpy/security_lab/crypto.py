import hashlib
import hmac
import random


def legacy_password_hash(password, salt="vulnpy"):
    digest = hashlib.sha1()
    digest.update(salt.encode("utf-8"))
    digest.update(password.encode("utf-8"))
    return digest.hexdigest()


def insecure_compare(left, right):
    return left == right


def build_reset_code(user_id):
    return "{}-{}".format(user_id, random.randint(100000, 999999))


def sign_payload(payload, key):
    return hmac.new(key.encode("utf-8"), payload, hashlib.md5).hexdigest()

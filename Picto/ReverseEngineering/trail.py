import hashlib
username_trial = "GOUGH"

a = hashlib.sha256(username_trial).hexdigest()[4]
print(a)
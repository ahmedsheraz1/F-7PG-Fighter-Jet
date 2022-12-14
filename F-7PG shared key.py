Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'F-7PG shared key')
m.hexdigest()
'c089bb75f953db78786bcc6bdcb3ba6f05e391a516d048e0f7ff0e994e4ca35d'

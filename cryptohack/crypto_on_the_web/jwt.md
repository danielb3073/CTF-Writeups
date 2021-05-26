# Crypto on the Web

```
pip install pyjwt
```

## Decrypting JWT with pyjwt

> Encrypted Token - eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ

```
python3
import jwt

enc = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

jwt.get_unverified_header(enc) -> {'typ': 'JWT', 'alg': 'HS256'}

jwt.decode(enc, options={"verify_signature": False})
```
> Decoding without secret key, key is only used to verify signature but can be decoded without using verify_signature : false

# No Way JOSE

> Create a session with username (zub), get session token.

```
{"session":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjpmYWxzZX0.SXfTBGJFoajk1uUq3P0g6WPZ-MSVJuul_TRj36QhrHU"}

enc = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjpmYWxzZX0.SXfTBGJFoajk1uUq3P0g6WPZ-MSVJuul_TRj36QhrHU"

jwt.decode(enc, options={"verify_signature": False})
```

> {'username': 'zub', 'admin': False}

```
jwt.encode({'username': 'zub', 'admin': True}, key="", algorithm='none')
```

> eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjp0cnVlfQ.

# JWT Secrets

```
{"session":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjpmYWxzZX0.NbLXDvikSw-L_PcHcI-bF-Uz7K1o7bjC54z6lsGiUag"}

enc = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjpmYWxzZX0.NbLXDvikSw-L_PcHcI-bF-Uz7K1o7bjC54z6lsGiUag"

jwt.decode(enc, options={"verify_signature": False})
```

> Potentially readme key means key="secret" as per JWT doc examples ?

```
jwt.encode({'username': 'zub', 'admin': True}, key="secret", algorithm='HS256')
```

> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inp1YiIsImFkbWluIjp0cnVlfQ.J_HWwxoezm4-YkstSny6UxRLE95jJJ0zuGsTgDP0wMk
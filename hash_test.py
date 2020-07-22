from passlib.hash import pbkdf2_sha256

password = '1234'

hash_pw = pbkdf2_sha256.hash(password)
print(hash_pw)
print(pbkdf2_sha256.verify(password, hash_pw))

# print(hash_pw == '$pbkdf2-sha256$29000$gVAqhbB2rpXS2lvrfe/9Hw$9QsR1nMoLAuNU2xRHUsJi3s5h7A/84FkSwNgDeZwS6k')

import base64
k1 ='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k2_and_k1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e' 
k2_and_k3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
f_and_k1_and_k3_and_k2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
k2 = bytes([a^b for a,b in zip(bytes.fromhex(k2_and_k1),bytes.fromhex(k1))]) #Concatenate each other => chuyển về tất cả thành bytes
print(k2)
k3 = bytes([b^a for b,a in zip(k2,bytes.fromhex(k2_and_k3))])
f = bytes([d^(c^(b^a)) for d,c,b,a in zip(bytes.fromhex(f_and_k1_and_k3_and_k2),k2,k3,bytes.fromhex(k1))])
print(f)


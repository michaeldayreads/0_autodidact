# non generalized version. Star Wars The Force Awakens tonight :P
data = 'X-DSPAM-Confidence: 0.8475'
atpos = data.find(':')
confidence = float(data[atpos+1:].strip())
print confidence
print type(confidence)

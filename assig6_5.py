text = "X-DSPAM-Confidence:    0.8475";

space = text.find(" ")

substring = text[space:]
substring = substring.strip()
substring = float(substring)

print(substring)

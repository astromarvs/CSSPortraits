# Generate a file with "LE SSERAFIM" repeated 1000 times

times = 2000
text = "LE SSERAFIM " * times  # note the trailing space

with open(f"LE_SSERAFIM_{times}.txt", "w", encoding="utf-8") as f:
    f.write(text.strip())  # remove the last trailing space

print(f"File 'LE_SSERAFIM_{times}.txt' created successfully!")

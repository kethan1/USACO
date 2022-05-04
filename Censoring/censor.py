with open("censor.in") as input_file:
    magazine = input_file.readline().strip()
    censored_text = input_file.readline().strip()

# while censored_text in magazine:
#     magazine = magazine.replace(censored_text, "")

output = ""
for letter in magazine:
    output += letter
    if (
        len(output) >= len(censored_text)
        and output[len(output) - len(censored_text):] == censored_text
    ):
        output = output[: len(output) - len(censored_text)]

with open("censor.out", "w") as output_file:
    print(output, file=output_file)

weather = input("Яка погода? (тепло, хмарно, холодно, дощ ):")

if weather == "тепло":
    print("літній або весняний вільний одяг")
elif weather == "хмарно":
    print("весняний одяг, бажано вітровку")
elif weather == "холодно":
    print("зимовий одяг")
elif weather == "дощ":
    print("спати")
else:
    print("повторіть спробу")
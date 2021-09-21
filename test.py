def main():
    step1 = "Вы находитесь в пещере"
    print(step1)
    command = "выйти наружу"
    if command.find("наружу"):
        exit_ = True
    print(f"Вы покидаете пещеру: {exit_}")

main()
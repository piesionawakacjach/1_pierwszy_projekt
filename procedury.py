
def clear_screen():
    print("\n" * 100)

def daj_prompt_z_zakresu_liczb(prompt, wart_min, wart_max):
    moj_prompt = prompt+f"({wart_min}-{wart_max}): "

    while True:
        try:
            wart = int(input(moj_prompt))
            if wart_min <= wart <= wart_max:
                return wart
        except ValueError:
            pass


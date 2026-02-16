led1, led2, led3 = map(int, input("Enter LED status (1/0) for 3 LEDs: ").split(','))

leds_on = [f"LED{i+1} ON" for i, val in enumerate([led1, led2, led3]) if val]
print(", ".join(leds_on) if leds_on else "All LEDs off")

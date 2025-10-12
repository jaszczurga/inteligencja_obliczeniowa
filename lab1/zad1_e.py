import math
from datetime import datetime, date

def calculate_biorhythms(days_lived):
    """Calculate physical, emotional, and intellectual biorhythms"""
    physical = math.sin(2 * math.pi * days_lived / 23)
    emotional = math.sin(2 * math.pi * days_lived / 28)
    intellectual = math.sin(2 * math.pi * days_lived / 33)
    return physical, emotional, intellectual

def get_user_info():
    """Get user information: name and birth date"""
    name = input("Podaj swoje imię: ")
    
    while True:
        try:
            birth_year = int(input("Podaj rok urodzenia (np. 1995): "))
            birth_month = int(input("Podaj miesiąc urodzenia (1-12): "))
            birth_day = int(input("Podaj dzień urodzenia (1-31): "))
            
            # Validate date
            birth_date = date(birth_year, birth_month, birth_day)
            break
        except ValueError:
            print("Nieprawidłowa data. Spróbuj ponownie.")
    
    return name, birth_date

def main():
    # Get user information
    name, birth_date = get_user_info()
    
    # Calculate days lived
    today = date.today()
    days_lived = (today - birth_date).days
    
    # Welcome user and show days lived
    print(f"\nWitaj, {name}!")
    print(f"Dzisiaj jest {days_lived} dzień twojego życia.")
    
    # Calculate biorhythms for today
    physical, emotional, intellectual = calculate_biorhythms(days_lived)
    
    # Display biorhythm values
    print(f"\nTwoje biorytmy na dzisiaj:")
    print(f"Fizyczny: {physical:.3f}")
    print(f"Emocjonalny: {emotional:.3f}")
    print(f"Intelektualny: {intellectual:.3f}")
    
    # Part b) - Check if biorhythms are high or low and provide feedback
    print("\nAnaliza biorytmów:")
    
    # Check each biorhythm
    biorhythms = {
        "Fizyczny": physical,
        "Emocjonalny": emotional,
        "Intelektualny": intellectual
    }
    
    for rhythm_name, value in biorhythms.items():
        if value > 0.5:
            print(f"{rhythm_name}: Gratulacje! Masz świetny dzień pod względem {rhythm_name.lower()}!")
        elif value < -0.5:
            print(f"{rhythm_name}: Nie martw się, masz trudny dzień pod względem {rhythm_name.lower()}.")
            
            # Check if tomorrow will be better
            tomorrow_value = 0
            if rhythm_name == "Fizyczny":
                tomorrow_value = math.sin(2 * math.pi * (days_lived + 1) / 23)
            elif rhythm_name == "Emocjonalny":
                tomorrow_value = math.sin(2 * math.pi * (days_lived + 1) / 28)
            elif rhythm_name == "Intelektualny":
                tomorrow_value = math.sin(2 * math.pi * (days_lived + 1) / 33)
            
            if tomorrow_value > value:
                print(f"  Dobra wiadomość: Jutro będzie lepiej! ({tomorrow_value:.3f})")
            else:
                print(f"  Jutro może być trudniejsze ({tomorrow_value:.3f}), ale to się zmieni!")
        else:
            print(f"{rhythm_name}: Neutralny poziom - stabilny dzień.")

if __name__ == "__main__":
    main()

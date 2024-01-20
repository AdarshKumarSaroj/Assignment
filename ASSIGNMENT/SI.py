class SIUnitConverter:
    def __init__(self):
        self.units = {
            'Meter': 1,
            'Centimeter': 0.01,
            'Kilometer': 1000,
            'Gram': 1,
            'Kilogram': 1000,
            'Milligram': 0.001,
        }

    def Recogniser(self):
        pass
        Meter = ["M","Meter"]
        Centimeter= ["Cm","Centimeter"]             #trying to get other values types by a user and cheking them
        Kilometer = ["Km","Kilometer"]
        Gram = ["G","Gram"]
        Kilogram = ["Kg","Kilogram"] 
        Milligram = ["Mg","Milligram"]

        mm = [Meter,Centimeter,Kilogram,Gram,Kilogram,Kilometer,Milligram]

        try:
            value = float(input("Enter the value to convert : "))

            print("\nSelect the source unit:")

            changing = self.get_unit_input()

            for a in mm:
                if changing in a:
                    changing_unit = a[-1]
                
                else:
                    pass

            print("\nSelect the target unit:")
            target = self.get_unit_input()

            for a in mm:
                if target in a:
                    target_unit= a[-1]
                
                else:
                    pass

            return value , changing_unit , target_unit
        
        except:
            print("Invalid input. Please enter a numeric value.")
            return None, None, None


    def get_unit_input(self):
        print("Available units:")
        for unit in self.units:
            print(f"- {unit}")

        selected_unit = input("Enter the unit: ").capitalize()
        return selected_unit



    def convert(self, value, source_unit, target_unit):
        try:
            converted_value = value * (self.units[source_unit] / self.units[target_unit])
            print(f"\nResult: {converted_value:.1f} {target_unit}")

        except:
            print("Invalid unit. Please select a valid unit.")




while True:
    user_input = SIUnitConverter().Recogniser()

    if user_input[0] is not None:
        SIUnitConverter().convert(*user_input)

    another_conversion = input("\nDo you want to perform another conversion? (yes/no): ").lower()

    if another_conversion != 'yes' or another_conversion != "y":
        break

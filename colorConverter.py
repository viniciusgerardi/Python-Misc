# Tool to convert color values, developed as study for object oriented programming


class Color:
    # Contructor receiving integer values
    def __init__(self, red: int, green: int, blue=0):
        # Validate arguments
        assert red >= 0 and red <= 255, f'Red value is invalid ({red} not in 0 ~ 255 range)'
        assert green >= 0 and green <= 255, f'Green value is invalid ({green} not in 0 ~ 255 range)'
        assert blue >= 0 and blue <= 255, f'Blue value is invalid ({blue} not in 0 ~ 255 range)'

        # Assign values
        self.red = red
        self.green = green
        self.blue = blue
        self.hexColor = self.convertHex(
            self.red)+self.convertHex(self.green)+self.convertHex(self.blue)

    # Method to describe color parameters
    def description(self):
        return(f'The color values are {self.red} red, {self.green} green and {self.blue} blue. '
               f'The Hexadecimal color is {self.hexColor}.')

    # Method to convert integer value to hexadecimal
    def convertHex(self, intColor):
        hexadecimalColor = hex(intColor).lstrip("0x")
        if len(hexadecimalColor) == 0:
            hexadecimalColor = "00"
        elif len(hexadecimalColor) == 1:
            hexadecimalColor = "0" + hexadecimalColor
        return hexadecimalColor

    # Method to validate hexadecimal value
    def validateHex(self, hexValue):
        error = False
        if len(hexValue) != 6:  # Validate lenght
            error = True
        else:
            # Validate values
            dicHex = ['0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
            for i in hexValue:
                if i.upper() not in dicHex:
                    error = True
        if error:
            return False
        else:
            return True

    # Method to convert hexadecimal value to integer (used on child class)
    def convertInt(self, hexColor):
        if self.validateHex(hexColor):
            self.red = int(hexColor[0:2], 16)
            self.green = int(hexColor[2:4], 16)
            self.blue = int(hexColor[4:6], 16)
        else:
            print(
                f'{hexColor} is invalid hexadecimal color, setting values to black')
            self.hexColor = '000000'
            self.red = 0
            self.green = 0
            self.blue = 0

    # Getters and Setters
    def setRed(self, red):
        self.red = red
        self.hexColor = self.convertHex(
            self.red)+self.convertHex(self.green)+self.convertHex(self.blue)

    def setGreen(self, green):
        self.green = green
        self.hexColor = self.convertHex(
            self.red)+self.convertHex(self.green)+self.convertHex(self.blue)

    def setBlue(self, blue):
        self.blue = blue
        self.hexColor = self.convertHex(
            self.red)+self.convertHex(self.green)+self.convertHex(self.blue)

    def setHex(self, hexColor):
        self.hexColor = hexColor
        self.convertInt(self.hexColor)

    def getRed(self):
        return self.red

    def getGreen(self):
        return self.green

    def getBlue(self):
        return self.blue

    def getHex(self):
        return self.hexColor


class ColorHex(Color):
    # Contructor receiving hexadecimal value
    def __init__(self, hexColor: str):
        self.hexColor = hexColor
        self.convertInt(hexColor)


# Main program
black = Color(0, 0, 0)
print(f'Black: {black.description()}')

white = ColorHex('ffffff')
print(f'White: {white.description()}')

grey = Color(0, 0, 0)
grey.setRed(128)
grey.setGreen(128)
grey.setBlue(128)
print(f'Grey: {grey.description()}')

yellow = Color(0, 0, 0)
yellow.setHex('ffff00')
print(f'Yellow: {yellow.description()}')

print('\nInvalid color 1:')
invalidColor1 = ColorHex('gfffff')
print(f'Invalid: {invalidColor1.description()}')

print('\nInvalid color 2:')
invalidColor2 = ColorHex('g')
print(f'Invalid: {invalidColor2.description()}')

# print('\nInvalid color 3:')
# invalidColor3 = Color(255, 256, -1)
# print(f'Invalid: {invalidColor3.description()}')

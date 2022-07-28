class Card:          
    """    A template for the cards in the game
        colors:
            1 = Red
            2 = Blue
            3 = Yellow
            4 = Green
        effects:
            0 - 9 = just the normal numbers
            10 = Invertion '<->'
            11 = Block 'X'
            12 = '+2'
            13 = Change color 'C.Color'
            14 = '+4'
        OBS: all cards with a 13(C.Color) or 14(+4) are automatically Black
    """    
    def __init__(self, number, color=None):       
        if color == 1:
            self.color = 'Red'
        elif color == 2:
            self.color = 'Blue'
        elif color == 3:
            self.color = 'Yellow'
        elif color == 4:
            self.color = 'Green'
        if number < 10:
            self.number = str(number)
        elif number == 10:
            self.number = '<->'
        elif number == 11:
            self.number = 'X'
        elif number == 12:
            self.number = '+2'
        elif number == 13:
            self.number = 'C.Color'
            self.color = 'Black'
        elif number == 14:
            self.number = '+4'
            self.color = 'Black'
    
    
    def __str__(self):
        return f'{"_":_^9}\n|{" ":^7}|\n|{self.number:^7}|\n|{self.color:^7}|\n|{" ":^7}|\n{"¨":¨^9}'
    
    
    def check(self, other_card):
        if self.number == other_card.number or self.color == other_card.color or self.color == 'Black' or other_card.color == 'Black':
            return True
        else:
            return False
    
    
    def effect(self):
        return self.number

    
    def get_color(self):
        return self.color


help(Card)
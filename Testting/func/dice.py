from func.sample import roll_dice

def get_result(num):
    result = roll_dice()
    if num == result:
        return "You win"
    else:
        return "You lose"
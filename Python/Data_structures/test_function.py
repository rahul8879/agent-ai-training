def check_age(age):
    if age > 18:
        return "Adult"
    else:
        return "Minor"
    

def cbse_result():
    return ('123', '124', '125')


# this will do addition
def xyz(a, b):
    """This function takes 
      two numbers as input and 
      returns their sum.
      eg. xyz(5, 10) will return 15
      """
    return a + b

def check_for_abusive_words(prompt_text, abusive_words):
    flag_abusive = False
    for word in abusive_words:
        if word.lower() in prompt_text.lower():
            print(f"The text contains abusive word: {word}")
            flag_abusive = True
    return flag_abusive
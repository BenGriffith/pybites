from typing import Type


def get_profile(name, age, *args, **kwargs):

    # Validations
    if not isinstance(age, int):
        raise ValueError

    if len(args) > 5:
        raise ValueError

    user_profile = {}

    user_profile["name"] = name
    user_profile["age"] = age

    if len(args) > 0:
        sport_list = [arg for arg in args]
        sport_list.sort()
        user_profile["sports"] = sport_list

    if len(kwargs) > 0:
        award_dict = {key: value for key, value in kwargs.items()}
        user_profile["awards"] = award_dict
    
    return user_profile

#if __name__ == "__main__":
    #print(get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis'))
    #print(get_profile('tim', 36, 'tennis'))
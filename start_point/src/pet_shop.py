# 1
def get_pet_shop_name(dict):
    return dict["name"]

#2
def get_total_cash(dict):
    return dict["admin"]["total_cash"]

#3.1
# def add_or_remove_cash(dict, cash):
#     dict["admin"]["total_cash"] += cash
#     return dict["admin"]["total_cash"]

#3.2
def add_or_remove_cash(dict, cash):
    dict["admin"]["total_cash"] += cash
    return get_total_cash(dict)

#4
def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]

#5 
def increase_pets_sold(dict, pet_num):
    dict["admin"]["pets_sold"] += pet_num
    return get_pets_sold(dict)
#6
def get_stock_count(dict):
    return len(dict["pets"])
#7
def get_pets_by_breed(dict, breed):
    return len(dict[breed])



     




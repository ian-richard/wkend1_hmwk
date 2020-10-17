import  pdb
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

#3 #4
def add_or_remove_cash(dict, cash):
    dict["admin"]["total_cash"] += cash
    return get_total_cash(dict)

#5
def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]

#6
def increase_pets_sold(dict, pet_num):
    dict["admin"]["pets_sold"] += pet_num
    return get_pets_sold(dict)
#7
def get_stock_count(dict):
    return len(dict["pets"])
#8 & #9
def get_pets_by_breed(pet_shop, pet_breed):
    pets_list = []
    for animal in pet_shop["pets"]:
        if animal["breed"] == pet_breed:
            pets_list.append(animal)
    return pets_list

#error 7
    # pdb.set_trace()
    # pets = []
    # for item in dict:
    #     if item["breed"] == pet_breed:
    #         pets.append(item["breed"])
#10 &  11
def find_pet_by_name(pet_shop, animal_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == animal_name:
            return pet

#12
def remove_pet_by_name(pet_shop, animal_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == animal_name:
            pet_shop["pets"].remove(pet)
    return find_pet_by_name(pet_shop, animal_name)

#13
def add_pet_to_stock(pet_shop, new_animal):
    pet_shop["pets"].append(new_animal)
    return get_stock_count(pet_shop)

#14
def get_customer_cash(customer):
    return customer["cash"]

#15
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return customer["cash"]

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return get_customer_pet_count(customer)





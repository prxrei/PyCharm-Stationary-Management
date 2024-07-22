#Yong Xuan Wei Johan , 235008L, IT2153-01

#Sorting Methods and other methods/functions (such as display and populate) to run certain features in the system .

from stationary import Stationary
from populateData import populateData
import random

stationary_dict = {}


def display_stationary():
    if stationary_dict:
        for item in stationary_dict.values():
            product_id = item.get_product_id()
            product_name = item.get_product_name()
            product_category = item.get_category()
            product_brand = item.get_brand()
            product_supplier_since = item.get_supplier_since()
            product_stock = item.get_stock()
            print("-----------------------------------------------------------------")
            print(f"Product ID: {product_id} \nProduct Name: {product_name} \nProduct Category: {product_category} \nBrand: {product_brand} \nSupplier Year: {product_supplier_since} \nStock: {product_stock}")
        print("-----------------------------------------------------------------")
    else:
        print("There are currently no products in the system!")


#Function used to generate a suggested product id which is close to the product id entered but already exists
def generate_suggestion(existing_id):
    base_id = existing_id[:2]
    last_digits = int(existing_id[2:])
    #Suggests a new product id using a random increment
    suggestion = f"{base_id}{str(last_digits + random.randint(1, 10)).zfill(4)}"
    #Using a while loop, if the suggested product id exists then continue the random increment until the suggested product id does not exist.
    while suggestion in stationary_dict:
        suggestion = f"{base_id}{str(last_digits + random.randint(1, 10)).zfill(4)}"
    return suggestion


def add_stationary():
    while True:
        prod_id = input("Enter Product ID (format: PDxxxx) or type 0 to return to main menu: ").upper()

        if prod_id == '0':
            return  # Return to main menu if 0 is chosen

        if not (prod_id.startswith("PD") and prod_id[2:].isdigit()):
            print("Invalid format! Product ID should start with 'PD' and contain digits for the rest of the product ID.")
            continue  # Prompt user to re-enter the Product ID

        if prod_id in stationary_dict:
            print("Product ID already exists! Please enter a unique Product ID.")
            suggestion = generate_suggestion(prod_id)
            print(f"Suggested Product ID: {suggestion}")
            continue  # Prompt user to re-enter the Product ID

        break  # Exit the loop if Product ID is valid and unique

    while True:
        prod_name = input("Enter Product Name or type 0 to return to main menu: ")
        if prod_name.lower() == '0':
            return  # Return to main menu if 0 is chosen
        break

    while True:
        category = input("Enter Category or type 0 to return to main menu: ")
        if category.lower() == '0':
            return  # Return to main menu if 0 is chosen
        break

    while True:
        brand = input("Enter Brand or type 0 to return to main menu: ")
        if brand.lower() == '0':
            return  # Return to main menu if 0 is chosen
        break

    while True:
        supplier_since = input(
            "Enter Supplier Since (year between 1900 and 2100) or type 0 to return to main menu: ")

        if supplier_since.lower() == '0':
            return  # Return to main menu if 0 is chosen

        if supplier_since.isdigit() and 1900 <= int(supplier_since) <= 2100:
            supplier_since = int(supplier_since)
            break
        else:
            print("Invalid input! Year should be a 4-digit number between 1900 and 2100.")

    new_stationary = Stationary(prod_id, prod_name, category, brand, supplier_since)
    new_stationary.set_product_id(prod_id)
    new_stationary.set_product_name(prod_name)
    new_stationary.set_category(category)
    new_stationary.set_brand(brand)
    new_stationary.set_supplier_since(supplier_since)
    stationary_dict[prod_id] = new_stationary
    print("Product added successfully!\n")


def optimized_bubble_sort_by_category():
    #Assigns the list of dictionary values to stationary_list
    stationary_list = list(stationary_dict.values())
    n = len(stationary_list)
    #For loop(Outer), going through the whole stationary_list
    for i in range(n):
        flag = False
        # For loop(Inner), going through the whole stationary_list and swap elements if condition met.
        for j in range(0, n-i-1):
            #If the category of index j is smaller than that of index j+1, it swaps both objects
            if stationary_list[j].get_category() < stationary_list[j+1].get_category():
                stationary_list[j], stationary_list[j+1] = stationary_list[j+1], stationary_list[j]
                flag = True
        if not flag:
            break
        print(f"Pass {i + 1}:\n------------------------------------------")
        for item in stationary_list:
            print(item.product_id)
        print("------------------------------------------")
    return stationary_list


#Improved insertion sort algorithm by adding the "=" to "<" becoming "<=" in the comparison in the while loop.
def insertion_sort_by_brand():
    # Assigns the list of dictionary values to stationary_list
    stationary_list = list(stationary_dict.values())
    # For loop, going through the whole stationary_list from the 2nd element
    for i in range(1, len(stationary_list)):
        #Create a placeholder to store the values temporarily
        key = stationary_list[i]
        j = i - 1
        # As long as j is >= 0 and the brand of key is less than the brand of stationary_list[j]
        while j >= 0 and key.get_brand() <= stationary_list[j].get_brand():
            #Push the element in j backwards by assigning it to [j+1].
            stationary_list[j + 1] = stationary_list[j]
            #Continue to go to the front the list until the placeholder's value is larger than the compared value
            j -= 1
        #As the loop ends, the placeholder is now inserted into its rightful position at [j+1] which was where the placeholder's value was larger than the compared value in the last index in the loop.
        stationary_list[j + 1] = key
        print(f"Pass {i}:\n------------------------------------------")
        for item in stationary_list:
            print(item.product_id)
        print("------------------------------------------")
    return stationary_list


def populatingData():
    product_list = populateData()
    for product in product_list:
        #Check if product is in Dictionary, add product to Dictionary only if it does not exist.
        if product.get_product_id() in stationary_dict:
            print("Product already exists, entry not added to System")
        else:
            stationary_dict[product.get_product_id()] = product


#A function used to print the Stationary Details that are in a new list, different from display_stationary which prints the Stationary Details directly from the original Dictionary populated by populateData
def product_display(item):
    product_id = item.get_product_id()
    product_name = item.get_product_name()
    product_category = item.get_category()
    product_brand = item.get_brand()
    product_supplier_since = item.get_supplier_since()
    return f"Product ID: {product_id} \nProduct Name: {product_name} \nProduct Category: {product_category} \nBrand: {product_brand} \nSupplier Year: {product_supplier_since}"


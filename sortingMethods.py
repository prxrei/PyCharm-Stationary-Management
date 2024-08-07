# Yong Xuan Wei Johan , 235008L, IT2153-01

# Sorting Methods and other methods/functions (such as display and populate) to run certain features in the system .

from stationary import Stationary
from stationary import RestockDetail
from populateData import populateData
from stationary import Queue
import random

stationary_dict = {}
RestockingQ = Queue()


def get_item_attributes(item):
    return [
        f"Product ID: {item.get_product_id()}",
        f"Product Name: {item.get_product_name()}",
        f"Product Category: {item.get_category()}",
        f"Brand: {item.get_brand()}",
        f"Supplier Year: {item.get_supplier_since()}",
        f"Stock: {item.get_stock()}"
    ]


def display_stationary(records_per_row=1, index=0, attr_idx=0):
    all_items = list(stationary_dict.values())
    max_attributes = 6
    column_width = 50

    # Base case: if the index is greater than or equal to the length of all_items, stop recursion
    if index >= len(all_items):
        return

    # Get the current row of items to display based on the records_per_row and current index
    current_row = all_items[index:index + records_per_row]
    # Generate a list of attributes for each item in the current row
    items = [get_item_attributes(item) for item in current_row]

    # Check if the current attribute index is less than the maximum number of attributes
    if attr_idx < max_attributes:
        # Iterate through the list of attributes and print the current attribute for each item
        for attr in items:
            print(attr[attr_idx][:column_width].ljust(column_width), end="")
        print()
        # Recursive call to print the next attribute for the current row
        display_stationary(records_per_row, index, attr_idx + 1)
    else:
        # If all attributes for the current row have been printed, move to the next row
        print("\n")
        display_stationary(records_per_row, index + records_per_row, 0)


# Function used to generate a suggested product id which is close to the product id entered but already exists
def generate_suggestion(existing_id):
    base_id = existing_id[:2]
    last_digits = int(existing_id[2:])
    # Suggests a new product id using a random increment
    suggestion = f"{base_id}{str(last_digits + random.randint(1, 10)).zfill(4)}"
    # Using a while loop, if the suggested product id exists then continue the random increment until the suggested product id does not exist.
    while suggestion in stationary_dict:
        suggestion = f"{base_id}{str(last_digits + random.randint(1, 10)).zfill(4)}"
    return suggestion


def add_stationary():
    while True:
        prod_id = input("Enter Product ID (format: PDxxxx) or type 0 to return to main menu: ").upper()

        if prod_id == '0':
            return  # Return to main menu if 0 is chosen

        if not (prod_id.startswith("PD") and prod_id[2:].isdigit()):
            print(
                "Invalid format! Product ID should start with 'PD' and contain digits for the rest of the product ID.")
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

    while True:
        stock = input("Enter Stock Quantity (positive integer) or type 0 to return to main menu: ")

        if stock.lower() == '0':
            return  # Return to main menu if 0 is chosen

        if stock.isdigit() and int(stock) > 0:
            stock = int(stock)
            break
        else:
            print("Invalid input! Stock should be a positive integer.")

    new_stationary = Stationary(prod_id, prod_name, category, brand, supplier_since, stock)
    new_stationary.set_product_id(prod_id)
    new_stationary.set_product_name(prod_name)
    new_stationary.set_category(category)
    new_stationary.set_brand(brand)
    new_stationary.set_supplier_since(supplier_since)
    new_stationary.set_stock(stock)
    stationary_dict[prod_id] = new_stationary
    print("Product added successfully!\n")


def optimized_bubble_sort_by_category():
    # Assigns the list of dictionary values to stationary_list
    stationary_list = list(stationary_dict.values())
    n = len(stationary_list)
    # For loop(Outer), going through the whole stationary_list
    for i in range(n):
        flag = False
        # For loop(Inner), going through the whole stationary_list and swap elements if condition met.
        for j in range(0, n - i - 1):
            # If the category of index j is smaller than that of index j+1, it swaps both objects
            if stationary_list[j].get_category() < stationary_list[j + 1].get_category():
                stationary_list[j], stationary_list[j + 1] = stationary_list[j + 1], stationary_list[j]
                flag = True
        if not flag:
            break
        print(f"Pass {i + 1}:\n------------------------------------------")
        for item in stationary_list:
            print(item.product_id)
        print("------------------------------------------")

    return stationary_list


# Improved insertion sort algorithm by adding the "=" to "<" becoming "<=" in the comparison in the while loop.
def insertion_sort_by_brand():
    # Assigns the list of dictionary values to stationary_list
    stationary_list = list(stationary_dict.values())
    # For loop, going through the whole stationary_list from the 2nd element
    for i in range(1, len(stationary_list)):
        # Create a placeholder to store the values temporarily
        key = stationary_list[i]
        j = i - 1
        # As long as j is >= 0 and the brand of key is less than the brand of stationary_list[j]
        while j >= 0 and key.get_brand() <= stationary_list[j].get_brand():
            # Push the element in j backwards by assigning it to [j+1].
            stationary_list[j + 1] = stationary_list[j]
            # Continue to go to the front the list until the placeholder's value is larger than the compared value
            j -= 1
        # As the loop ends, the placeholder is now inserted into its rightful position at [j+1] which was where the placeholder's value was larger than the compared value in the last index in the loop.
        stationary_list[j + 1] = key
        print(f"Pass {i}:\n------------------------------------------")
        for item in stationary_list:
            print(item.product_id)
        print("------------------------------------------")

    return stationary_list


def merge_sort_by_category_then_stock(stationary_list):
    if len(stationary_list) <= 1:
        return stationary_list

    mid = len(stationary_list) // 2
    left = merge_sort_by_category_then_stock(stationary_list[:mid])
    right = merge_sort_by_category_then_stock(stationary_list[mid:])

    merged = merge_sort(left, right)

    # Print the merged list for this pass
    print("New List:\n" + "-" * 40)
    for item in merged:
        print(f"Prod_id: {item.get_product_id()}")
    print("-" * 40)

    return merged


def merge_sort(left, right):
    if not left:
        return right
    if not right:
        return left

    if (left[0].get_category(), left[0].get_stock()) <= (right[0].get_category(), right[0].get_stock()):
        return [left[0]] + merge_sort(left[1:], right)
    else:
        return [right[0]] + merge_sort(left, right[1:])


def selection_sort_by_prod_id():
    stationary_list = list(stationary_dict.values())
    n = len(stationary_list)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if stationary_list[j].get_product_id() > stationary_list[max_idx].get_product_id():
                max_idx = j
        stationary_list[i], stationary_list[max_idx] = stationary_list[max_idx], stationary_list[i]
        print(f"Pass {i + 1}:\n------------------------------------------")
        for item in stationary_list:
            print(item.get_product_id())
        print("------------------------------------------")

    update_stationary_dict(stationary_list)

    return stationary_list


def populatingData():
    product_list = populateData()
    stationary_dict.clear()

    for product in product_list:
        if product.get_product_id() in stationary_dict:
            print("Product already exists, entry not added to System")
        else:
            stationary_dict[product.get_product_id()] = product


# A function used to print the Stationary Details that are in a new list, different from display_stationary which prints the Stationary Details directly from the original Dictionary populated by populateData
# Function to display the stationary list from a given list
def product_display(stationary_list, records_per_row=1, index=0, attr_idx=0):
    max_attributes = 6
    column_width = 50

    if index >= len(stationary_list):
        return

    current_row = stationary_list[index:index + records_per_row]
    attributes = [get_item_attributes(item) for item in current_row]

    if attr_idx < max_attributes:
        for attr in attributes:
            print(attr[attr_idx][:column_width].ljust(column_width), end="")
        print()
        product_display(stationary_list, records_per_row, index, attr_idx + 1)
    else:
        print("\n")
        product_display(stationary_list, records_per_row, index + records_per_row, 0)


def update_stationary_dict(sorted_list):
    stationary_dict.clear()
    stationary_dict.update({item.get_product_id(): item for item in sorted_list})


def add_stock_arrival_to_queue():
    prod_id = input("Enter Product ID: ").upper()

    if prod_id not in stationary_dict:
        print("Invalid Product ID. Please try again!")
        return

    quantity = int(input("Enter quantity to restock: "))

    restock_detail = RestockDetail(prod_id, quantity)
    RestockingQ.enqueue(restock_detail)
    print(f"Restocking Arrival Queued Successfully.")


def view_stock_arrival_in_queue():
    print(f"Number of Restocking in queue: {RestockingQ.length()}")


def handle_next_stock_arrival_in_queue():
    if RestockingQ.isEmpty():
        print("No deliveries to handle.")
        return

    restock_detail = RestockingQ.dequeue()
    prod_id = restock_detail.prod_id
    quantity = restock_detail.quantity

    print("Display Pending stock arrival:")
    print("-" * 40)
    print(f"Product ID: {prod_id}")
    print(f"Product Name: {stationary_dict[prod_id].get_product_name()}")
    print(f"Product Category: {stationary_dict[prod_id].get_category()}")
    print(f"Brand: {stationary_dict[prod_id].get_brand()}")
    print(f"Supplier Year: {stationary_dict[prod_id].get_supplier_since()}")
    print(f"Stock remaining: {stationary_dict[prod_id].get_stock()}")
    print("-" * 40)
    print(f"New Stock: {quantity}")
    print("-" * 40)

    action = input("Proceed with restocking (Y/N): ").upper()

    if action == 'Y':
        new_stock = stationary_dict[prod_id].get_stock() + quantity
        stationary_dict[prod_id].set_stock(new_stock)
        print(f"Prod id: {prod_id} updated stock: {new_stock}")
        print(f"Remaining restock in queue: {RestockingQ.length()}")
    else:
        RestockingQ.enqueue(restock_detail)
        print(f"Product {prod_id} re-queued!")

    print(f"\nThere are {RestockingQ.length()} deliveries remaining in the queue.\n")

#Yong Xuan Wei Johan , 235008L, IT2153-01

from sortingMethods import display_stationary, add_stationary, optimized_bubble_sort_by_category, \
    insertion_sort_by_brand, populatingData, product_display, stationary_dict, selection_sort_by_prod_id, \
    merge_sort_by_category_then_stock, add_stock_arrival_to_queue, view_stock_arrival_in_queue, handle_next_stock_arrival_in_queue


#Main Menu Console
def stationarymenu():
    print("Stationary Management Menu:")
    print("1. Add New Stationary")
    print("2. Display Stationary Details")
    print("3. Sort Stationary via Bubble Sort on Category (Descending Order)")
    print("4. Sort Stationary via Insertion Sort on Brand (Ascending Order)")
    print("5. Sort Stationary via Selection Sort on Prod Id")
    print("6. Sort Stationary via Merge Sort on Category followed by Stock (Ascending Order)")
    print("7. Go to Restocking Menu")
    print("8. Set number of records per row to display")
    print("9. Populate Data")
    print("0. Exit Program")
    print("")


#Main function to run the system.
def stationarymenu():
    print("Stationary Management Menu:")
    print("1. Add New Stationary")
    print("2. Display Stationary Details")
    print("3. Sort Stationary via Bubble Sort on Category (Descending Order)")
    print("4. Sort Stationary via Insertion Sort on Brand (Ascending Order)")
    print("5. Sort Stationary via Selection Sort on Prod Id (Descending Order)")
    print("6. Sort Stationary via Merge Sort on Category followed by Stock (Ascending Order)")
    print("7. Go to Restocking Menu")
    print("8. Set number of records per row to display")
    print("9. Populate Data")
    print("0. Exit Program")
    print("")


def restocking_menu():
    print("Restocking Menu:")
    print("1. Enter New Stock Arrival")
    print("2. View Number of Stock Arrival")
    print("3. Service Next Restock in Queue")
    print("0. Return to Main Menu")
    print("")


def main():
    records_per_row = 1
    while True:
        stationarymenu()
        choice = input("Please select one: ")
        if choice == '1':
            add_stationary()
        elif choice == '2':
            print("Product List:")
            print("-" * 200)
            display_stationary(records_per_row)
            print("-" * 200)
        elif choice == '3':
            sorted_list = optimized_bubble_sort_by_category()
            print("Sort Stationary via Optimized Bubble Sort on Category (Descending Order):")
            product_display(sorted_list, records_per_row)
        elif choice == '4':
            sorted_list = insertion_sort_by_brand()
            print("Sort Stationary via Insertion Sort on Brand (Ascending Order):")
            product_display(sorted_list, records_per_row)
        elif choice == '5':
            sorted_list = selection_sort_by_prod_id()
            print("Sort Stationary via Selection Sort on Prod id (Descending Order)")
            product_display(sorted_list, records_per_row)
        elif choice == '6':
            sorted_list = merge_sort_by_category_then_stock(list(stationary_dict.values()))
            print("Sort Stationary via Merge Sort on Category followed by Stock (Ascending Order)")
            product_display(sorted_list, records_per_row)
        elif choice == '7':
            while True:
                restocking_menu()
                restock_choice = input("Please select one: ")
                if restock_choice == '1':
                    add_stock_arrival_to_queue()
                elif restock_choice == '2':
                    view_stock_arrival_in_queue()
                elif restock_choice == '3':
                    handle_next_stock_arrival_in_queue()
                elif restock_choice == '0':
                    break
                else:
                    print("Invalid choice! Please try again.")
        elif choice == '8':
            while True:
                try:
                    total_items = len(stationary_dict)
                    records_per_row = int(input("Enter number of records per row (default is 1): "))
                    if records_per_row < 1:
                        raise ValueError("Number of records per row must be at least 1.")
                    if total_items < records_per_row:
                        raise ValueError("Not enough items in the system to display that many records per row.")
                    print(f"Number of records to display per row is set to {records_per_row}.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
        elif choice == '9':
            populatingData()
        elif choice == '0':
            print("Good Bye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()


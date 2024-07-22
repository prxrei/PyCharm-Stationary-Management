#Yong Xuan Wei Johan , 235008L, IT2153-01

from sortingMethods import display_stationary, add_stationary, optimized_bubble_sort_by_category, insertion_sort_by_brand, populatingData, product_display

#Main Menu Console
def stationarymenu():
    print("Stationary Management Menu:")
    print("1. Add New Stationary")
    print("2. Display Stationary Details")
    print("3. Sort Stationary via Bubble Sort on Category.(Descending Order)")
    print("4. Sort Stationary via Insertion Sort on Brand.(Ascending Order)")
    print("5. Sort Stationary via Selection Sort on Prod Id.()")
    print("6. Sort Stationary via Merge Sort on Category followed by Stock. (Ascending Order)")
    print("7. Go to Restocking Menu")
    print("8. Set number of records per row to display")
    print("9. Populate Data")
    print("0. Exit Program")
    print("")

#Main function to run the system.
def main():
    while True:
        stationarymenu()
        choice = input("Please select one: ")

        if choice == '1':
            add_stationary()
        elif choice == '2':
            print("Product List:")
            display_stationary()
        elif choice == '3':
            sorted_list = optimized_bubble_sort_by_category()
            print("Sort Stationary via Optimized Bubble Sort on Category.(Descending Order):")
            print("Product List:")
            for item in sorted_list:
                print("-----------------------------------------------------------------")
                print(product_display(item))
            print("-----------------------------------------------------------------")
        elif choice == '4':
            sorted_list = insertion_sort_by_brand()
            print("Sort Stationary via Insertion Sort on Brand.(Ascending Order):")
            print("Product List:")
            for item in sorted_list:
                print("-----------------------------------------------------------------")
                print(product_display(item))
            print("-----------------------------------------------------------------")
        elif choice == '9':
            populatingData()
        elif choice == '0':
            print("Good Bye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()

#Yong Xuan Wei Johan , 235008L, IT2153-01

#Stationary Class with all the Getters and Setters(Get and Set methods)

class Stationary:
    def __init__(self, prod_id, prod_name, category, brand, supplier_since, stock):
        self.product_id = prod_id
        self.product_name = prod_name
        self.category = category
        self.brand = brand
        self.supplier_since = supplier_since
        self.stock = stock

    #Get Methods to retrieve data from the Stationary Class
    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_category(self):
        return self.category

    def get_brand(self):
        return self.brand

    def get_supplier_since(self):
        return self.supplier_since

    def get_stock(self):
        return self.stock


    #Set Methods to update data to the Stationary Class, hardly used for this assignment since there is no updating.
    def set_product_id(self, value):
        self.product_id = value

    def set_product_name(self, value):
        self.product_name = value

    def set_category(self, value):
        self.category = value

    def set_brand(self, value):
        self.brand = value

    def set_supplier_since(self, value):
        self.supplier_since = value

    def set_stock(self, value):
        self.stock = value



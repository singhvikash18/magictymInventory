from django.db import models

Type =(('01','Individual'),('02','Bussiness'))
GSTChoice =(('1','item1'),('2','item2'),('3','item3'))
PlaceSupply = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
TaxChoice =(('01','Taxable'),('02','Exempted'))
Money =(('USA','USD'),('India','Indian-Rupee'),('European-Union','Euro'),('UAE','Dirham'),('China','Yuan')) 
Term =(('01','Net 45'),('02','Due of the end'),('03','Net 15'),('04','Due Receipt'))
PriceOption =(('A','from 1'),('B','from 2'))


class Customer(models.Model):
    customer_type =models.CharField(max_length=10,choices=Type,default='01')
    company_name = models.CharField(max_length=30)
    customer_fullname = models.CharField(max_length=20)
    customer_email =models.CharField(max_length=20)
    customer_phone =models.CharField(max_length=15)
    GST_treatment = models.CharField(max_length=20,choices=GSTChoice,default='1')
    PlaceOfSupply = models.CharField(max_length= 40,choices=PlaceSupply,default="Assam")
    Tax_preference = models.CharField(max_length=10,choices=TaxChoice,default='01')
    Currency = models.CharField(max_length=20,choices=Money,default='India')
    Payment_Terms =models.CharField(max_length=20,choices=Term,default='02')
    Price_list = models.CharField(max_length=20,choices=PriceOption,default='A')
    Billing_Address_country = models.CharField(max_length=20,default="India")
    Billing_Address =models.CharField(max_length=100,default="Street 1")
    Billing_Address_city =models.CharField(max_length=20,default="road")
    Billing_Address_State =models.CharField(max_length=20,default="Delhi")
    Billing_Address_ZipCode =models.CharField(max_length=10,default="110001")
    Shipping_Address_country = models.CharField(max_length=20,default="India")
    Shipping_Address =models.CharField(max_length=100,default="Street 1")
    Shipping_Address_city =models.CharField(max_length=20,default="Delhi")
    Shipping_Address_State =models.CharField(max_length=20,default="Delhi")
    Shipping_Address_ZipCode =models.CharField(max_length=10,default="110001")
    Remarks =models.TextField(max_length=200,default="any remarks")



    



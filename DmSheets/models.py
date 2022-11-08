
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.forms import DateField








class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number, email, Employee_type,branch_name, password=None):
        
        if not phone_number:
            raise ValueError('The phone_number must be Set')
        if not name:
            raise ValueError("User Must have a  name") 

        if not email :
            raise ValueError("User Must have a email") 
               
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            branch_name=branch_name,
            Employee_type = Employee_type,
            phone_number = phone_number,
        
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self ,phone_number,email,branch_name, name, Employee_type, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.   
        """
        user = self.create_user(
            name = name,
            email= email,
            branch_name=branch_name,
            Employee_type = Employee_type,
            phone_number = phone_number or  "superadmin2022",
            password = password

      
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using = self._db)
        return user    

############ Custom User Model ###########

class CustomUser(AbstractBaseUser):
    Employee_type=[
        ("Admin",'Admin'),
        ("Accountant",'Accountant'),
        ("Go-Down",'Go-Down'),
    ]
    Employee_type=models.CharField(max_length=30,choices=Employee_type,null=True,blank=True)
    email = models.EmailField(verbose_name = 'email',max_length=255,)
    name = models.CharField(max_length = 200,null=True,blank=True)
    branch_name=[
        ("Vijayawada-Gas-Company",'Vijayawada-Gas-Company'),
        ("Hema-Gas-Company",'Hema-Gas-Company,'),
        ("Sri-Balaji-Gas Company",'Sri-Balaji-Gas-Company'),
    ]
    branch_name = models.CharField(max_length=30,choices=branch_name,null=True,blank=True)

    phone_number = models.CharField(max_length = 20,unique=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_superuser = models.BooleanField(default = False)



   

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    PHONE_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['Employee_type','email','name','branch_name']

    def __str__(self):
      return self.phone_number

    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

    def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

    @property
    def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class GasAgencyProducts(models.Model):


    Select_Category=[
        ("14.2kgs" ,'14.2kgs'),
        ("19kgs" ,'19kgs'),
        ("47.5kgs" ,'47.5kgs'),
        ("5kgs" ,'5kgs'),
    ]

    Select_Category=models.CharField(max_length=1000,choices=Select_Category,blank=True,null=True)
    date=models.DateField(null=True)
    Opening_DBTL=models.CharField(max_length=1000,blank=True,null=True) 
    Opening_NONSUB=models.CharField(max_length=1000,blank=True,null=True) 
    Opening_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Otheroils=models.CharField(max_length=1000,blank=True,null=True)

    Hpcl_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Otheroils=models.CharField(max_length=1000,blank=True,null=True)

    Sale_DBTL=models.CharField(max_length=1000,blank=True,null=True) 
    Sale_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Otheroils=models.CharField(max_length=1000,blank=True,null=True)

    Tv_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Tv_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Otheroils=models.CharField(max_length=1000,blank=True,null=True)

    Total_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Total_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Total_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Total_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Total_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Total_Otheroils=models.CharField(max_length=1000,blank=True,null=True)

    
    Sale_DBTL1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_NONSUB1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Shortage1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Otheroils1=models.CharField(max_length=1000,blank=True,null=True)
    




   
    Crd_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Crd_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Otheroils=models.CharField(max_length=1000,blank=True,null=True)


   
     
    Nc_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Nc_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Otheroils=models.CharField(max_length=1000,blank=True,null=True)


   

  
    Tadepalli_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Otheroils=models.CharField(max_length=1000,blank=True,null=True)


    

     
    Prcn_DBTL=models.CharField(max_length=1000,blank=True,null=True) 
    Prcn_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Otheroils=models.CharField(max_length=1000,blank=True,null=True)


   

    closing_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    closing_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    closing_Empity=models.CharField(max_length=1000,blank=True,null=True)
    closing_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    closing_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    closing_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)
    


class Branch(models.Model):
    date=models.DateField(auto_now_add=True,null=True,blank=True)

    name=models.CharField(max_length=50,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)



class Branch_name(models.Model):
    Branch_namecompany_one=models.CharField(max_length=100,null=True,blank=True)
    Branch_namecompany_two=models.CharField(max_length=100,null=True,blank=True)
    Branch_namecompany_three=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)


class Depositfrombank(models.Model):

    user=models.CharField(max_length=1000,null=True,blank=True)
    IOB=models.CharField(max_length=1000,null=True,blank=True)
    HDFC=models.CharField(max_length=1000,null=True,blank=True)
    Bharat_Pay=models.CharField(max_length=1000,null=True,blank=True)
    Bobby_chitts=models.CharField(max_length=1000,null=True,blank=True)
    Online_Bills=models.CharField(max_length=1000,null=True,blank=True)
    OneTown_Autodisels=models.CharField(max_length=1000,null=True,blank=True)
    John_credit=models.CharField(max_length=1000,null=True,blank=True)
    Nsl=models.CharField(max_length=1000,null=True,blank=True)
    Ap16tv1918repaire=models.CharField(max_length=1000,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)



    
    IOB_date=models.DateField(null=True,blank=True)
    HDFC_date=models.DateField(null=True,blank=True)
    Bharat_Pay_date=models.DateField(null=True,blank=True)
    Bobby_chitts_date=models.DateField(null=True,blank=True)
    Online_Bills_date=models.DateField(null=True,blank=True)
    OneTown_Autodisels_date=models.DateField(null=True,blank=True)
    John_credit_date=models.DateField(null=True,blank=True)
    Nsl_date=models.DateField(null=True,blank=True)
    Ap16tv1918repaire_date=models.DateField(null=True,blank=True)
 
   
    
   

  

  

class bankdetails(models.Model):
     user=models.CharField(max_length=100,null=True,blank=True)
     created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)

     bank = models.ForeignKey(Depositfrombank,on_delete=models.CASCADE)
     date = models.DateField(auto_now_add=True,null=True,blank=True)
     IOB = models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
     HDFC = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     Bharat_Pay = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     Bobby_chitts = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)


     Online_Bills = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     OneTown_Autodisels = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     John_credit = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     Nsl = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
     Ap16tv1918repaire = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)


class product(models.Model):
    # branch_name=[
    #     ("Vijayawada-Gas-Company",'Vijayawada-Gas-Company'),
    #     ("Hema-Gas-Company",'Hema-Gas-Company,'),
    #     ("Sri-Balaji-Gas Company",'Sri-Balaji-Gas-Company'),
    # ]
    # branch_name = models.CharField(max_length=30,choices=branch_name,null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)
   
    fourteebpoint_twokg_sale=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    extra_sale=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    five_kgRefilsale_one=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    five_kgRefilsale_two=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    nineteen_pointtwo_KGS=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    VGC_CRD=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)
    






class product_BulkSale(models.Model):

    Customer_name=models.CharField(max_length=20,null=True,blank=True)
    fourtysevenpointfivekg_quantity=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    Nineteenkg_quantity=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)



class general_quantities(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    fourteebpoint_twokg_sale=models.IntegerField(null=True,blank=True)
    extra_sale=models.IntegerField(null=True,blank=True)
    five_kgRefilsale_one=models.IntegerField(null=True,blank=True)
    five_kgRefilsale_two=models.IntegerField(null=True,blank=True)
    nineteen_pointtwo_KGS=models.IntegerField(null=True,blank=True)
    VGC_CRD=models.IntegerField(null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)
    



class totalamount1(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)

    product=models.ForeignKey('product',on_delete=models.CASCADE)
    general_quantities=models.ForeignKey('general_quantities',on_delete=models.CASCADE)
    fourteebpoint_twokg_sale=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    extra_sale=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    five_kgRefilsale_one=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    five_kgRefilsale_two=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    nineteen_pointtwo_KGS=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    VGC_CRD=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    
    class Meta:
        unique_together=(("product","general_quantities"),)





class bulkprice(models.Model):

   
    
    customer_name=models.CharField(max_length=20,null=True,blank=True)
    fourtysevenpointfive_kgprice=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    nineteen_kgprice=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    quantity_fourtysevenpointfive_kgprice=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    quantity_nineteen_kgprice=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2, null=True,blank=True)
    user=models.CharField(max_length=100,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)

   
    date=models.DateField(auto_now_add=True, null=True,blank=True)

    

    


class totalamount2(models.Model):

    user=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    date_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    ARB_DBT_W_K=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    SV_TV_Amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)


class fourteenpointtwo(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)


    Opening_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Opening_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Sale_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Sale_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Sale_DBTL1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_NONSUB1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity1=models.CharField(max_length=1000,blank=True,null=True)
    Tv_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Tv_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Total_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Total_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Total_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Nc_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Nc_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Empity=models.CharField(max_length=1000,blank=True,null=True)
    closing_DBTL=models.CharField(max_length=1000,blank=True,null=True)
    closing_NONSUB=models.CharField(max_length=1000,blank=True,null=True)
    closing_Empity=models.CharField(max_length=1000,blank=True,null=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)

   







class Nineteenm(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)

    Opening_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Shortage1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity1=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Total_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Total_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Total_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Empity=models.CharField(max_length=1000,blank=True,null=True)

    Tadepalli_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Empity=models.CharField(max_length=1000,blank=True,null=True)
    closing_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    closing_Shortage=models.CharField(max_length=1000,blank=True,null=True)
    closing_Empity=models.CharField(max_length=1000,blank=True,null=True)
    user=models.CharField(max_length=100,null=True,blank=True)

    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)




class Fourtysevenpointfive(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    Opening_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    
    Opening_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Empity=models.CharField(max_length=1000,blank=True,null=True)
    
    Sale_Fulls=models.CharField(max_length=1000,blank=True,null=True)
  
    Sale_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls1=models.CharField(max_length=1000,blank=True,null=True)
    
    Sale_Empity1=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    
    Tv_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Total_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    
    Total_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Fulls=models.CharField(max_length=1000,blank=True,null=True)
   
    Crd_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Fulls=models.CharField(max_length=1000,blank=True,null=True)
   
    Nc_Empity=models.CharField(max_length=1000,blank=True,null=True)

    Tadepalli_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    
    Tadepalli_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Fulls=models.CharField(max_length=1000,blank=True,null=True)
   
    Prcn_Empity=models.CharField(max_length=1000,blank=True,null=True)
    closing_Fulls=models.CharField(max_length=1000,blank=True,null=True)
  
    closing_Empity=models.CharField(max_length=1000,blank=True,null=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)
    


class five(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    Opening_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Opening_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Hpcl_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Fulls1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Otheroils1=models.CharField(max_length=1000,blank=True,null=True)
    Sale_Empity1=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Tv_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Total_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Total_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Total_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Crd_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Nc_Empity=models.CharField(max_length=1000,blank=True,null=True)

    Tadepalli_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Tadepalli_Empity=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    Prcn_Empity=models.CharField(max_length=1000,blank=True,null=True)
    closing_Fulls=models.CharField(max_length=1000,blank=True,null=True)
    closing_Otheroils=models.CharField(max_length=1000,blank=True,null=True)
    closing_Empity=models.CharField(max_length=1000,blank=True,null=True)
    created_by=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_by=models.DateTimeField(auto_now=True,null=True,blank=True)
 
 

class credit(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(max_length=1000,null=True,blank=True)
    Bulk_price=models.CharField(max_length=1000,null=True,blank=True)
    Bank=models.CharField(max_length=1000,null=True,blank=True)
    credit_sale=models.CharField(max_length=1000,null=True,blank=True)
    total_credit_sale=models.CharField(max_length=1000,null=True,blank=True)



class pending_amount(models.Model):
    user=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(max_length=1000,null=True,blank=True)
    pending_money=models.CharField(max_length=1000,null=True,blank=True)
    credit_sale=models.CharField(max_length=1000,null=True,blank=True)
    total_credit_sale=models.CharField(max_length=1000,null=True,blank=True)



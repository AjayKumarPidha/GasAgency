from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework import *
from .models import *
import tokenize
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

USER_DETAILS_SERIALIZER = 'rest_auth.views.UserDetailsView' 

##############  Register ###########################


class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['Employee_type','id','email', 'name', 'branch_name' ,'phone_number','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }


    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)


##############  Login ###########################

class loginserializers(serializers.ModelSerializer):
    phone_number = serializers.CharField()    
    class Meta:
        model = CustomUser
        fields=['phone_number','password']



class forgetpwdserializers(serializers.ModelSerializer):
    phone_number = serializers.CharField()    
    class Meta:
        model = CustomUser
        fields=['phone_number','password']


##############  Login ###########################


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'phone_number','email','branch_name','Employee_type' ,'password']




class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['Employee_type','id','email', 'name', 'branch_name' ,'phone_number']



class EmployeedeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id']
        

class fourteenpointtwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = fourteenpointtwo
        fields = ['id','Opening_DBTL','Opening_NONSUB','Opening_Empity','Hpcl_NONSUB','Hpcl_Empity','Hpcl_DBTL','Sale_DBTL','Sale_NONSUB','Sale_Empity', 'Sale_DBTL1','Sale_NONSUB1','Sale_Empity1','Tv_DBTL','Tv_NONSUB','Tv_Empity','Total_DBTL',  'Total_NONSUB','Total_Empity','Crd_DBTL','Crd_NONSUB','Crd_Empity', 'Nc_DBTL','Nc_NONSUB','Nc_Empity','Tadepalli_DBTL','Tadepalli_NONSUB','Tadepalli_Empity','Prcn_DBTL',   'Prcn_NONSUB','Prcn_Empity','closing_DBTL','closing_NONSUB',  'closing_Empity']


class fourteenpointtwo_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasAgencyProducts
        fields = ['id','Opening_DBTL','Opening_NONSUB','Opening_Empity','Hpcl_NONSUB','Hpcl_Empity','Hpcl_DBTL','Sale_DBTL','Sale_NONSUB','Sale_Empity', 'Sale_DBTL1','Sale_NONSUB1','Sale_Empity1','Tv_DBTL','Tv_NONSUB','Tv_Empity','Total_DBTL',  'Total_NONSUB','Total_Empity','Crd_DBTL','Crd_NONSUB','Crd_Empity', 'Nc_DBTL','Nc_NONSUB','Nc_Empity','Tadepalli_DBTL','Tadepalli_NONSUB','Tadepalli_Empity','Prcn_DBTL',   'Prcn_NONSUB','Prcn_Empity','closing_DBTL','closing_NONSUB',  'closing_Empity']

class NineteenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nineteenm
        fields = ['id','Opening_Fulls','Opening_Shortage' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Shortage','Hpcl_Empity','Sale_Fulls' ,'Sale_Shortage' ,'Sale_Empity','Tv_Fulls',  'Tv_Shortage',  'Tv_Empity', 'Total_Fulls'  ,'Total_Shortage'  ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Shortage1' ,'Sale_Empity1', 'Crd_Fulls', 'Crd_Shortage', 'Crd_Empity','Nc_Fulls' ,'Nc_Shortage' ,'Nc_Empity' ,'Tadepalli_Fulls', 'Tadepalli_Shortage' ,'Tadepalli_Empity' ,'Prcn_Fulls'  , 'Prcn_Shortage'  , 'Prcn_Empity' ,'closing_Fulls' ,'closing_Shortage'  ,'closing_Empity']


class Nineteen_listSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nineteenm
        fields = ['id','Opening_Fulls','Opening_Shortage' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Shortage','Hpcl_Empity','Sale_Fulls' ,'Sale_Shortage' ,'Sale_Empity','Tv_Fulls',  'Tv_Shortage',  'Tv_Empity', 'Total_Fulls'  ,'Total_Shortage'  ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Shortage1' ,'Sale_Empity1', 'Crd_Fulls', 'Crd_Shortage', 'Crd_Empity','Nc_Fulls' ,'Nc_Shortage' ,'Nc_Empity' ,'Tadepalli_Fulls', 'Tadepalli_Shortage' ,'Tadepalli_Empity' ,'Prcn_Fulls'  , 'Prcn_Shortage'  , 'Prcn_Empity' ,'closing_Fulls' ,'closing_Shortage'  ,'closing_Empity']


class FourtysevenpointfiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fourtysevenpointfive
        fields = ['id','Opening_Fulls' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Empity','Sale_Fulls'  ,'Sale_Empity','Tv_Fulls',    'Tv_Empity', 'Total_Fulls'    ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Empity1', 'Crd_Fulls',  'Crd_Empity','Nc_Fulls' ,'Nc_Empity' ,'Tadepalli_Fulls','Tadepalli_Empity','Prcn_Fulls', 'Prcn_Empity','closing_Fulls','closing_Empity']



class Fourtysevenpointfive_listSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fourtysevenpointfive
        fields = ['id','Opening_Fulls' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Empity','Sale_Fulls'  ,'Sale_Empity','Tv_Fulls',    'Tv_Empity', 'Total_Fulls'    ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Empity1', 'Crd_Fulls',  'Crd_Empity','Nc_Fulls' ,'Nc_Empity' ,'Tadepalli_Fulls','Tadepalli_Empity' ,'Prcn_Fulls'   , 'Prcn_Empity' ,'closing_Fulls'   ,'closing_Empity']


class FiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = five

        fields = ['id','Opening_Fulls','Opening_Otheroils' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Otheroils','Hpcl_Empity','Sale_Fulls' ,'Sale_Otheroils' ,'Sale_Empity','Tv_Fulls',  'Tv_Otheroils',  'Tv_Empity', 'Total_Fulls'  ,'Total_Otheroils'  ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Otheroils1' ,'Sale_Empity1', 'Crd_Fulls', 'Crd_Otheroils', 'Crd_Empity','Nc_Fulls' ,'Nc_Otheroils' ,'Nc_Empity' ,'Tadepalli_Fulls', 'Tadepalli_Otheroils' ,'Tadepalli_Empity' ,'Prcn_Fulls'  , 'Prcn_Otheroils'  , 'Prcn_Empity' ,'closing_Fulls' ,'closing_Otheroils'  ,'closing_Empity']


class Five_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = five

        fields = ['id','Opening_Fulls','Opening_Otheroils' ,'Opening_Empity','Hpcl_Fulls' ,'Hpcl_Otheroils','Hpcl_Empity','Sale_Fulls' ,'Sale_Otheroils' ,'Sale_Empity','Tv_Fulls',  'Tv_Otheroils',  'Tv_Empity', 'Total_Fulls'  ,'Total_Otheroils'  ,'Total_Empity', 'Sale_Fulls1' ,'Sale_Otheroils1' ,'Sale_Empity1', 'Crd_Fulls', 'Crd_Otheroils', 'Crd_Empity','Nc_Fulls' ,'Nc_Otheroils' ,'Nc_Empity' ,'Tadepalli_Fulls', 'Tadepalli_Otheroils' ,'Tadepalli_Empity' ,'Prcn_Fulls'  , 'Prcn_Otheroils'  , 'Prcn_Empity' ,'closing_Fulls' ,'closing_Otheroils'  ,'closing_Empity']



class Branchname_serializer(serializers.ModelSerializer):
    class Meta:
        model=Branch_name
     
        fields=['id','Branch_namecompany_one','Branch_namecompany_two','Branch_namecompany_three','date']



class Branchname_serializer(serializers.ModelSerializer):
    class Meta:
        model=Branch_name
     
        fields=['id','Branch_namecompany_one','Branch_namecompany_two','Branch_namecompany_three','date']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=['id','name','location']


class BranchdeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=['id']


class Pricedepositserializer(serializers.ModelSerializer):
    class Meta:
        model=Depositfrombank
        fields=['id','IOB','HDFC' ,'Bharat_Pay','Bobby_chitts','Online_Bills','OneTown_Autodisels','John_credit','Nsl', 'Ap16tv1918repaire','IOB_date','HDFC_date' ,'Bharat_Pay_date','Bobby_chitts_date','Online_Bills_date','OneTown_Autodisels_date','John_credit_date','Nsl_date', 'Ap16tv1918repaire_date' ]

class bankdetailserializer(serializers.ModelSerializer):
    class Meta:
        model=bankdetails
        fields=['IOB','HDFC' ,'Bharat_Pay','Bobby_chitts','Online_Bills','OneTown_Autodisels','John_credit','Nsl', 'Ap16tv1918repaire','IOB_date','HDFC_date' ,'Bharat_Pay_date','Bobby_chitts_date','Online_Bills_date','OneTown_Autodisels_date','John_credit_date','Nsl_date', 'Ap16tv1918repaire_date' ]


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one','five_kgRefilsale_two', 'nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']


class Productlist_serializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one','five_kgRefilsale_two', 'nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']



class Productupdateserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one','five_kgRefilsale_two', 'nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']


class Product_bulk_updateserializer(serializers.ModelSerializer):
    class Meta:
        model=bulkprice
        fields=['id','customer_name','fourtysevenpointfive_kgprice','nineteen_kgprice','date','quantity_fourtysevenpointfive_kgprice', 'quantity_nineteen_kgprice', 'total']




class bulksaleserializer(serializers.ModelSerializer):
    class Meta:
        model=product_BulkSale
        fields=['id','Customer_name', 'fourtysevenpointfivekg_quantity' , 'Nineteenkg_quantity' ,'date']



class bulksales_listserializer(serializers.ModelSerializer):
    class Meta:
        model=product_BulkSale
        fields=['id','Customer_name', 'fourtysevenpointfivekg_quantity' , 'Nineteenkg_quantity' ,'date']



class bulksales_deleteserializer(serializers.ModelSerializer):
    class Meta:
        model=product_BulkSale
        fields=['id','date']

class generalquantitieslist_serializer(serializers.ModelSerializer):
    class Meta:
        model=general_quantities
        fields=['id','fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one', 'five_kgRefilsale_two','nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']

class generalquantities_serializer(serializers.ModelSerializer):
    class Meta:
        model=general_quantities
        fields=['id','fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one', 'five_kgRefilsale_two','nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']

class generalquantities_updateserializer(serializers.ModelSerializer):
    class Meta:
        model=general_quantities
        fields=['id','fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one', 'five_kgRefilsale_two','nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']


class bulkprice_serializer(serializers.ModelSerializer):
    class Meta:
        model=bulkprice
        fields=['customer_name','fourtysevenpointfive_kgprice','nineteen_kgprice','date','quantity_fourtysevenpointfive_kgprice', 'quantity_nineteen_kgprice', 'total']



class bulkpricelist_serializer(serializers.ModelSerializer):
    class Meta:
        model=bulkprice
        fields=['id','customer_name','fourtysevenpointfive_kgprice','nineteen_kgprice','date','quantity_fourtysevenpointfive_kgprice', 'quantity_nineteen_kgprice', 'total']


class bulkprice_add_serializer(serializers.ModelSerializer):
    class Meta:
        model=bulkprice
        fields=['id','quantity_fourtysevenpointfive_kgprice', 'quantity_nineteen_kgprice', 'total']


class bulkpricedelete_serializer(serializers.ModelSerializer):
    class Meta:
        model=bulkprice
        fields=['id','date']


class totalamount1_serializer(serializers.ModelSerializer):
    class Meta:
        model=totalamount1
        fields=['id','fourteebpoint_twokg_sale','extra_sale',  'five_kgRefilsale_one', 'five_kgRefilsale_two','nineteen_pointtwo_KGS', 'VGC_CRD' ,'date']



class totalamount2_serializer(serializers.ModelSerializer):
    class Meta:
        model=totalamount2
        fields=[ 'id','date', 'date_amount','ARB_DBT_W_K',  'SV_TV_Amount','user']


class totalamount2list_serializer(serializers.ModelSerializer):
    class Meta:
        model=totalamount2
        fields=[ 'id','date', 'date_amount','ARB_DBT_W_K',  'SV_TV_Amount','user']

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

       


class credit_add_serializer(serializers.ModelSerializer):
    class Meta:
        model=credit
        fields=['id','date','Bulk_price','Bank','credit_sale','total_credit_sale']

class credit_list_serializer(serializers.ModelSerializer):
    class Meta:
        model=credit
        fields=['id','date','total_credit_sale']


class pending_amount_serializer(serializers.ModelSerializer):
    class Meta:
        model=pending_amount 
        fields=['id','date','pending_money']

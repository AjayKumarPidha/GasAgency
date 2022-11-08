from ast import Delete
from email.policy import HTTP
from functools import partial
from lib2to3.pgen2 import token
from pickle import TRUE
from sre_constants import SUCCESS
from statistics import quantiles
from tokenize import Triple
from urllib import request, response
from django.shortcuts import render
from decimal import *
from rest_framework import generics
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  *
from .serializers import pending_amount_serializer,credit_list_serializer,credit_add_serializer,totalamount2list_serializer, generalquantitieslist_serializer,forgetpwdserializers,BranchSerializer,bulkprice_add_serializer, LogoutSerializer,Branchname_serializer,totalamount2_serializer,totalamount1_serializer,generalquantities_updateserializer, totalamount2_serializer,bulkpricedelete_serializer,bulksales_deleteserializer,Product_bulk_updateserializer,bulkpricelist_serializer,Productlist_serializer,bulkprice_serializer,bulksales_listserializer,EmployeeListSerializer, EmployeeUpdateSerializer, EmployeedeleteSerializer, FiveSerializer, FourtysevenpointfiveSerializer, NineteenSerializer, Pricedepositserializer,Productserializer, Registerserializers, bulksaleserializer, fourteenpointtwoSerializer, loginserializers,bankdetailserializer,generalquantities_serializer,Productupdateserializer ,fourteenpointtwo_listSerializer ,Five_listSerializer ,Fourtysevenpointfive_listSerializer ,Nineteen_listSerializer

from DmSheets import serializers
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

################ RegisterList ###################


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {

        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterList(APIView):

    def post(self,request):

        phone = request.data['phone_number']
        print(phone)
        
        serializer=Registerserializers(data = request.data)
      
      
        branch_name=request.data['branch_name']
        print(branch_name)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status':'True','msg':"User registrations successfully!",'data':serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({'status':'False','msg':"User Not  registered  "}, status=status.HTTP_400_BAD_REQUEST)





################ LoginList ###################


class LoginView(APIView):

    def post(self, request, format=None):
        serializer = loginserializers(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number')
            password = serializer.data.get('password')
            print(phone_number)
            print(password)
            user = authenticate(phone_number=phone_number, password=password)

            
            if user is not None:

                if user.Employee_type == "Admin":
                    print(user)
              
                    token = get_tokens_for_user(user)
                   
                    return Response({'status':'True', 'message':'Admin User Succesful', 'token':token,'Employee_type':user.Employee_type})
                
                #    'id':user.id
              
                    
                if user.Employee_type =="Accountant":
                    print(user)
              
                    token = get_tokens_for_user(user)
                   
                    return Response({'status':'True', 'message':'Accountant User Succesful', 'token':token,'Employee_type':user.Employee_type})

                if user.Employee_type =="Go-Down":
                    print(user)
              
                    token = get_tokens_for_user(user)
                    return Response({'status':'True', 'message':'Go-Down User Succesful', 'token':token,'Employee_type':user.Employee_type})

            else: 
                return Response({"status":"False", "message":"Invalid Phone Number Or password"})    
            return Response({'status':'False', 'message':'404 Bad Request', 'errors':serializer.errors})

                  




################ ShowList ###################
             
class EmployeeListshow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk=None,format=None):
     id=pk
     if id is not None:
      stu=CustomUser.objects.get(id=id)
      serializer=EmployeeListSerializer(stu)
      return Response({'status':'True','msg':"list successfully",'data':serializer.data})

     stu = CustomUser.objects.all()
     serializer = EmployeeListSerializer(stu,many=True) 
     return Response({'status':'True','msg':'list successfully','data':serializer.data})




class EmployeeUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request, id,format=None):
        if CustomUser.objects.filter(id=id).exists():

            fourteen=CustomUser.objects.get(id=id)
            
            Serializer = EmployeeUpdateSerializer(fourteen, data=request.data, partial=True)

            if Serializer.is_valid():

                Serializer.save()
                return Response({'status':'True','msg':'Complete data updated successfully'},status=status.HTTP_200_OK)
            return Response({'status':'False','msg':' data is not updated '},status=status.HTTP_400_BAD_REQUEST)




class EmployeeDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):
        
        

          user_id = request.data["id"]
          print(user_id)
          data=CustomUser.objects.get(pk=user_id)
        
        
          data.delete()
          return Response({'status':'true',"msg":"User Delete Sucessfully"},status=status.HTTP_200_OK)

    

        
class Fourteenpointtwo(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
      
       
        serializer = fourteenpointtwoSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save(user=request.user)
            return Response({'status':'True', 'message':'data save Successfully',"data":serializer.data})



class Fourteenpointtwo_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):


        if fourteenpointtwo.objects.filter(user=request.user).exists():
           data=fourteenpointtwo.objects.filter(user=request.user).latest('updated_by')
          
           serializer=fourteenpointtwo_listSerializer(data)
           return Response({'msg':'Data save Successfully','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)


class Totalamount2_view(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        
        serializer=totalamount2_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True','msg':'General Amount sucessfully','data':serializer.data})
  



class Totalamount2_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formet=None):
        
        
        if totalamount2.objects.filter(user=request.user).exists():
           data=totalamount2.objects.filter(user=request.user).latest('updated_by')
          
           serializer=totalamount2list_serializer(data)
           return Response({'msg':'Totalamount1 successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)


class Five(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,format=None):
      
        serializer=FiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True', 'message':'data save Successfully',"data":serializer.data})





class Five_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if five.objects.filter(user=request.user).exists():
           data=five.objects.filter(user=request.user).latest('updated_by')
          
           serializer=FiveSerializer(data)
           return Response({'msg':'Data save Successfully','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)

        # data=five.objects.order_by('-updated_by').first()
        # serializer=FiveSerializer(data)
        # return Response({"status":'True',"msg":'data save Successfully',"data":serializer.data})









       


class Nineteen(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = NineteenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True', 'message':'Data save Successfully',"data":serializer.data})
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)



class Nineteen_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if Nineteenm.objects.filter(user=request.user).exists():
           data=Nineteenm.objects.filter(user=request.user).latest('updated_by')
          
           serializer=NineteenSerializer(data)
           return Response({'msg':'Data save Successfully','status':'True',"data":serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)







class fourtysevenpointfive_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if Fourtysevenpointfive.objects.filter(user=request.user).exists():
           data=Fourtysevenpointfive.objects.filter(user=request.user).latest('updated_by')
          
           serializer=FourtysevenpointfiveSerializer(data)
           return Response({'msg':'Data save Successfully','status':'True',"data":serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'false','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)


# class fourtysevenpointfive_list(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         if Fourtysevenpointfive.objects.filter(user=request.user).exists():
#            data=Fourtysevenpointfive.objects.filter(user=request.user).latest('updated_by')
          
#            serializer=Fourtysevenpointfive_listSerializer(data)
#            return Response({'msg':'data save Successfully','status':'True','data':serializer.data},status=status.HTTP_200_OK)
#         return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)





class fourtysevenpointfive(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
      
        serializer=FourtysevenpointfiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True', 'message':'Data  save Successfully',"data":serializer.data})




    

# class Fourteenpointtwo_list(APIView):
#     permission_classes=[IsAuthenticated]
 
#     def post(self,request):
#          id=request.data.get('id')
#          print(id)


#          if GasAgencyProducts.objects.filter(id=id).exists():
#                data=GasAgencyProducts.objects.get(id=id)
#                print(data)
#                serializer=fourteenpointtwoSerializer(data)
#                return Response({'status':'True','msg':'list Successfully','data':serializer.data})
#          return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

    
        
       



# class Nineteen_list(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request):
#         id=request.data.get('id')
#         if GasAgencyProducts.objects.filter(id=id).exists():
#             data=GasAgencyProducts.objects.get(id=id)
#             serializer=NineteenSerializer(data)
#             return Response({"status":'True',"msg":'Nineteen_list',"data":serializer.data})
#         return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

    


# class fourtysevenpointfive(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request,format=None):
      
#         serializer=FourtysevenpointfiveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'True', 'message':'data  save Successfully',"data":serializer.data})



# class fourtysevenpointfive_list(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request):
#         id=request.data.get('id')
#         if GasAgencyProducts.objects.filter(id=id).exists():
#             data=GasAgencyProducts.objects.get(id=id)
#             serializer=FourtysevenpointfiveSerializer(data)
#             return Response({"status":'True',"msg":'fourtysevenpointfive',"data":serializer.data})
#         return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)






       
       

# class Five_list(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request):
#         id=request.data.get('id')
#         if GasAgencyProducts.objects.filter(id=id).exists():
#             data=GasAgencyProducts.objects.get(id=id)
#             serializer=FiveSerializer(data)
#             return Response({"status":'True',"msg":'Five_list',"data":serializer.data})
#         return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

       

class BrancAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id=None,format=None):
        if id is not None:
            data=Branch.objects.get(id=id)
            Serializers=BranchSerializer(data)
            return Response({'status':'True','messege':'Branch Recent Details Successfully',"data":Serializers.data})

        
        data=Branch.objects.all()
        Serializers=BranchSerializer(data,many=True)
        return Response({'status':'True','messege':'Branch Recent Details Successfully',"data":Serializers.data})

class Branchname_view(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formet=None):
        data=Branch_name.objects.all()
        serializer=Branchname_serializer(data,many=True)
        return Response({'status':'True','messege':"successfully",'data':serializer.data})


class BranchView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        Serializer=BranchSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save(user=request.user)
            return Response({'status':'True','msg':'Branch  Successfully'})
        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

       


class BrancDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):
        user_id = request.data["id"]
        print(user_id)
        data=Branch.objects.get(id=user_id)
        
        data.delete()
        return Response({'status':'true',"msg":"User Delete Sucessfully"},status=status.HTTP_200_OK)







        
        
        
class pricedeposit_update(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id,format=None):
        if Depositfrombank.objects.filter(id=id).exists():
            data=Depositfrombank.objects.get(id=id)
            serializer=Pricedepositserializer(data,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'True','messege':'Recent list',"data":serializer.data})

            return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

        
        





# class pricedeposit_list(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         data=Depositfrombank.objects.order_by('-updated_by').first()
#         serializer=Pricedepositserializer(data)
#         return Response({'status':'True', 'message':'Recent  DepositRupeefromBank successfully', "data": serializer.data})

       
       
    

        

             

        

 
            
class Bank_detailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
       

        my_bank = bankdetails.objects.all()
        serializer = bankdetailserializer(my_bank, many=True)
        return Response({'status':'True', 'message':'Bank details successfully', "data": serializer.data})


class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'status':'True', 'message':'Product details successfully',"data":serializer.data})
        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

       



# class product_list(APIView):
#     permission_classes=[IsAuthenticated]

#     def get(self,request,formet=None):

#         # if product.objects.filter(user=request.user).exists():
#         #    data=product.objects.filter(user=request.user).latest('updated_by')
          
#         #    serializer=Productlist_serializer(data)
#         #    return Response({'msg':'data save Successfully','status':'True','data':serializer.data},status=status.HTTP_200_OK)
#         # return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)

class product_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data=product.objects.order_by('-updated_by').first()
        serializer=Productlist_serializer(data)
        
        
        return Response({'status':'True','messege':'Data save successfully',"data":serializer.data})


# class product_list(APIView):
#     def get(self,request):
#         product_list=product.objects.all()
#         Serializer=Productlist_serializer(product_list,many=True)
#         return Response({'status':'True','messege':'product_list successfully',"data":Serializer.data})


class productupdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id,formet=None):
        if product.objects.filter(id=id).exists():
            price=product.objects.get(id=id)
            Serializer=Productupdateserializer(price,data=request.data,partial=True)
            if Serializer.is_valid():
                Serializer.save()
                return Response({"status":"true","msg":'Updated Successfully'},status=status.HTTP_200_OK)
            return Response({"status":"False","msg":"data is not update"},status=status.HTTP_400_BAD_REQUEST)








class product_bulkpriceupdate(APIView): 
    permission_classes = [IsAuthenticated]
    def put(self,request, id,format=None):
     if bulkprice.objects.filter(id=id).exists():
        product = bulkprice.objects.get(id=id)
        Serializer = Product_bulk_updateserializer(product, data=request.data, partial=True)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'status':'True','msg':'Complete product bulkpriceupdate updated'})
        return Response({'errors':Serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class product_bilksale(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,formet=None):
        serializer=bulksaleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

        return Response({'status':'True','message':'Product bulksale successfully','data':serializer.data})


class product_bulksalelist(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,formet=None):
        if product_BulkSale.objects.filter(user=request.user).exists():
           data=product_BulkSale.objects.filter(user=request.user).latest('updated_by')
          
           serializer=bulksaleserializer(data)
           return Response({'msg':'Product bulksalelist successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)




class product_bulksaleupdate(APIView): 
    permission_classes = [IsAuthenticated]
    
    def put(self,request, id,format=None):
     if product_BulkSale.objects.filter(id=id).exists():
        product = product_BulkSale.objects.get(id=id)
    
        Serializer = bulksaleserializer(product, data=request.data, partial=True)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'status':'true','msg':'Complete product bulksaleupdate updated'})
        return Response({'status':'false','errors':Serializer.errors}, status=status.HTTP_400_BAD_REQUEST)









  

class Pricedeposit(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = Pricedepositserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True', 'message':'Recent  DepositRupeefromBank successfully', "data": serializer.data})
       
         

        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)



class general_quantityapi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer=generalquantities_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'true','msg':"General quantityapi created successfully",'data':serializer.data})





#         serializer=generalquantities_serializer(data)

       
#         return Response({'status':'True','msg':'general_quantitylist successfully created','data':serializer.data})
    

# class general_quantitylist(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request,formet=None):
         
#         if general_quantities.objects.filter(user=request.user).exists():
#            data=general_quantities.objects.filter(user=request.user).latest('updated_by')
          
#            serializer=generalquantitieslist_serializer(data)
#            return Response({'msg':'general_quantitylist successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
#         return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)




class pricedeposit_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
          
        if Depositfrombank.objects.filter(user=request.user).exists():
           data=Depositfrombank.objects.filter(user=request.user).latest('updated_by')
          
           serializer=Pricedepositserializer(data)
           return Response({'msg':'Pricedeposit list successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)



        # data=Depositfrombank.objects.order_by('-updated_by').first()
        # serializer=Pricedepositserializer(data)
        # return Response({'msg':'pricedeposit_list successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        
       
        # data=Depositfrombank.objects.get(id=id)
        # serializer=Pricedepositserializer(data)
       
        # return Response({'status':'True','messege':'Recent list',"data":serializer.data})




class general_quantitylist(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formet=None):
         
        if general_quantities.objects.filter(user=request.user).exists():
           data=general_quantities.objects.filter(user=request.user).latest('updated_by')
          
           serializer=generalquantitieslist_serializer(data)
           return Response({'msg':'General quantitylist successfully','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)

       





       







# class general_quantitylist(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request,formet=None):['20', '50', '100', '345', '609'] 
#         data=general_quantities.objects.order_by('-updated_by').first()
#         serializer=generalquantities_serializer(data)

       
#         return Response({'status':'True','msg':'general_quantitylist successfully created','data':serializer.data})
    
        
        

class general_quantityupdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        if general_quantities.objects.filter(id=id).exists():
            product=general_quantities.objects.get(id=id)
            serializer=generalquantities_updateserializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'True','msg':'General_quantity successfully updated'})
            return Response({'status':'True','errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)




# class product_bilksale(APIView):
#     def post(self,request,formet=None):
#         serializer=bulksaleserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#         return Response({'status':'True','message':'product_bilksale successfully'})


class bulkprice_View(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,formet=None):
       
        serializer=bulkprice_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'True','msg':'bulkprice_add successfully'})
        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)

    


class bulkprice_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formet=None):
        product=bulkprice.objects.all()
        Serializer=bulkpricelist_serializer(product,many=True)
        return Response({'status':'True','msg':'Bulkprice list  successfully',"data":Serializer.data})




class bulkprice_add(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id,formet=None):
        if bulkprice.objects.filter(id=id).exists():
           add=bulkprice.objects.get(id=id)
           serializer=bulkprice_add_serializer(add,data=request.data,partial=True)
           if serializer.is_valid():
               serializer.save()
               return Response({'status':'True','msg':'Bulkprice_add successfully',"data":serializer.data})











# class credit_add(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request,formet=None):
#         serializer=credit_add_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response({'status':'True','msg':'credit_add successfully'})
#         return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)















class amount(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,formet=None):
        serializer=pending_amount_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status':'True','msg':'Pending_amount successfully',"data":serializer.data})
        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)







           


# class general_quantitylist(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request,formet=None):
         
#         if general_quantities.objects.filter(user=request.user).exists():
#            data=general_quantities.objects.filter(user=request.user).latest('updated_by')
          
#            serializer=generalquantitieslist_serializer(data)
#            return Response({'msg':'general_quantitylist successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
#         return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)







class general_quantitylist(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formet=None):
         
        if general_quantities.objects.filter(user=request.user).exists():
           data=general_quantities.objects.filter(user=request.user).latest('updated_by')
          
           serializer=generalquantitieslist_serializer(data)
           return Response({'msg':'General_quantitylist successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)




class credit_add(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,formet=None):
        serializer=credit_add_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
           
            return Response({'status':'True','msg':'Credit_add successfully',"data":serializer.data})
        return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)




class credit_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,formet=None):
        if credit.objects.filter(user=request.user).exists():
            data = credit.objects.filter(user=request.user).all()
               
          
            serializer=credit_list_serializer(data, many=True)
            return Response({'msg':'Credit_list successfully created','status':'True',"data":serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)


        
        # data=credit.objects.all()
          
        # serializer=credit_list_serializer(data,many=True)
        # return Response({'msg':'credit_list successfully created','status':'True','data':serializer.data},status=status.HTTP_200_OK)
   










class pending_amount_list(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,formet=None):
        if pending_amount.objects.filter(user=request.user).exists():
           data=pending_amount.objects.filter(user=request.user).all()
          
           serializer=pending_amount_serializer(data,many=True)
           return Response({'msg':'Pending amount list list successfully created','status':'True',"data":serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)

       


       
           
       



# class bulkprice_add(APIView):
#     def post(self,request,id):
       
#         data=bulkprice.objects.all()
#         serializer=bulkprice_add_serializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'True','msg':'bulkprice list one created successfully',"data":serializer.data})






class bulkprice_delete(APIView):
    def post(self,request,formet=None):
        user_id=request.data['id']
        data=bulkprice.objects.get(pk=user_id)

        data.delete()
        return Response({'status':'True','msg':'Bulkprice deleted successfully'})




        
            

class productbulk_saledelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user_id=request.data['id']
        data=product_BulkSale.objects.get(pk=user_id)
        data.delete()
        return Response({'status':'True','msg':'Productbulk_saledelete successfully'})

       


# class product_bulkpriceupdate(APIView):
#     def put(self,request,id,formet=None):
#         product=product_bulkprice.objects.get(id=id)
#         Serializer=Product_bulkserializer(product,data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             if product_bulkprice.objects.filter(id=id).exists():
#                product=product_bulkprice.objects.get(id=id)
#                Serializer=Product_bulkserializer(product)
#                return Response({'msg':'complete data updated', 'data':Serializer.data})
#             return Response(status=status.HTTP_400_BAD_REQUEST)

        
################ LoginList ###################







        
        


# class loginView(APIView):

#     def post(self,request):

#         serializer=loginserializers(data=request.data)
#         phone_number=serializer.data.Get['phone_number']
#         password=serializer.data.Get['password']
#         user=authenticate(phone_number=phone_number,password=password)
#         if user is not None:
#             if user.Employee_type=='Admin':
#                 token=get_tokens_for_user(user)
#                 return Response({'status':'True','msg':'login successfully',token:"token","Employee_type":user.Employee_type})

#             if user.Employee_type=="Accountant":
#                 token=get_tokens_for_user(user)
#                 return Response({'status':'True','msg':'Accountant successfully',token:"token","Employee_type":user.Employee_type})

#             if user.Employee_type=="Go_Down":
#                 token=get_tokens_for_user(user)
#                 return Response({'status':'True','msg':'Go_Dowm successfully',token:"token","Employee_type":user.Employee_type})

#         else: 
#           return Response({"status":"False", "message":"Invalid Phone Number Or password"})    
#         return Response({'status':'False', 'message':'404 Bad Request', 'errors':serializer.errors})




        

# class register(APIView):
#     def get(self,request):
#         serializer=Registerserializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'status':'True','msg':'registration successfully'},status=status.HTTP_200_OK)

#         else:

#           return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)
        

class Totalamount1_view(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):

        fourteebpoint_twokg_sale=request.data.get('fourteebpoint_twokg_sale')
        extra_sale=request.data.get('extra_sale')
        five_kgRefilsale_one=request.data.get('five_kgRefilsale_one')
        five_kgRefilsale_two=request.data.get('five_kgRefilsale_two')
        nineteen_pointtwo_KGS=request.data.get('nineteen_pointtwo_KGS')
        vgc_crd = request.data.get('VGC_CRD')

        if totalamount1.objects.filter(fourteebpoint_twokg_sale=fourteebpoint_twokg_sale,extra_sale=extra_sale,five_kgRefilsale_one=five_kgRefilsale_one,five_kgRefilsale_two=five_kgRefilsale_two,nineteen_pointtwo_KGS=nineteen_pointtwo_KGS,VGC_CRD=vgc_crd).exists():    
               data=totalamount1.objects.get(fourteebpoint_twokg_sale=fourteebpoint_twokg_sale,extra_sale=extra_sale,five_kgRefilsale_one=five_kgRefilsale_one,five_kgRefilsale_two=five_kgRefilsale_two,nineteen_pointtwo_KGS=nineteen_pointtwo_KGS,VGC_CRD=vgc_crd)
               serializer=totalamount1_serializer(data)

               if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response({'msg':'add successfully','status':'True','data':serializer.data})
               return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)



         
# if totalamount1.objects.filter(fourteebpoint_twokg_sale=fourteebpoint_twokg_sale,extra_sale=extra_sale,five_kgRefilsale_one=five_kgRefilsale_one,five_kgRefilsale_two=five_kgRefilsale_two,nineteen_pointtwo_KGS=nineteen_pointtwo_KGS,VGC_CRD=vgc_crd).exists():    
#
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'msg':'totalamount1 successfully created','status':'True','data':serializer.data})
        # return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)
 






# class pricedeposit_list(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         data=Depositfrombank.objects.order_by('-updated_by').first()
#         serializer=Pricedepositserializer(data)
#         return Response({'status':'True', 'message':'Recent  DepositRupeefromBank successfully', "data": serializer.data})

       










# class Totalamount2_list(APIView):
#     def get(self,request,formet=None):
#         data=totalamount2.objects.order_by('-updated_by').first()
#         serializer=totalamount2_serializer(data)
#         return Response({'status':'True','msg':'Totalamount2_list created sucessfully','data':serializer.data})





class UserLogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'True', 'message':'User is Logout'})
        return Response({'status':'False', 'message':'404 Bad Request', 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


  


class Forgetpasswordview(APIView):
    
    
    def post(self, request, format=None):
        
     
        user = CustomUser.objects.filter(phone_number=request.data['phone_number'])
        
        if user.exists():
            user=user.first()
            user.set_password(request.data['password'])
            user.save()
            
            return Response({'msg':'Password reset successfully!' , "success":"true"}, status=status.HTTP_200_OK) 
        else: 
            return Response({'msg':' User phone number Invalid', "success":"false" }, status=status.HTTP_400_BAD_REQUEST) 
  


# class forgetpassword(APIView):

#     def post(self,request,format=None):
#         user=CustomUser.objects.filter(phone_number=request.data['phone_number'])
#         if user.exists():
#             user.set_password(request.data['password'])
#             user.save()
#             return response({'msg':'Password reset successfully',"success":'True'},status=status.HTTP_200_OK)
#         else:
#             return response({'msg':'user phone_number invalid',"success":'False'},status=status.HTTP_400_OK)





              






# class bulkprice_View(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request,formet=None):
       
#         serializer=bulkprice_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(id=request.user.id)
#             return Response({'status':'True','msg':'bulkprice_add successfully'})
#         return Response({"status":"false"},status=status.HTTP_400_BAD_REQUEST)



# class bulkprice_list(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request,formet=None):
#         if bulkprice.objects.filter(id=request.user.id).exists():
#            data=bulkprice.objects.filter(id=request.user.id).all()
          
#            serializer=bulkpricelist_serializer(data,many=True)
#            return Response({'msg':'bulkprice_list successfully created','status':'True',"data":serializer.data},status=status.HTTP_200_OK)
#         return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)



        # product=bulkprice.objects.all()
        # Serializer=bulkpricelist_serializer(product,many=True)
        # return Response({'status':'True','msg':'Bulkprice list  successfully',"data":Serializer.data})





         

# class bulkprice_add(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request,id,formet=None):
#         serializer=bulkprice_add_serializer(data=request.data,partial=True)
#         if id is not None:
#             if bulkprice.objects.filter(id=request.user.id).exists():
#                 add=bulkprice.objects.filter(id=request.user.id).latest('updated_by')
#                 serializer=bulkprice_add_serializer(add,data=request.data,partial=True)
#                 if serializer.is_valid():
#                     serializer.save(id=request.user.id)
#                     return Response({'status':'True','msg':'Bulkprice_add successfully',"data":serializer.data})
#                 return Response({'status':'True','msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)





        



           
            
          
from django.urls import path,include
from DmSheets import views



urlpatterns=[

   path('employee-register',views.RegisterList.as_view(), name='register'),
   path('employee-login', views.LoginView.as_view(), name='login'),
   path('Forgetpassword', views.Forgetpasswordview.as_view(), name='Forgetpassword'),
   path('employeelist_show', views.EmployeeListshow.as_view(), name='employeelist_show'),
   path('employeelist_show/<int:id>', views.EmployeeListshow.as_view(), name='employeelist_show'),
   path('EmployeeUpdate/<int:id>', views.EmployeeUpdate.as_view(), name='EmployeeUpdate'),
   # path('Fourteenpointtwo/<int:id>', views.Fourteenpointtwo.as_view(), name='Fourteenpointtwo'),
   path('Fourteenpointtwo', views.Fourteenpointtwo.as_view(), name='Fourteenpointtwo'),

   path('Fourteenpointtwo_list', views.Fourteenpointtwo_list.as_view(), name='Fourteenpointtwo_list'),
   path('Nineteen', views.Nineteen.as_view(), name='Nineteen'),
   path('Nineteen_list', views.Nineteen_list.as_view(), name='Nineteen'),
   path('fourtysevenpointfive',views.fourtysevenpointfive.as_view(),name='fourtysevenpointfive'),
   path('fourtysevenpointfive_list',views.fourtysevenpointfive_list.as_view(),name='fourtysevenpointfive_list'),
   path('Five',views.Five.as_view(),name='Five'),
   path('Five_list',views.Five_list.as_view(),name='Five_list'),
   path('Branchlist',views.BrancAPI.as_view(),name='Branchlist'),
   path('Branchlist/<int:id>',views.BrancAPI.as_view(),name='Branchlist'),
   path('moneydepositbank',views.Pricedeposit.as_view(),name='moneydeposit'),
   path('moneydepositbank_list',views.pricedeposit_list.as_view(),name='pricedeposit_list'),

   path('moneydepositbank_update/<int:id>',views.pricedeposit_update.as_view(),name='pricedeposit_update'),
   path('Bank_details',views.Bank_detailsView.as_view(),name='Bank_details'),
   path('EmployeeDelete',views.EmployeeDelete.as_view(),name='EmployeeDelete'),
   
   path('generalprice',views.ProductView.as_view(),name='generalprice'),
   path('generalpriceupdate/<int:id>',views.productupdate.as_view(),name='generalpriceupdate'),
   path('generallist',views.product_list.as_view(),name='generallist'),

   path('product_bulkpriceupdate/<int:id>',views.product_bulkpriceupdate.as_view(),name='product_bulkpriceupdate'),
   path('product_bulksale',views.product_bilksale.as_view(),name='product_bulksale'),
   path('product_bulksalelist',views.product_bulksalelist.as_view(),name='bulksalelist'),
   path('product_bulksaleupdate/<int:id>',views.product_bulksaleupdate.as_view(),name='product_bulksaleupdate'),
   path('productbulk_saledelete',views.productbulk_saledelete.as_view(),name='productbulk_saledelete'),
   path('general_quantity',views.general_quantityapi.as_view(),name='general_quantitie'),
   path('general_quantityupdate/<int:id>',views.general_quantityupdate.as_view(),name='general_quantitie'),
   path('general_quantitylist',views.general_quantitylist.as_view(),name='general_quantitylist'),
   
   path('brachpost',views.BranchView.as_view(),name='general_quantitie'),
   path('BrancDelete/<int:id>',views.BrancDelete.as_view(),name='BrancDelete'),
   path('BrancDelete',views.BrancDelete.as_view(),name='BrancDeletee'),
   path('Branchname_company',views.Branchname_view.as_view(),name='Branchname_company'),
    
     
   path('bulkprice',views.bulkprice_View.as_view(),name='bulkpric'),
   path('bulkprice_add/<int:id>',views.bulkprice_add.as_view(),name='bulkprice_add'),
   path('bulkprice_add',views.bulkprice_add.as_view(),name='bulkprice_add'),
   path('bulkprice_list',views.bulkprice_list.as_view(),name='bulkprice_list'),
   path('bulkprice_delete',views.bulkprice_delete.as_view(),name='bulkprice_delete'),
   path('Totalamount1_view',views.Totalamount1_view.as_view(),name='Totalamount1_view'),
   path('Totalamount2_view',views.Totalamount2_view.as_view(),name='Totalamount1_view'),
   path('Totalamount2_list',views.Totalamount2_list.as_view(),name='Totalamount2list'),
   path('UserLogoutView',views.UserLogoutView.as_view(),name='UserLogoutView'),
   
   path('credit_add',views.credit_add.as_view(),name='credit_add'),
   path('credit_list',views.credit_list.as_view(),name='credit_list'),
   path('amountpending',views.amount.as_view(),name='amount'),
   path('pending_amount_list',views.pending_amount_list.as_view(),name='pending_amount_list')

]

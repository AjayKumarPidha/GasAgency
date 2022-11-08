

# Register your models here.

from django.contrib import admin


from .models import *

admin.site.register(CustomUser)
admin.site.register(GasAgencyProducts)
admin.site.register(Branch)

admin.site.register(Depositfrombank)
admin.site.register(bankdetails)
admin.site.register(product)
admin.site.register(bulkprice)
admin.site.register(product_BulkSale)
admin.site.register(totalamount1)
admin.site.register(general_quantities)
admin.site.register(totalamount2)
admin.site.register(Branch_name)
admin.site.register(credit)
admin.site.register(pending_amount)
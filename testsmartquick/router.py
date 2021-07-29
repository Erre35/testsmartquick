from clients.viewsets import ClientsViewset
from bills.viewsets import BillsProductsViewset, BillsViewset
from products.viewsets import ProductsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', ClientsViewset)
router.register('products', ProductsViewset)
router.register('bills', BillsViewset)
router.register('billsProducts', BillsProductsViewset)
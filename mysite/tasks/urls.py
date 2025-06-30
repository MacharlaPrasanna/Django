from django.urls import path
from .import views

urlpatterns = [
    path('',views.task_list, name='task_list'),
    path('math/<int:x>/<int:y>',views.math_operations,name='math_operations'),
    path('sum/<int:x>/<int:y>', views.sum, name='Addition'),
    path('difference/<int:x>/<int:y>', views.difference, name='Difference'),
    path('product/<int:x>/<int:y>', views.product, name='Product'),
    path('division/<int:x>/<int:y>', views.division, name='Division'),
]
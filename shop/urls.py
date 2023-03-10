from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from payment import views

urlpatterns = [
    path('webhooks/stripe/', views.stripe_webhook, name='stripe-webhook'),
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('', include(('order.urls', 'order'), namespace='order')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

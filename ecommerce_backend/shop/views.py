# shop/views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, Cart, OrderItem, Order # Pastikan Order sudah di-import
from .serializers import ProductSerializer, CartSerializer, OrderSerializer # Pastikan OrderSerializer di-import



@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
   
    cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Produk tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)

   
    if product.stock < quantity:
        return Response({"error": f"Stok tidak mencukupi. Sisa stok: {product.stock}"}, status=status.HTTP_400_BAD_REQUEST)


    cart, created = Cart.objects.get_or_create(user=user, ordered=False)

    order_item, item_created = OrderItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        if product.stock < (order_item.quantity + quantity):
            return Response({"error": "Total jumlah di keranjang melebihi stok yang tersedia"}, status=status.HTTP_400_BAD_REQUEST)
        order_item.quantity += quantity
    else:
        order_item.quantity = quantity
        
    order_item.save()
    return Response({"message": f"{product.name} berhasil ditambahkan ke keranjang"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user
    
    try:
        cart = Cart.objects.get(user=user, ordered=False)
    except Cart.DoesNotExist:
        return Response({"error": "Tidak ada keranjang aktif untuk di-checkout"}, status=status.HTTP_404_NOT_FOUND)
        
    
    if not cart.items.exists():
        return Response({"error": "Keranjang kamu masih kosong"}, status=status.HTTP_400_BAD_REQUEST)

    for item in cart.items.all():
        product = item.product
        if product.stock < item.quantity:
            return Response({"error": f"Stok {product.name} mendadak tidak mencukupi"}, status=status.HTTP_400_BAD_REQUEST)
        
        product.stock -= item.quantity
        product.save()

    cart.ordered = True
    cart.save()

    return Response({"message": "Checkout berhasil! Terima kasih sudah berbelanja."}, status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user
    
    try:
        cart = Cart.objects.get(user=user, ordered=False)
    except Cart.DoesNotExist:
        return Response({"error": "Tidak ada keranjang aktif untuk di-checkout"}, status=status.HTTP_404_NOT_FOUND)
        
    if not cart.items.exists():
        return Response({"error": "Keranjang kamu masih kosong"}, status=status.HTTP_400_BAD_REQUEST)

    total_price = 0
    for item in cart.items.all():
        product = item.product
        if product.stock < item.quantity:
            return Response({"error": f"Stok {product.name} tidak mencukupi"}, status=status.HTTP_400_BAD_REQUEST)
        
        total_price += product.price * item.quantity
        
        product.stock -= item.quantity
        product.save()


    cart.ordered = True
    cart.save()


    order = Order.objects.create(
        user=user,
        cart=cart,
        total_price=total_price
    )

    return Response({
        "message": "Checkout berhasil! Riwayat transaksi telah dicatat.",
        "nota_id": order.id,
        "total_pembayaran": total_price
    }, status=status.HTTP_200_OK)


api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-ordered_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
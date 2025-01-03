from rest_framework import serializers 
from .models import Product, Order, OrderItem, Category






class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),  
        slug_field='name',               
        allow_null=True                  
    )

    class Meta:
        model = Product
        fields = (
                'description',
                'name', 
                'price',
                'stock',
                'category'
                )
        
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero! ")
        return value
    


class CategorySerializer(serializers.ModelSerializer):
    products_list = serializers.SerializerMethodField(method_name="get_names")
    
    def get_names(self, obj):
        pd_list = obj.products.all()
        return [pd.name for pd in pd_list]
    class Meta:
        model = Category
        fields = (
            "category_id",
            "name", 
            "description",
            "products_list"
        )
        
        

    
    
class OrderItemSerilizer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2
        )
    
    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity', 'item_subtotal')
        
        
        
class OrderSerilizer(serializers.ModelSerializer):
    items = OrderItemSerilizer(many=True, read_only = True)
    total_price = serializers.SerializerMethodField(method_name='total')
    
    
    def total(self, obj):
        item_lists = obj.items.all()
        y = 0
        for x in item_lists:
            y+=x.item_subtotal
        return y
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'created_at',
            'status',
            'items',
            'total_price'
        )
    
class ProductInfoSerilizer(serializers.Serializer):
    product = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    
    
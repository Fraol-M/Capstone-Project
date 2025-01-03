import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from products.models import User, Product, Order, OrderItem, Category


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username='admin', defaults={"is_superuser": True, "is_staff": True})
        if created:
            user.set_password('test')
            user.save()

        categories = []
        category_data = [
            {"name": "Electronics", "description": lorem_ipsum.paragraph()},
            {"name": "Cloth", "description": lorem_ipsum.paragraph()},
            {"name": "Cosmetics", "description": lorem_ipsum.paragraph()},
            {"name": "Furniture", "description": lorem_ipsum.paragraph()},
            {"name": "Beverge", "description": lorem_ipsum.paragraph()},
            {"name": "Media", "description": lorem_ipsum.paragraph()},
            {"name": "Book", "description": lorem_ipsum.paragraph()},

        ]
        for data in category_data:
            category, created = Category.objects.get_or_create(
                name=data["name"], defaults={"description": data["description"]}
            )
            categories.append(category)
          
        categories_dict = {category.name: category for category in categories}

        products = [
            Product(name="A Scanner ", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4, category=categories_dict["Electronics"]),
            Product(name="Coffee Machine", description=lorem_ipsum.paragraph(), price=Decimal('70.99'), stock=6, category=categories_dict["Electronics"]),
            Product(name="Velvet Underground & Nico", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=11, category=categories_dict["Media"]),
            Product(name="Enter the Wu-Tang (36 Chambers)", description=lorem_ipsum.paragraph(), price=Decimal('17.99'), stock=2, category=categories_dict["Media"]),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('350.99'), stock=4, category=categories_dict["Electronics"]),
            Product(name="Atomic Habit", description=lorem_ipsum.paragraph(), price=Decimal('500.05'), stock=0, category=categories_dict["Book"]),
            Product(name="Lotion", description=lorem_ipsum.paragraph(), price=Decimal('200.05'), stock=0, category=categories_dict["Cosmetics"]),
            Product(name="Max-Energey drink", description=lorem_ipsum.paragraph(), price=Decimal('200.05'), stock=0, category=categories_dict["Beverge"]),

        ]
        Product.objects.bulk_create(products)

        for _ in range(3):
            order = Order.objects.create(user=user)
            for product in random.sample(products, 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1, 3)
                )

from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    """Платёжка"""
    name_bank = models.CharField(max_length=50, verbose_name="имя банка")
    detail = models.CharField(max_length=200, verbose_name="детали счёта")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")


    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"

    def __str__(self):
        return f"Счёт {self.payment_id}"
    

class Cart(models.Model):
    """Корзина"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")


    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Конзина {self.cart_id}"
    
class Product(models.Model):
    """Продукт"""
    name = models.CharField(max_length=50, verbose_name="имя товара")
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="корзина")
    description = models.TextField(verbose_name="описание товара")
    price = models.PositiveIntegerField(max_length=200, verbose_name="цена товара")


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"Конзина {self.product_id}"

class CartItem(models.Model):
    """Элемент Корзины"""
    name = models.CharField(max_length=200, verbose_name="имя товара")
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Пользователь")
    count = models.PositiveIntegerField(max_length=200, verbose_name="количество товаров")
    price = models.PositiveIntegerField(max_length=200, verbose_name="цена товара")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Пользователь")



    class Meta:
        verbose_name = "Элемент товара"
        verbose_name_plural = "Элементы товаров"

    def __str__(self):
        return f"Конзина {self.cart_item}"
    
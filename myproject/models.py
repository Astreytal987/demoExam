class Order(model.Model):
    """Заказ"""
    order_number = models.CharField(max_length)
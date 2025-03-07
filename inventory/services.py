from .models import Batch, WareVariant

def receive_stock(ware_variant, quantity, expiry_date, lot_number):
    batch = Batch.objects.create(
        variant=ware_variant,
        quantity=quantity,
        expiry_date=expiry_date,
        lot_number=lot_number,
    )

    ware_variant.stock += quantity
    ware_variant.save()

def adjust_stock(batch, new_quantity):
    difference = new_quantity - batch.quantity
    batch.quantity = new_quantity
    batch.save()

    ware_variant = batch.variant
    ware_variant.stock += difference
    ware_variant.save()
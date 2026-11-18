def hitung_total(harga, qty):
    subtotal =  harga * qty
    total = subtotal - (subtotal * 0.10)
    return total
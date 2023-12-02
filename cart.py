cart5 = {
  "id": 5,
  "userId": 3,
  "date": "2020-03-01T00:00:00.000Z",
  "products": [
    {
      "productId": 7,
      "quantity": 1
    },
    {
      "productId": 8,
      "quantity": 1
    }
  ],
  "__v": 0
}

print(cart5["products"])

for product in cart5["products"]:
    print(f"ProductId: {product['productId']}")
    print(f"Quantity: {product['quantity']} \n")
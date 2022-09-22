import csv
import json
import os
from typing import List

from shop.order import Order
from shop.order_element import OrderElement
from shop.product import ProductCategory, Product
from shop.store import AvailableProduct


def save_order(order: Order, file_name: str = "orders.json") -> None:
    new_order_data = {
        "client_first_name": order.client_first_name,
        "client_last_name": order.client_last_name,
        "order_elements": [
            {
                "product": {
                    "name": order_element.product.name,
                    "category": order_element.product.category.name,
                    "unit_price": order_element.product.unit_price,
                    "identifier": order_element.product.identifier,
                },
                "quantity": order_element.quantity
            } for order_element in order.order_elements
        ],
    }

    path_to_file = os.path.join("data", file_name)
    try:
        with open(path_to_file, mode="r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{order.client_first_name}-{order.client_last_name}"
    if client_id not in orders_by_clients_data:
        orders_by_clients_data[client_id] = []
    orders_by_clients_data[client_id].append(new_order_data)

    with open(path_to_file, mode="w") as orders_file:
        json.dump({"orders": orders_by_clients_data}, orders_file, indent=4)


def load_orders(client_first_name: str, client_last_name: str, file_name: str = "orders.json") -> List[Order]:
    path_to_file = os.path.join("data", file_name)
    try:
        with open(path_to_file, "r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{client_first_name}-{client_last_name}"
    if client_id not in orders_by_clients_data:
        return []
    orders = orders_by_clients_data[client_id]
    return [
        Order(
            client_first_name=order["client_first_name"],
            client_last_name=order["client_last_name"],
            order_elements=[OrderElement(
                quantity=order_element["quantity"],
                product=Product(
                    name=order_element["product"]["name"],
                    category=ProductCategory[order_element["product"]["category"]],
                    unit_price=order_element["product"]["unit_price"],
                    identifier=order_element["product"]["identifier"],
                )
            ) for order_element in order["order_elements"]],
        ) for order in orders
    ]


def load_store(file_name: str = "store.csv") -> List[AvailableProduct]:
    path_to_file = os.path.join("data", file_name)
    with open(path_to_file, newline="") as store_file:
        csv_reader = csv.DictReader(store_file)
        return [
            AvailableProduct(
                name=row["name"],
                category=ProductCategory[row["category"]],
                identifier=int(row["identifier"]),
                unit_price=float(row["unit_price"]),
                quantity=int(row["quantity"]),
            )
            for row in csv_reader
        ]


def save_store(available_products: List[AvailableProduct], file_name: str = "store.csv") -> None:
    path_to_file = os.path.join("data", file_name)
    with open(path_to_file, mode="w", newline="") as store_file:
        headers = ["name", "category", "unit_price", "identifier", "quantity"]
        csv_writer = csv.DictWriter(store_file, fieldnames=headers)
        csv_writer.writeheader()
        for available_product in available_products:
            product = available_product.product
            csv_writer.writerow(
                {
                    "name": product.name,
                    "category": product.category.name,
                    "unit_price": product.unit_price,
                    "identifier": product.identifier,
                    "quantity": available_product.quantity,
                }
            )

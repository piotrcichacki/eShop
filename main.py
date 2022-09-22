from shop import user_interface
from shop.persistance import load_store, save_store
from shop.store import Store


def run_example() -> None:
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    run_example()

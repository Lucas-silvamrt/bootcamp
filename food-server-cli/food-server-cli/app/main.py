import sys
from storage import load_data, save_data
from utils import is_expired, is_expiring_soon


def add_item(name, expiry):
    data = load_data()
    data.append({"name": name, "expiry": expiry})
    save_data(data)
    print("✅ Item adicionado!")


def list_items():
    data = load_data()
    if not data:
        print("📭 Nenhum item cadastrado.")
        return

    for item in data:
        print(f"{item['name']} - {item['expiry']}")


def list_expiring():
    data = load_data()
    found = False

    for item in data:
        if is_expiring_soon(item["expiry"]):
            print(f"⚠️ {item['name']} vence em breve ({item['expiry']})")
            found = True

    if not found:
        print("✅ Nenhum item vencendo em breve.")


def list_expired():
    data = load_data()
    found = False

    for item in data:
        if is_expired(item["expiry"]):
            print(f"❌ {item['name']} vencido em {item['expiry']}")
            found = True

    if not found:
        print("✅ Nenhum item vencido.")


def remove_item(name):
    data = load_data()
    new_data = [item for item in data if item["name"] != name]

    save_data(new_data)
    print("🗑️ Item removido!")


def help_menu():
    print("""
Comandos disponíveis:

add "nome" YYYY-MM-DD
list
expiring
expired
remove "nome"
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_menu()
        sys.exit()

    command = sys.argv[1]

    if command == "add":
        add_item(sys.argv[2], sys.argv[3])
    elif command == "list":
        list_items()
    elif command == "expiring":
        list_expiring()
    elif command == "expired":
        list_expired()
    elif command == "remove":
        remove_item(sys.argv[2])
    else:
        help_menu()
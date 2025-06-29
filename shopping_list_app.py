# Shopping List App 🛒 with colorama
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Liste dosyadan yükleniyor
if os.path.exists("shopping_list.txt"):
    with open("shopping_list.txt", 'r') as file:
        shopping_list = [line.strip() for line in file]
else:
    shopping_list = []

# Listeyi dosyaya kaydet
def save_list():
    with open("shopping_list.txt", 'w') as file:
        for item in shopping_list:
            file.write(item + "\n")

# Menü
def show_menu():
    print(Fore.CYAN + "\n--- Shopping List Menu 📝 ---")
    print(Fore.YELLOW + "1. View the shopping list 👀")
    print("2. Add items 🍱")
    print("3. Remove an item 🗑")
    print("4. Clear the list 🧹")
    print("5. Edit an item ✏️")
    print("6. Exit ❌")

# Listeyi göster
def view_list():
    print(Fore.BLUE + "\n🛍 Your Shopping List:")
    print(Fore.BLUE + "------------------------")
    time.sleep(1)
    if not shopping_list:
        print(Fore.LIGHTBLACK_EX + "📭 Your shopping list is empty.")
    else:
        for index, item in enumerate(shopping_list, 1):
            print(Fore.WHITE + f"{index}. {item}")

# Öğeleri ekle
def add_item():
    print(Fore.CYAN + "Enter items to add. When you're done, just press Enter on an empty line.")
    while True:
        item = input(Fore.WHITE + "Add item (or press Enter to finish): ").strip()
        if item == "":
            break
        shopping_list.append(item)
        print(Fore.GREEN + f"✅ '{item}' added.")
    save_list()
    print(Fore.MAGENTA + "All new items saved. Returning to menu.")
    time.sleep(1)

# Öğeyi sil
def remove_item():
    if not shopping_list:
        print(Fore.RED + "🛑 Your shopping list is empty. Nothing to remove.")
        time.sleep(1)
        return

    view_list()
    try:
        index_str = input(Fore.YELLOW + "Enter the number of the item to remove: ").strip()
        if not index_str.isdigit():
            print(Fore.RED + "⚠️ Please enter a valid number.")
            return

        index = int(index_str)

        if 1 <= index <= len(shopping_list):
            removed = shopping_list.pop(index - 1)
            save_list()
            print(Fore.RED + f"🗑 '{removed}' has been removed from the shopping list.")
        else:
            print(Fore.RED + "⚠️ Number out of range.")
    except Exception as e:
        print(Fore.RED + f"⚠️ Unexpected error: {e}")
    time.sleep(1)

# Tüm listeyi temizle
def clear_list():
    if not shopping_list:
        print(Fore.RED + "🛑 Your shopping list is already empty.")
        time.sleep(1)
        return

    confirm = input(Fore.YELLOW + "Are you sure you want to clear the entire list? (y/n): ").strip().lower()
    if confirm == 'y':
        shopping_list.clear()
        save_list()
        print(Fore.RED + "🧹 Cleared! Your shopping list is now empty.")
    else:
        print(Fore.LIGHTBLACK_EX + "❌ Clear operation cancelled.")
    time.sleep(1)

# Öğeyi düzenle
def edit_item():
    if not shopping_list:
        print(Fore.RED + "🛑 Your shopping list is empty. Nothing to edit.")
        time.sleep(1)
        return

    view_list()
    try:
        index = int(input(Fore.YELLOW + "Enter the number of the item to edit: "))
        if 1 <= index <= len(shopping_list):
            new_item = input(Fore.CYAN + "Enter the new name for the item: ").strip()
            if new_item:
                old_item = shopping_list[index - 1]
                shopping_list[index - 1] = new_item
                save_list()
                print(Fore.GREEN + f"✏️ '{old_item}' updated to '{new_item}'.")
            else:
                print(Fore.RED + "⚠️ Item name cannot be empty.")
        else:
            print(Fore.RED + "⚠️ Invalid item number.")
    except ValueError:
        print(Fore.RED + "⚠️ Please enter a valid number.")
    time.sleep(1)

# Ana döngü
while True:
    show_menu()
    choice = input(Fore.WHITE + "\n👩‍🍳👨‍🍳 Enter your choice (1-6): ").strip()
    time.sleep(1)

    if choice == '1':
        view_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        edit_item()
    elif choice == '6':
        print(Fore.MAGENTA + "\nExiting the program... ❌")
        time.sleep(2)
        print(Fore.GREEN + "Goodbye 👋 Happy Shopping!")
        break
    else:
        print(Fore.RED + "⚠️ Invalid choice. Please try again.")

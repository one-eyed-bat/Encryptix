import dearpygui.dearpygui as dpg

i = 1
items = []
def add_item(sender, app_data, user_data):
    global i, items
    item_name = dpg.get_value(user_data)
    if item_name == "":
       return 
    dpg.add_button(label=str(i)+'-' + item_name, parent='ItemList', callback=remove_item, user_data=item_name)
    i += 1
    items.append(item_name)
    dpg.set_value(user_data, '')
    print(f"{item_name} added")

def remove_item(sender, app_data):
    dpg.delete_item(sender)
def save_list():
    global items
    with open('list.txt', 'w') as f:
        for item in items:
            print(item)
            f.write("%s\n" % item)
            quit()
def load_list():
    global items
    try:
        print("trying to read file")
        with open('list.txt', 'r') as f:
            items = [line for line in f]
            for item in items:
                print(item)
                dpg.add_button(label=item, parent='ItemList', callback=remove_item, user_data=item)
    except FileNotFoundError:
        pass

dpg.create_context()
dpg.create_viewport(width=800, height=500)
dpg.setup_dearpygui()

with dpg.window(label="To Do List", width=800, height=500):
    dpg.add_text("Todo list")
    item_input = dpg.add_input_text(label="Item name")
    dpg.add_button(label="Add Item", callback=add_item, user_data = item_input)
    dpg.add_text("Click on an item to remove it")
    dpg.add_button(label="save and exit", callback=save_list)
    with dpg.child_window(id='ItemList', width=300, height=200):
        load_list()


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



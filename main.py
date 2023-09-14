from tkinter import *
stores = []
products = []
vendor_codes = []
editing_list = []
command = ''
name = ''
count = 0
much = 0.0
edit_command = []


def clear_func():
    temp = 123


def entry_del_p():
    vendor_code = command_ent.get()
    for i in products:
        print(i)
        if i[1] == vendor_code:
            products.remove(i)
    enter.configure(command=clear_func)


def entry_add_p():
    data = command_ent.get().split()
    name = data[0]
    artikule = data[1]
    if artikule not in vendor_codes:
        count = data[2]
        much = data[3]
        products.append([name, artikule, count, much])
        vendor_codes.append(artikule)
    else:
        output0.configure(text='Incorrect vendor code! This vendor code is using!')
    enter.configure(command=clear_func)


def add_product():
    enter.configure(command=entry_add_p)
    output0.configure(text='Print like this: name, vendor code, count, price.')


def delete_product():
    enter.configure(command=entry_del_p)
    output0.configure(text='Print like this: vendor code.')


def edit_product():
    enter.configure(command=entry_edt_p)
    output0.configure(text='Print like this: vendor code, command, value.')


def entry_edt_p():
    data = command_ent.get().split()
    vendor_code = data[0]
    change = data[1]
    change_value = data[2]
    if change == 'name' or change == 'Name':
        for i in products:
            if i[1] == vendor_code:
                i[0] = change_value
    elif change == 'count' or change == 'count':
        for i in products:
            if i[1] == vendor_code:
                i[2] = change_value
    elif change == 'price' or change == 'price':
        for i in products:
            if i[1] == vendor_code:
                i[3] = change_value
    enter.configure(command=clear_func)


def entry_add_s():
    data = command_ent.get().split()
    name = data[0]
    city = data[1]
    stores.append([name, city])
    enter.configure(command=clear_func)


def add_store():
    enter.configure(command=entry_add_s)
    output0.configure(text='Print like this: name, city.')


def entry_del_s():
    name = command_ent.get()
    for i in range(len(stores)):
        if stores[i][0] == name:
            stores.pop(i)
    enter.configure(command=clear_func)


def delete_store():
    enter.configure(command=entry_del_s)
    output0.configure(text='Print like this: name.')


def all_products():
    all_pr = ''
    for i in range(len(products)):
        all_pr += 'Name: ' + str(products[i][0]) + ' Vendor code: ' + str(products[i][1]) + ' Count: ' + str(products[i][2]) \
                  + ' Price: ' + str(products[i][3] + ' ')
    output0.configure(text=all_pr)
    enter.configure(command=clear_func)


def all_stores():
    all_pr = ''
    for i in range(len(stores)):
        all_pr += 'Name: ' + stores[i][0] + ' City: ' + stores[i][1]
    print(all_pr, type(all_pr))
    output0.configure(text=all_pr)
    enter.configure(command=clear_func)


window = Tk()


window.title('Pre-release build')
window.geometry('350x200')
add_p = Button(window, text='Add product', font=('Como Sans', 10), bg='white', fg='black', command=add_product)
add_p.grid(column=0, row=1)
del_p = Button(window, text='Delete product', font=('Como Sans', 10), bg='white', fg='black', command=delete_product)
del_p.grid(column=0, row=2)
edt_p = Button(window, text='Edit product', font=('Como Sans', 10), bg='white', fg='black', command=edit_product)
edt_p.grid(column=0, row=3)
add_s = Button(window, text='Add store', font=('Como Sans', 10), bg='white', fg='black', command=add_store)
add_s.grid(column=1, row=1)
del_s = Button(window, text='Delete store', font=('Como Sans', 10), bg='white', fg='black', command=delete_store)
del_s.grid(column=1, row=2)
space = Label(text='-----------------------')
space.grid(column=0, row=4)
space_1 = Label(text='-------------------------')
space_1.grid(column=1, row=4)
all_p = Button(window, text='Print all products', font=('Como Sans', 10), bg='white', fg='black', command=all_products)
all_p.grid(column=0, row=5)
all_s = Button(window, text='Print all stores', font=('Como Sans', 10), bg='white', fg='black', command=all_stores)
all_s.grid(column=1, row=5)
output0 = Label(window, text='<output>', font=('Como Sans', 10))
output0.grid(column=1, row=6)
command_ent = Entry(window, width=30)
command_ent.grid(column=0, row=6)
enter = Button(window, text='Enter', font=('Como Sans', 10), bg='white', fg='black', command=entry_add_p)
enter.grid(column=0, row=7)

window.mainloop()

contacts = {}
def add_contact(contacts,name,phone,email):
    contacts[name] = {
        'phone': phone,
        'email': email
    }
#   return contacts
# add_contact(contacts,'Jack','1234567890','shbh')
# add_contact(contacts,'Rose','0987654321','hjsbhd')
# print(contacts)

def find_contact(contacts,name):
    if name in contacts:
        return contacts[name]
    return '未找到该联系人'

# print(find_contact(contacts,'Jack'))
# print(find_contact(contacts,'Tom'))

def delete_contact(contacts,name):
    if name in contacts:
        del contacts[name]
        return'删除成功!'
    else:
        return '未找到该联系人'

# print(delete_contact(contacts,'Jack'))
# print(contacts)
# print(delete_contact(contacts,'Tom'))

def update_contact(contacts, name, phone=None, email=None):
    if name in contacts:
        if phone is not None:
            contacts[name]['phone'] = phone
        if email is not None:
            contacts[name]['email'] = email
        return'修改成功！'
    return'未找到该联系人'

# print(update_contact(contacts,'Rose',phone='77777'))
# print(contacts)
# print(update_contact(contacts,'Rose',email='6666@12345'))
# print(contacts)
# print(update_contact(contacts,'Rose',phone='77777',email='qwed@13244'))
# print(contacts)

def show_contacts(contacts):
    if not contacts:
        print('暂无联系人')
        return
    else:
        for name,info in contacts.items():
            phone = info['phone']
            email = info['email']
            print(f"姓名:{name} 手机号：{phone} 邮箱：{email}")
            

while True:
    print('通讯录')
    print('1.添加联系人')
    print('2.查找联系人')
    print('3.删除联系人')
    print('4.修改联系人')
    print('5.显示所有联系人')
    print('0.退出')

    choice = input('请输入操作编号：')

    if choice == '1':
        name = input('姓名：')
        phone = input('手机号：')
        email = input('邮箱：')

        add_contact(contacts,name,phone,email)
        print('添加成功！')

    elif choice == '2':
        name = input('请输入要查找的名字：')
        result = find_contact(contacts,name)
        print(result)

    elif choice == '3':
        name = input('请输入要删除的名字：')
        result = delete_contact(contacts,name)
        print(result)

    elif choice == '4':
        name = input('请输入要修改的联系人姓名：')
        if name in contacts:
            phone = input('请输入新的手机号,如果不需要直接按Enter:')
            email = input('请输入新的邮箱,如果不需要直接按Enter:')
            if phone == '':
                phone = None
            if email == '':
                email = None
            result = update_contact(contacts,name,phone=phone,email=email)
            print(result)
        else:
            print('未找到该联系人')

    elif choice == '5':
        show_contacts(contacts)

    elif choice == '0':
        print('退出通讯录')
        break
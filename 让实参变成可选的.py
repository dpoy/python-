def get_formatted_name(firs_name, last_name, middle_name=""):
    """得到简洁的姓名"""
    if middle_name:
        full_name = firs_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = firs_name + last_name
    return full_name.title()

muaician = get_formatted_name('jimi', 'hend')
print(muaician)

muaician = get_formatted_name('jimi', 'ss', 'hend')
print(muaician)

def format_name(f_name, l_name):
    """ Take a first and a last name and format
    it to return the title case version of the
    name"""
    name = f_name.title()
    name2 = l_name.title()
    
    return f"{name} {name2}"

full_name = format_name("angela", "YU")

print(full_name)
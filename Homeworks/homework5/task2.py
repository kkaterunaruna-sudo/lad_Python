product_categories = ["smartphones", "computers", "laptops", "gadgets", "computers components", "home appliances","tv", "Cameras"]
filtration = [n for  n in product_categories  if len(product_categories) > 5]
print(f"Строки длиннее 5 символов {filtration}")
string_length = [len(n) for  n in product_categories]
print(f"Список из длин всех строк {string_length}")
title = [n.capitalize()  for  n in product_categories]
print(f"Список строк с первой буквой в верхнем регистре  {title}")



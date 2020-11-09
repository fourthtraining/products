#記帳程式
products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	#------以下方式也可以-----
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	#------------------------
	#------以下方式是簡寫-----
	#p = [name, price]
	#products.append(p)
	#------------------------
	#------更可以再簡寫-------
	products.append([name,price])
print(products)
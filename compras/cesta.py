


from produtos import Produto
class Cesta:
    produtos = []
    total = 0
    
    def main():
        p1 = Produto("jantinha",20)
        p2 = Produto("Bebida",20.0)
        p3 = Produto("Sobremesa",20.0)
        c = Cesta
        c.produtos.append(p1)
        c.produtos.append(p2)
        c.produtos.append(p3)

        for item in c.produtos:
            print(item.nome)
        
    main()
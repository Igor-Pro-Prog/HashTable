#tabela hash com tratamento de colisões por encadeamento externo
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #substituir
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #substituir

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                        not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
    
    def __len__(self):
        return len(self.slots)

    def __contains__(self, key):
        return self.get(key) != None

    def __delitem__(self, key):
        self.put(key, None)
#faz um menu para o usuário escolher o que fazer
def menu():
    print('1 - Inserir')
    print('2 - Buscar')
    print('3 - Remover')
    print('4 - Imprimir')
    print('5 - Sair')
    return int(input('Escolha uma opção: '))
#cria a tabela hash
tabela = HashTable(11)
#loop para o menu
while True:
    opcao = menu()
    if opcao == 1:
        chave = int(input('Digite a chave: '))
        valor = input('Digite o valor: ')
        tabela[chave] = valor
    elif opcao == 2:
        chave = int(input('Digite a chave: '))
        print(tabela[chave])
    elif opcao == 3:
        chave = int(input('Digite a chave: '))
        del tabela[chave]
    elif opcao == 4:
        print(tabela.slots)
        print(tabela.data)
    elif opcao == 5:
        break
    else:
        print('Opção inválida')

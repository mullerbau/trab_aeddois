class HashTable:
    def __init__(self, size=37):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0
    
    def _hash(self, key):
        # converte para string e maiuscula
        key = str(key).upper()
        hash_value = 0
        
        # calcula hash usando ASCII e potencias de 2
        for i, char in enumerate(key):
            ascii_val = ord(char)
            peso = 2 ** i  # 1, 2, 4, 8, 16...
            hash_value += ascii_val * peso
        
        return hash_value % self.size
    
    def insert(self, key, value):
        # insere item na tabela
        posicao = self._hash(key)
        bucket = self.table[posicao]
        
        # verifica se ja existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # nova insercao
        if len(bucket) > 0:
            self.collisions += 1
        
        bucket.append((key, value))
    
    def search(self, key):
        # busca item na tabela
        posicao = self._hash(key)
        bucket = self.table[posicao]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    

    def mostrar_tabela(self):
        # mostra a tabela completa
        print(f"\nTabela Hash (tamanho {self.size}):")
        for i, bucket in enumerate(self.table):
            if bucket:
                nomes = [key for key, _ in bucket]
                print(f"  [{i:2d}] {nomes}")
    
    def testar(self):
        # testa com os nomes obrigatorios
        nomes = [
            "João", "João Silva", "Ana Clara", "Ana Cláudia", "Andressa", "André",
            "Roberta", "Roberto", "Carla", "Karl", "Marcos", "Marcus", 
            "Pablo", "Pabllo", "Maria", "Mário", "José", "Josué",
            "Pedro", "Petra", "Lucas", "Lúcia", "Rafael", "Rafaela"
        ]
        
        print("Inserindo nomes na tabela hash:")
        print(f"{'Nome':<12} {'Hash':<8} {'Indice':<6}")
        print("-" * 30)
        
        for nome in nomes:
            hash_val = 0
            key = str(nome).upper()
            for i, char in enumerate(key):
                if char.isalpha():
                    hash_val += ord(char) * (2 ** i)
            
            indice = self._hash(nome)
            self.insert(nome, nome)
            print(f"{nome:<12} {hash_val:<8} {indice:<6}")
        
        print(f"\nResultados:")
        print(f"Total de nomes: {len(nomes)}")
        print(f"Colisoes: {self.collisions}")
        print(f"Taxa de ocupacao: {len(nomes)/self.size:.2f}")
        
        # mostra distribuicao
        distribuicao = [len(bucket) for bucket in self.table]
        ocupados = sum(1 for x in distribuicao if x > 0)
        print(f"Posicoes ocupadas: {ocupados}/{self.size}")
        
        self.mostrar_tabela()


# teste
if __name__ == "__main__":
    ht = HashTable()
    ht.testar()
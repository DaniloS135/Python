class Televisor:
    def __init__(self, Volume=20, Canal_Atual=None, Lista_Canais=[]):
        self.Canal_Atual=Canal_Atual
        self.Volume=Volume
        self.Lista_Canais = Lista_Canais
        
    def aumentavolume(self, valor):
        self.Volume += valor
        
    def diminuivolume (self, valor):
        self.Volume -= valor
        
    def mutevolume (self):
        self.Volume = 0
    
    def returnvolume (self, valor):
        self.Volume = valor
    
    def trocadeCanal (self, canal):
        if canal in self.Lista_Canais:
            self.Canal_Atual = canal
            
    def sintonizarcanal (self, canal):
        if canal not in self.Lista_Canais:
            self.Lista_Canais.append(canal)
    

tv = Televisor()
tv.aumentavolume(5)
print(tv.Volume)

tv.diminuivolume(6)
print(tv.Volume)

tv.mutevolume()
print(tv.Volume)

tv.returnvolume(5)
print(tv.Volume)

#adicionando canais
tv.sintonizarcanal('Globo')
tv.sintonizarcanal('SBT')
tv.sintonizarcanal('Record')
tv.sintonizarcanal('Band')

#Mostrando lista de canais
print("Mostrando canais disponiveis", tv.Lista_Canais)

#trocando para um canal existente
tv.trocadeCanal('SBT')
print('Canal atual', tv.Canal_Atual)

#Tentando trocar para um canal que não foi sintonizado
tv.trocadeCanal('CNN')
print('Canal Atual (após tentativa invalida)')


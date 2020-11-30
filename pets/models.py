from users.models import User
from django.db import models

PET_SIZES = [('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')]
PET_SEX = [('M', 'Macho'), ('F', 'Fêmea')]

# PET TYPE
GATO = 'Gato' 
CACHORRO = 'Cachorro' 
PASSARO = 'Pássaro' 
ROEDOR = 'Roedor' 
OUTRO = 'Outro'

# DEFAULT
DE00 = 'Sem raça definida' 
DE01 = 'Outra'

# CAT BREED
CB00 = 'Abssínios'                  
CB01 = 'Alemão de pelo comprido'
CB02 = 'American Curl'              
CB03 = 'American Shorthair'         
CB04 = 'American Wirehair'          
CB05 = 'Azul Russo'                 
CB06 = 'Balineses'                  
CB07 = 'Bengalês'                   
CB08 = 'Bobtail'                    
CB09 = 'Bobtail Japonês'            
CB10 = 'Bombay'                     
CB11 = 'British Shorthair'          
CB12 = 'Burmês'                     
CB13 = 'Burmilla'                   
CB14 = 'Califórinia Spangled'       
CB15 = 'Chartreux'                  
CB16 = 'Cornish Rex'                
CB17 = 'Cymric'                     
CB18 = 'Devon Rex'                  
CB19 = 'Exóticos'                   
CB20 = 'Foldex'                     
CB21 = 'German Rex'                 
CB22 = 'Habana'                     
CB23 = 'High Land Fold'             
CB24 = 'Himalaios'                  
CB25 = 'Javaneses'                  
CB26 = 'Khao Manee'                 
CB27 = 'Korat'                      
CB28 = 'Maine Coon'                 
CB29 = 'Manx'                       
CB30 = 'Mau Egípcio'                
CB31 = 'Munch Kin'                  
CB32 = 'Ragdoll'                    
CB33 = 'Pixie Bob'                  
CB34 = 'Ragamuffin'                 
CB35 = 'Ragdoll'                           

# DOG BREED
DB00 = 'Akita'
DB01 = 'Basset hound'	
DB02 = 'Beagle'		
DB03 = 'Boiadeiro australiano'
DB04 = 'Border collie'	
DB05 = 'Boston terrier'	
DB06 = 'Boxer'	
DB07 = 'Buldogue'		
DB08 = 'Bull terrier'
DB09 = 'Chihuahua'	
DB10 = 'Chow chow'			
DB11 = 'Dálmata'	
DB12 = 'Doberman'	
DB13 = 'Dogo argentino'	
DB14 = 'Dogue alemão'	
DB15 = 'Fila brasileiro'	
DB16 = 'Golden retriever'	
DB17 = 'Husky siberiano'
DB18 = 'Jack russell terrier'
DB19 = 'Labrador'
DB20 = 'Lhasa apso'
DB21 = 'Lulu da pomerânia'
DB22 = 'Maltês'
DB23 = 'Pastor alemão'
DB24 = 'Pastor australianoPastor de Shetland'	
DB25 = 'Pequinês'
DB26 = 'Pinscher'	
DB27 = 'Pit bull'	
DB28 = 'Poodle'	
DB29 = 'Pug'	
DB30 = 'Rottweiler'
DB31 = 'Shar-pei'	
DB32 = 'Shiba'	
DB33 = 'Shih tzu'
DB34 = 'Weimaraner'		
DB35 = 'Yorkshire'

# BIRD BREED
BB00 = 'Agapornis'
BB01 = 'Araponga'
BB02 = 'Arara'
BB03 = 'Azulão'
BB04 = 'Bavete'
BB05 = 'Bicudo'
BB06 = 'Cabloquinho'
BB07 = 'Cacatua'
BB08 = 'Calafete'
BB09 = 'Calopsita'
BB10 = 'Canário'
BB11 = 'Cardeal'
BB12 = 'Coleiro'
BB13 = 'Cordonbleu'
BB14 = 'Coruja'
BB15 = 'Curió'
BB16 = 'Diamante Mandarin'
BB17 = 'Dominó'
BB18 = 'Explêndido'
BB19 = 'Granatina'
BB20 = 'Jandaia'
BB21 = 'Lóris'
BB22 = 'Mainá'
BB23 = 'Modesto'
BB24 = 'Papagaio'
BB25 = 'Pássaro Preto'
BB26 = 'Patativa'
BB27 = 'Perequito Autraliano'
BB28 = 'Pica-pau'
BB29 = 'Pintassilgo'
BB30 = 'Pombo'
BB31 = 'Rolinha'
BB32 = 'Rouxinol'
BB33 = 'Sabiá Laranjeira'
BB34 = 'Tangará'
BB35 = 'Tico-tico'
BB36 = 'Tucano'

# RODENT BREED
RB00 = 'Camundongo'
RB01 = 'Chinchila'
RB02 = 'Gerbil - Esquilo da MOngólia'
RB03 = 'Hamster Anão Russo'
RB04 = 'Hamster Sírio'
RB05 = 'Mecol - Twister'
RB06 = 'Porquinho da índia'
RB07 = 'Topolino'

TYPE_CHOICES = [(GATO, GATO), (CACHORRO, CACHORRO), (PASSARO, PASSARO), (ROEDOR, ROEDOR), (OUTRO, OUTRO),]

BREED_CHOICES = [
    (DE00, DE00), (DE01, DE01), 
    
    (CB00, CB00), (CB01, CB01), (CB02, CB02), (CB03, CB03), (CB04, CB04), (CB05, CB05), 
    (CB06, CB06), (CB07, CB07), (CB08, CB08), (CB09, CB09), (CB10, CB10), (CB11, CB11), 
    (CB12, CB12), (CB13, CB13), (CB14, CB14), (CB15, CB15), (CB16, CB16), (CB17, CB17),
    (CB18, CB18), (CB19, CB19), (CB20, CB20), (CB21, CB21), (CB22, CB22), (CB23, CB23), 
    (CB24, CB24), (CB25, CB25), (CB26, CB26), (CB27, CB27), (CB28, CB28), (CB29, CB29),
    (CB30, CB30), (CB31, CB31), (CB32, CB32), (CB33, CB33), (CB34, CB34), (CB35, CB35),

    (DB00, DB00), (DB01, DB01), (DB02, DB02), (DB03, DB03), (DB04, DB04), (DB05, DB05), 
    (DB06, DB06), (DB07, DB07), (DB08, DB08), (DB09, DB09), (DB10, DB10), (DB11, DB11), 
    (DB12, DB12), (DB13, DB13), (DB14, DB14), (DB15, DB15), (DB16, DB16), (DB17, DB17), 
    (DB18, DB18), (DB19, DB19), (DB20, DB20), (DB21, DB21), (DB22, DB22), (DB23, DB23), 
    (DB24, DB24), (DB25, DB25), (DB26, DB26), (DB27, DB27), (DB28, DB28), (DB29, DB29), 
    (DB30, DB30), (DB31, DB31), (DB32, DB32), (DB33, DB33), (DB34, DB34), (DB35, DB35),

    (BB00, BB00), (BB01, BB01), (BB02, BB02), (BB03, BB03), (BB04, BB04), (BB05, BB05), 
    (BB06, BB06), (BB07, BB07), (BB08, BB08), (BB09, BB09), (BB10, BB10), (BB11, BB11), 
    (BB12, BB12), (BB13, BB13), (BB14, BB14), (BB15, BB15), (BB16, BB16), (BB17, BB17), 
    (BB18, BB18), (BB19, BB19), (BB20, BB20), (BB21, BB21), (BB22, BB22), (BB23, BB23), 
    (BB24, BB24), (BB25, BB25), (BB26, BB26), (BB27, BB27), (BB28, BB28), (BB29, BB29), 
    (BB30, BB30), (BB31, BB31), (BB32, BB32), (BB33, BB33), (BB34, BB34), (BB35, BB35),

    (RB00, RB00), (RB01, RB01), (RB02, RB02), (RB03, RB03), (RB04, RB04), (RB05, RB05), 
    (RB06, RB06), (RB07, RB07),
]

def get_cat_breeds():
    catBreeds = [
        DE00, DE01,

        CB00, CB01, CB02, CB03, CB04, CB05, CB06, CB07, CB08, CB09, CB10, CB11,
        CB12, CB13, CB14, CB15, CB16, CB17, CB18, CB19, CB20, CB21, CB22, CB23,
        CB24, CB25, CB26, CB27, CB28, CB29, CB30, CB31, CB32, CB33, CB34, CB35,
    ]

    return catBreeds

def get_dog_breeds():
    dogBreeds = [
        DE00, DE01,

        DB00, DB01, DB02, DB03, DB04, DB05, DB06, DB07, DB08, DB09, DB10, DB11, 
        DB12, DB13, DB14, DB15, DB16, DB17, DB18, DB19, DB20, DB21, DB22, DB23, 
        DB24, DB25, DB26, DB27, DB28, DB29, DB30, DB31, DB32, DB33, DB34, DB35,
    ]

    return dogBreeds

def get_bird_breeds():
    birdBreeds = [
        DE00, DE01,

        BB00, BB01, BB02, BB03, BB04, BB05, BB06, BB07, BB08, BB09, BB10, BB11, 
        BB12, BB13, BB14, BB15, BB16, BB17, BB18, BB19, BB20, BB21, BB22, BB23, 
        BB24, BB25, BB26, BB27, BB28, BB29, BB30, BB31, BB32, BB33, BB34, BB35,
    ]

    return birdBreeds

def get_rodent_breeds():
    rodentBreeds = [
        DE00, DE01,

        RB00, RB01, RB02, RB03, RB04, RB05, RB06, RB07, 
    ]

    return rodentBreeds

def get_other_breeds():
    otherBreed = [DE01,]

    return otherBreed

class Pet(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_image', blank=False, null=False) 
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    size = models.CharField(max_length=1, choices=PET_SIZES, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=PET_SEX, blank=False, null=False)
    vaccinated = models.BooleanField(default=False)
    castrated = models.BooleanField(default=False)
    dewormed = models.BooleanField(default=False)
    vulnerable = models.BooleanField(default=False)
    isAdopted = models.BooleanField(default=False)
    pet_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)
## Struktura adresu IP

```192.168.100.192```
```255.255.255.0```




### Jak policzyć?
#### Adres sieci

1. Rozpisz adres IP oraz maskę podsieci na zapis binarny  

```192.168.100.192 = 11000000.10101000.01100100.11000000```  
```255.255.255.0  =  11111111.11111111.11111111.00000000```

2. Wykonaj na pozyższych oktetach operację binarną AND
3. ???
4. Przekonwertuj spowrotem na dziesiętny

#### Adres rozgłoszeniowy

1. Weź binarny adress sieci oraz binarną maskę podsieci 
2. Zaneguj binarnie podsieci (NOT)
3. Wykonaj operację binarną OR
4. Przekonwertuj spowrotem na system dziesiętny


## Podział na równą ilość podsieci

```2^S >= n```

Chcemy 7 -> 2^3 >= 7

Maska -> 255.255.255.11100000 -> 255.255.255.224 -> /27


## Wprowadzenie

| dziesiętnie |  binarnie   | 
| ----------- | -----------  |
| ``10``  | ``00001010``| 
| ``92``  | ``01011100``| 
| ``37``  | ``00100101``| 
| ``240`` | ``11110000``| 
| ``192`` | ``11000000``| 
| ``255`` | ``11111111``| 
| ``128`` | ``10000000``| 
| ``168`` | ``10101000``| 

## 

| binarnie |  dziesiętnie   | 
| ----------- | -----------  |
| ``00100000``  |  ``32``| 
| ``11111000``  | ``248``| 
| ``10100000``  | ``160``| 
| ``00110000`` | ``48``| 
| ``10101100`` | ``172``| 
| ``01000000`` | ``64``| 
| ``11111100`` | ``252``| 
| ``01100010`` | ``98``| 
 
## Notacja CIDR
##  
| maska |  /(X) x - liczba bitów   | 
| ----------- | -----------  |
| ``255.255.255.0``   | ``/24`` | 
| ``255.128.0.0``     | ``/9``| 
| ``255.255.252.0``   | ``/22``| 
| ``255.255.254.0``   | ``/23``| 
| ``255.255.255.240`` | ``/28``| 
| ``255.240.0.0``     | ``/12``| 
## 

| CIDR |  Maska   | 
| ----------- | -----------  |
| ``/8``    | ``255.0.0.0.0``| 
| ``/20``   | ``255.255.240.0``| 
| ``/30``   | ``255.2555.255.192``| 
| ``/16``   | ``255.255.0.0``| 
| ``/27``   | ``255.255.255.224``| 
| ``/11``   | ``255.224.0.0``| 


## Liczba hostów
## 
| sieć |  liczba   | 
| ----------- | -----------  |
| ``10.0.0.0/8``    | ``liczba zer w masce = 24, hostów = 2^24-2 = 16777214`` | 
| ``172.16.0.0/16``   | `` liczba zer w masce = 16 , hostów 2^16-2 = 65534``| 
| ``192.168.1.0/24``   | ``liczba zer w masce = 8, hostów = 2^8-2=254``| 
| ``192.168.1.0/27``   | ``liczba zer w masce = 5, hostów = 2^5-2=30``| 
| ``192.168.1.0/29``   | ``liczba zer w masce = 3, hostów = 2^3-2=6``| 
| ``192.168.1.0/31``   | ``liczba zer w masce = 1, hostów = 2^1-2=0``| 

* liczba 0 w masce?


## Parametry na podstawie adresu

Mając dany adres hosta i maskę znajdź:
  * adres sieci
  * początkowy adres hosta w sieci
  * liczbę hostów w zadanej podsieci ```2^(32 bity - bity maski maska) - 2 (siec i broadcast)```
  * końcowy zakres adresu hosta w sieci
  * adres rozgłoszeniowy
##   ## 

| Parametr |  wartość   | 
| ----------- | -----------  |
| ``ip``    | ``192.168.1.145``| 
| ``maska``   | ``255.255.255.128`` | 
| ``adres sieci``   | ``192.168.1.128``|
| ``liczba hostów``   | ``2^7-2=126``|
| ``host - min``   | ``192.168.1.129``| 
| ``host - max``   | ``192.168.1.254``| 
| ``broadcast``   | ``192.168.1.255``| 
 
## Zadanie

0. Znajdz wszystkie parametry sieci dla hosta o adresie 172.16.128.64 / 16
##   
| Parametr |  wartość   | 
| ----------- | -----------  |
| ``ip``    | ``172.16.128.64``| 
| ``maska``   | ``255.255.0.0`` | 
| ``adres sieci``   | ``172.16.0.0``|
| ``liczba hostów``   | ``2^16-2=65534``|
| ``host - min``   | ``172.16.0.1``| 
| ``host - max``   | ``172.16.255.254``| 
| ``broadcast``   | ``172.16.255.255``| 

1.
  * Podziel sieć ```192.168.1.0/16``` na 16 równych podsieci
##   
| Adres sieci |  zakres hostów   | Adres Rozgłoszeniowy |
| ----------- | -----------  | ----------- |
| ``192.168.1.0``    | | |
| ``192.168.``   | | |
| ````   | | |
| ````   | | |
| ````   | | |
| ````   | | |

2. 
  * Podziel sieć ``172.16.0.0/16`` na 6 równych podsieci.

3. 
  * Podziel sieć ``192.168.1.0/24``, tak aby każda podsieć miała 11 użytkowników.

4. 
  * Podziel sieć ``10.0.0.0/8`` na 5 podsieci. 
    * Podsieć A ma posiadać 100 000 użytkowników,
    * B – 10 000 użytkowników
    * C – 3 000 użytkowników
    * D – 500 użytkowników
    * E – 2 użytkowników.
    
## Wizualizacja

![krakow siec akademicka](cracow-core.jpeg)


## Materiały

    * http://www.cyfronet.krakow.pl/sieci/13152,artykul,charakterystyka_sieci.html
    * https://www.computerworld.pl/news/Sieci-szkieletowe-polskich-operatorow,394360.html
    * https://cidr.xyz/

    * Lista polskich puli adresów
    * http://42.pl/pl/networks.html?html=1

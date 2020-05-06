## Ustawianie parametrów sieci

### Zadania

0. Z wykorzystaniem dowolnych systemów operacyjnych na których potrafisz uruchomić interpreter ``python`` oraz oprogramowania virtualbox odwzoruj poniższy schemat sieci:

![alt text][network]

[network]: ./network.png "Logo Title Text 2"

1. na 1 z komputerów zainstaluj i uruchom program ``server.py`` dostępne pod adresem ``https://github.com/jkanclerz/client-server-chat``
2. na 2 z komputerów zainstaluj i uruchom program ``client.py`` dostępne pod adresem ``https://github.com/jkanclerz/client-server-chat``
3. Manipulując konfiguracją sieci na poziomie virtualbox, uruchom serwer czatu, oraz udostępnij go na wybranym porcie oraz adresie tak aby istniała możliwość połączenia przez inne osoby w obrębie pracowni
4. Zainstaluj oprogramowanie serwera HTTP ``nginx`` lub innego, skonfiguruj plik index.html wg instrukcji, sprawdź dostępność strony z wykorzystaniem dowolnego klienta protokołu ``HTTP`` z różnych konfiguracji IP
5. Posługując się programami tj: ``netstat`` lub ``lsof`` sprawdź na jakich portach zostały uruchomione serwery czatu czy HTTP

Wejściowe parametry sieci
-------------------------
| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
|   PC 1 |  
| IP - address  | 10.0.15.4 | |
| MASKA  | /24 (255.255.255.0) | |
|   |  | |
| PC 2  |  | |
| IP - address  | 10.0.15.6 | |
| MASKA  | /24 (255.255.255.0 )| |

Weryfikacja połączenia

Polecenie
ping 10.0.15.4

pc1:
python3 server.py
pc2:
python3 client.py 10.0.15.4 9999

Efekt
Pakiety zostają wysłane oraz wracają.
Na pc1 na porcie 9999 zostaje otworzony serwer.
Pc2 łaczy sie z serwerem na pc1.

Statyczna konfiguracja parametrów połączenia
Wejściowe parametry sieci
-------------------------
| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
|   PC 1 |  
| IP - address  | 192.168.10.10 | |
| MASKA  | 255.255.255.0 | |
|   |  | |
| PC 2  |  | |
| IP - address  | 192.168.10.11 | |
| MASKA  | 255.255.128.0 | |
| PC 2  |  | |
| IP - address  | 172.16.100.100 | |
| MASKA  | 255.255.0.0 | |

Weryfikacja połączenia


Polecenie
PC1:
ping 192.168.10.11
ping 172.16.100.100
PC2:
ping 192.168.10.10
ping 172.16.100.100
PC3:
ping 192.168.10.10
ping 192.168.10.11

Efekt
Brak efektu

Nowa statyczna konfiguracja 

-------------------------
| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
|   PC 1 |  
| IP - address  | 192.168.10.10 | pozostaje taki sam |
| MASKA  | 255.255.255.0  | pozostaje taki sam|
|   |  | |
| PC 2  |  | |
| IP - address  | 192.168.10.11 |taki sam jak w wersji 1 |
| MASKA  | 255.255.255.0 |maska 24 bitowa pasujaca do adresacji sieci |

Weryfikacja połączenia

Polecenie
PC1:
ping 192.168.10.11
PC2:
ping 192.168.10.10

Efekt
Pakiety wylatują i wracają.

### Utrwalenie konfiguracji

Dlaczego? Jak? Co? :)
Ogolnie to ifconfig fajna komenda, ogarnąłem że można wszystko na raz wpisac
np. ifconfig eth0 192.168.1.1 netmask 255.255.255.0


### Warto wiedzieć

-------------------------
| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
| Lokalizacja pliku z konfiguracją sieci| /etc/resolv.conf| |
| UP -> Wyłączenie interfejsu sieciowego| False | Up jest flaga, która włacza interfejs |
| DOWN -> Włączenie interfejsu sieciowego| False | down jest flaga która wyłacza sterownik interfejsu|
| Sprawdzenie obecnych parametrów | ifconfig | |
| lista wszystkich interfejsów | ifconfig -a| |
| Które interfejsy jakie porty słuchają | netstat -a | |


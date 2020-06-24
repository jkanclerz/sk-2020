# Zadanie 1

Organizacja planuje rozpoczęcie działalności w 3 budynkach, w każdym z nich przewiduje do 1000 urządzeń IP

1. Zaprojektuj oraz udokumentuj prototyp rozwiązania z wykorzystaniem oprogramowania ``CISCO Packet Tracer``, ``VirtualBox`` lub podobnego. 

## Schemat

![zadanie 1](stage-01.svg)

## Zawartość

 * Adresy poszczególnych sieci IP
 * Adresację linków pomiędzy routerami
 * Tablice routingów na poszczególnych routerach
 


| Sieć  | Adres Sieci | Host min     | Host max      | Adres rozgłoszeniowy |
| -------------     |:-------------: | -----:       | -----:        | -----:    |
| 1         | 10.0.0.0/22 | 10.0.0.1 | 10.0.3.254 | 10.0.3.255 
| 2         | 10.1.0.0/22 | 10.1.0.1| 10.1.3.254 | |  10.1.3.255
| 3         | 10.2.0.0/22 | 10.2.0.1| 10.2.3.254 | |  10.2.3.255
| 4 (Routing) | 192.168.1.0/30 | 192.168.1.1 | 192.168.1.2 | 192.168.1.3 |
| 5 (Routing) | 192.168.2.0/30 | 192.168.2.1 | 192.168.w.2 | 192.168.2.3 |
| 6 (Routing) | 192.168.3.0/30 | 192.168.3.1 | 192.168.3.2 | 192.168.3.3 |

| Router | Interface | Ip | 
| ------------- | -------------  |:-------------:|
| Router 1 | Serial 0/3/0 |   192.168.1.1/30 | 
| Router 1 | Serial 0/3/1  |   192.168.3.2/30 | 
| Router 1 | FastEthernet 0/0  |  10.0.0.1/22 | 

| Router | Interface | Ip | 
| ------------- | -------------  |:-------------:|
|  Router 2 |  Serial 0/3/0 | Serial 0/3/0  |  192.168.2.1 | 
|  Router 2 | Serial 0/3/1  |  192.168.1.2/30 | 
|  Router 2 | FastEthernet 0/0  |  10.1.0.1/22 | 

| Router | Interface | Ip | 
| ------------- | -------------  |:-------------:|
|  Router 3 | Serial 0/3/0 |  192.168.3.1/30 | 
|  Router 3 |Serial 0/3/1  |  192.168.2.2/30 | 
|  Router 3 | FastEthernet 0/0  |  10.2.0.1/22 | 

Routery Cisco 2811 zostały wyposażone w moduł WIC-2T, który pozwala na komunikację routerów przez port szeregowy  
Interfejsy WIC-2T zostały połączone ze sobą kablem Serial DCE, tak aby każdy router miał jeden interfejs aktywny (każdy interfejs z Serial 0 jest z ustalonym clockiem) oraz pasywny  
Każdy interface routera był konfigurowany za pomocą Cisco CLI, a dokładnie komendami:  

```> enable``` -- wejście w tryb uprzywilejowany  
```# config terminal``` -- wejście w tryb konfiguracji  
```(config)# interface Serial X/X/X``` -- konfiguracja interfejsu  
```(config-if)# ip address <ip <maska>``` -- nadanie adresu IP  
```(config-if)# clock rate 64000``` -- ustalenie częstotliwości zegara DCE (Tylko dla stron z clockiem)  
```(config-if)# no shutdown``` -- włączenie interfejsu  
```# copy running-config startup-config``` -- ważna komenda zapisująca obecne ustawienia do ustawień ogólnych  

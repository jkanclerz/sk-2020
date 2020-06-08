# Podział i agregacja sieci

Dysponująć siecią o adresie ``192.168.100.0/24`` dokonaj podziału podsieci z uwzględnieniem licznosci hostów

| podsieć | liczba hostów |
| ------------- |:-------------:|
| 1 | 64 |
| 2 | 16 |
| 3 | 1  |

-------------------------------

| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
| Adres sieci do podziału |  192.168.100.0 | |
| Maska sieci  |  /24 | |
| Maska binarnie  |  11111111.11111111.11111111.00000000 | |


2^(32 - dlugość maski) - 2 >= wymagana ilosć hostów

2^(32-26) - 2 = 62 za mało
2^(32-25) - 2 = 126 >= OK

2^(32-28) -2 = 14 za mało
2^(32-27) -2 = 30 >= 16 OK

| Podsiec   | Adres podsieci | Host min     | Host max      | Adres rozgłoszeniowy |
| -------------     |:-------------: | -----:       | -----:        | -----:    |
| 1         | 192.168.100.0/25 | 192.168.100.1 | 192.168.100.126 | 192.168.100.127 
| 2         | 192.168.100.128/27 | 192.168.100.129 | 192.168.100.158 |  192.168.100.159
| 3         | 192.168.100.160/30 | 192.168.100.161 | 192.168.100.162  | 192.168.100.163

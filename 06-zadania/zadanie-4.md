# Podział i agregacja sieci

Dysponująć siecią o adresie ``80.90.100.96/27`` dokonaj podziału na 4 równe podsieci

| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
| Adres sieci do podziału | 80.90.100.96 | | 
| Maska sieci  |  /27 | |
| Maska binarnie  |  11111111.11111111.11111111.11100000 | |


2^n >= 4
2^3 >= 4
n = 2

| Podsiec   | Adres podsieci | Host min     | Host max      | Adres rozgłoszeniowy |
| -------------     |:-------------: | -----:       | -----:        | -----:    |
| 1         | 80.90.100.96 | 80.90.100.97 | 80.90.100.102 | 80.90.100.103 | 
| 2         | 80.90.100.104 | 80.90.100.105 | 80.90.100.110 | 80.90.100.111 |
| 3         | 80.90.100.112 | 80.90.100.113 | 80.90.100.118 | 80.90.100.119 |
| 4         | 80.90.100.120 | 80.90.100.121 | 80.90.100.126 | 80.90.100.127 |

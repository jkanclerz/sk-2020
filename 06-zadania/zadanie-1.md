# Podział i agregacja sieci

Dysponująć siecią o adresie ``192.168.1.0/24`` dokonaj podziału na 4 równe podsieci


| Parametr | wartość | komentarz(opcionalny) |
| ------------- |:-------------:| -----:|
| Adres sieci do podziału |  ``192.168.1.0`` | | 
| Maska sieci  | ``/24`` | |
| Maska binarnie  | ``11111111.11111111.11111111.00000000``  | |

---------------------------

Nowa maska podsieci

```
2^n >= L
n – liczba jedynek, które należy dopisać do starego adresu maski
L – liczba podsieci na którą dzielimy sieć
```

2^n >= 4
2^2 >= 4

zatem n = 2

Musimy oddać 2 jedynki z maski na rzecz adresów wydzielonych sieci


| Podsiec   | Adres podsieci | Host min     | Host max      | Adres rozgłoszeniowy |
| -------------     |:-------------: | -----:       | -----:        | -----:    |
| 1         | 192.168.1.0 | 192.168.1.1      | 192.168.1.62 |  192.168.1.63 |
| 2         | 192.168.1.64 | 192.168.1.65      | 192.168.1.126 | 192.168.1.127 |
| 3         | 192.168.1.128 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| 4         | 192.168.1.192 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |



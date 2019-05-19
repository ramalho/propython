# Linguagem Sucuri

A sucuri é uma cobra constritora comum no Brasil. É também o nome desta brincadeira: traduzir a linguagem Python para o português.

```
# coding: sucuri

def fibonacci(a=1, b=1): 
    enquanto 1: 
        produzir a 
        a, b = b, a+b

t = fibonacci()
para i em faixa(100): 
    exibir(prox(t))
```

Veja que `while` virou `enquanto`, `yield` virou `produzir`, `print` virou `exibir` e `range` virou `faixa`. Mas `def` é `def` mesmo.

O comentário especial `coding: sucuri` faz com que o interpretador Python invoque o nosso *codec* para pré-processar o programa-fonte.


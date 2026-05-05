# 🛠️ Exercícios de Tratamento de Erros e POO em Python

Este repositório contém uma série de desafios práticos focados no aprendizado de **Tratamento de Exceções (`try-except`)** e **Programação Orientada a Objetos (POO)** utilizando a linguagem Python.

## 📌 Visão Geral
O objetivo das atividades é garantir que o software consiga lidar com entradas inválidas ou comportamentos inesperados do usuário sem "quebrar" (interromper a execução), utilizando as cláusulas `try`, `except`, `else` e `finally`.

---

## 🚀 Detalhes dos Desafios

### 1. Desafio de Divisão Segura
Uma função que solicita dois números ao usuário e realiza a divisão.
- **Tratamentos incluídos:**
  - `ValueError`: Captura quando o usuário digita texto em vez de números.
  - `ZeroDivisionError`: Impede a divisão por zero.
  - `Exception`: Captura qualquer outro erro inesperado.
- **Estrutura:** Utiliza `else` para confirmar o sucesso e `finally` para encerrar o bloco.

### 2. Telemóvel e Duração (Input de String)
Primeira implementação da classe `Celular`.
- **Foco:** Tratar a entrada de dados no método `fazer_chamada`.
- **Lógica:** Tenta converter a duração da chamada para inteiro. Se o usuário passar uma string (ex: "Dez"), o sistema exibe uma mensagem de erro amigável.

### 3. Telemóvel e Custo (Tipos de Dados)
Segunda iteração da classe `Celular`.
- **Foco:** Tratamento de `TypeError`.
- **Lógica:** Verifica se o valor subtraído da bateria é compatível (numérico). Demonstra o uso de blocos completos de tratamento de erro dentro de métodos de classe.

### 4. Status de Bateria (Lógica + Erros)
Implementação focada em validação de intervalos.
- **Foco:** Unir lógica condicional (`if/elif`) com tratamento de erro.
- **Lógica:** Converte a entrada para `float` e categoriza o status da bateria (Baixo, Normal, Excelente), validando se o número está entre 0 e 100.

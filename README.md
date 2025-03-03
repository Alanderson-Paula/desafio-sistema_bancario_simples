# 🏦 Banco D'Paula - Sistema Bancário Simples

Este projeto é um sistema bancário simples desenvolvido em Python. Ele permite que os usuários realizem operações básicas como saques, depósitos e visualização de extratos.

## 📌 Funcionalidades

- **Saque:** Permite ao usuário sacar um valor de sua conta, respeitando o limite de saque e o saldo disponível.
- **Depósito:** Permite ao usuário depositar um valor em sua conta.
- **Extrato:** Exibe o extrato das transações realizadas e o saldo atual.
- **Sair:** Encerra o sistema bancário.

## 📷 Menu de Operações

```plaintext
╔═════════════════════════════════════════════╗
║               BANCO D`PAULA                 ║
╠═════════════════════════════════════════════╣
║        Selecione uma operação no menu       ║
╠═════════════════════════════════════════════╣
║        1 - SAQUE                            ║
║        2 - DEPÓSITO                         ║
║        3 - EXTRATO                          ║
║        4 - SAIR                             ║
╚═════════════════════════════════════════════╝
```
## ⚙️ Regras de Negócio
- **Limite de Saque**: O limite por saque é de R$ 500,00.
- **Número de Saques**: O usuário pode realizar até 3 saques por dia.
- **Validação de Valores**: O sistema valida se os valores informados para saque e depósito são positivos.

### Exemplo de Uso
  1. 🏧 Saque:

        - O usuário seleciona a opção 1.
        - Informa o valor do saque.
        - O sistema verifica se o valor é válido, se está dentro do limite e se o usuário possui saldo suficiente.
        - Se todas as condições forem atendidas, o valor é debitado do saldo e registrado no extrato.
  2. 💰 Depósito:

        - O usuário seleciona a opção 2.
        - Informa o valor do depósito.
        - O sistema verifica se o valor é válido.
        - Se o valor for válido, ele é creditado no saldo e registrado no extrato.
  3. 📝 Extrato:

        - O usuário seleciona a opção 3.
        - O sistema exibe o extrato das transações realizadas e o saldo atual.
  4. 🚪 Sair:

        - O usuário seleciona a opção 4.
        - O sistema encerra a execução.

### Como Executar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Execute o script conta_bancaria-v1.py em um terminal ou prompt de comando:
```bash
python conta_bancaria-v1.py
```


## 🚀 Conclusão
Este projeto faz parte do bootcamp **Suzano - Python Developer** oferecido pela ***Digital Innovation One*** (DIO). Durante o desenvolvimento deste sistema bancário, foram aplicados conceitos fundamentais de programação em Python, como controle de fluxo, manipulação de strings, e tratamento de exceções. Além disso, foi possível praticar a criação de interfaces de usuário baseadas em texto e a implementação de regras de negócio simples.

<br><br>
### 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo e usá-lo conforme necessário.

<br><br><br> Desenvolvido com 💙 por Alanderson de Paula

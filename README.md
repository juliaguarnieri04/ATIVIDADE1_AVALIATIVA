# SEUC-4 — Sistema de Escoamento de Unidades de Carga

## Integrantes do Grupo
- Julia Andrade Guarnieri
- Larissa Souza Quito Sampaio
- Pedro Henrique Sanches Agatti Godoy

---

# Sobre o Projeto

O SEUC-4 é um sistema desenvolvido em Python para monitorar leituras de pressão hidrodinâmica da Refinaria Delta-9.

O programa realiza ajustes térmicos automáticos nas leituras recebidas, classifica os níveis de estabilidade do duto e identifica situações críticas que podem causar danos ao sistema de escoamento.

Além disso, o sistema possui um protocolo de segurança que interrompe automaticamente o funcionamento ao detectar duas leituras consecutivas na Zona Vermelha.

---

# Funcionalidades

- Leitura de pressões hidrodinâmicas
- Ajuste térmico automático
- Classificação das zonas:
  - Zona Verde
  - Zona Amarela
  - Zona Vermelha
- Detecção de risco crítico
- Travamento automático do sistema
- Cálculo de métricas finais
- Interface organizada no terminal

---

# Regras do Sistema

## Ajuste térmico

### Pressões acima de 150 UPC
Aumento de 8%.

### Pressões menores ou iguais a 150 UPC
Redução de 4%.

---

# Classificação

## Zona Verde
Entre 120 e 180 UPC.

## Zona Amarela
Valores fora da Zona Verde e abaixo de 250 UPC.

## Zona Vermelha
Valores acima de 250 UPC.

---

# Protocolo de Segurança

Caso ocorram duas leituras consecutivas na Zona Vermelha, o sistema interrompe automaticamente o escoamento para evitar danos estruturais ao duto.

---

# Métricas Exibidas

Ao finalizar o processamento, o sistema apresenta:

- Média das pressões ajustadas
- Menor pressão registrada
- Percentual de leituras na Zona Verde
- Percentual executado até o travamento (caso ocorra)

---

# Tecnologias Utilizadas

- Python 3
- VSCode
- IDLE Python.org

---

# Como Executar

1. Abra o arquivo `.py` no VSCode ou IDLE.
2. Execute o programa.
3. Informe o número de leituras.
4. Digite os valores das pressões solicitadas.

---

# Estrutura do Projeto

```text
SEUC-4/
│
├── LICENSE
├── ProgramaAtividade.py
└── README.MD

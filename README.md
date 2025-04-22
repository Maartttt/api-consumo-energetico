# API de Consumo Energético

API RESTful desenvolvida em Django REST Framework para registro e monitoramento de consumo de energia por dispositivos.

## Objetivo

Gerenciar dispositivos e registrar o consumo de energia elétrica de forma simples, com possibilidade de expandir para análises, gráficos e integrações com sensores reais.

## Funcionalidades

- Cadastro de dispositivos (ex: ar-condicionado, geladeira, etc).
- Registro diário de consumo de energia (kWh).
- Listagem e filtro por data e dispositivo.
- Estrutura preparada para futuras integrações com IoT e IA.

## Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- SQLite (padrão, pode ser trocado por PostgreSQL)
- Git

## Como Rodar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/Maartttt/api-consumo-energetico.git
cd api-consumo-energetico

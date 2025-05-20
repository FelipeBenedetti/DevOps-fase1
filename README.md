# Projeto DevOps na Prática

Este repositório contém a implementação de um pipeline completo de DevOps, incluindo Integração Contínua (CI), Entrega Contínua (CD), e scripts de Infraestrutura como Código (IaC).

## Estrutura do Projeto

```
.
├── .github/workflows    # Configurações do GitHub Actions para CI/CD
├── src/                 # Código fonte da aplicação de exemplo
├── tests/               # Testes automatizados
└── terraform/           # Scripts de Infraestrutura como Código
```

## Funcionalidades Implementadas

- **Pipeline de Integração Contínua**: Configurado com GitHub Actions para executar testes automatizados, análise de código e validação de infraestrutura.
- **Infraestrutura como Código**: Scripts Terraform para provisionamento automatizado de infraestrutura na AWS.
- **Aplicação de Exemplo**: API simples em Flask para demonstrar o funcionamento do pipeline.

## Como Utilizar

### Pré-requisitos

- Git
- Python 3.9+
- Terraform 1.0+
- Conta AWS (para deploy da infraestrutura)

### Configuração Local

1. Clone o repositório:
   ```
   git clone https://github.com/FelipeBenedetti/DevOps-fase1.git
   cd DevOps-fase1
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute os testes:
   ```
   pytest tests/
   ```

4. Execute a aplicação localmente:
   ```
   python src/app.py
   ```

### Configuração da Infraestrutura

Consulte o [Tutorial de Implementação](docs/tutorial_implementacao.md) para instruções detalhadas sobre como configurar e provisionar a infraestrutura.

## Pipeline de CI/CD

O pipeline de CI/CD está configurado para executar automaticamente nas seguintes situações:

- **Push para as branches main ou develop**: Executa testes, análise de código e validação de infraestrutura.
- **Pull Requests para main ou develop**: Executa testes e análise de código para validar as alterações antes do merge.
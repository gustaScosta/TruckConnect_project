# Fluxograma Geral - TruckConnect

Este arquivo organiza o fluxo principal do projeto para servir de base na montagem do diagrama no Miro.

## Estrutura Principal

```mermaid
flowchart TD
    A[Início do sistema] --> B[Menu principal]
    B --> C{Qual opção o usuário escolheu?}

    C -->|Cadastro| D[Cadastro]
    C -->|Login| E[Login]
    C -->|Sair| F[Encerrar sistema]

    D --> G{Tipo de cadastro?}
    G -->|Empresa| H[Cadastro de empresa]
    G -->|Parceiro| I[Cadastro de parceiro]
    H --> J[Validar dados]
    I --> J
    J --> K[Salvar no banco de dados]
    K --> B

    E --> L{Tipo de login?}
    L -->|Empresa| M[Login de empresa]
    L -->|Parceiro| N[Login de parceiro]
    M --> O[Verificar dados no banco]
    N --> O
    O --> P{Login válido?}
    P -->|Sim - Empresa| Q[Área da empresa]
    P -->|Sim - Parceiro| R[Área do parceiro]
    P -->|Não| S[Exibir erro e tentar novamente]
    S --> E

    Q --> T[Sistema de fretes]
    R --> T

    T --> U[Cadastrar frete]
    T --> V[Listar fretes]
    T --> W[Aceitar frete]
    T --> X[Atualizar status]

    U --> Y[Banco de dados]
    V --> Y
    W --> Y
    X --> Y

    Y --> Z[Validações do sistema]
    Z --> B
    F --> AA[Fim]
```

## Blocos Principais

- Início do sistema
- Menu principal
- Cadastro
- Login
- Área da empresa
- Área do parceiro
- Sistema de fretes
- Banco de dados
- Validações do sistema
- Encerramento

## Subdivisão por Área

### 1. Menu principal

- Entrar no sistema
- Escolher cadastro
- Escolher login
- Sair

### 2. Cadastro

- Cadastro de empresa
- Cadastro de parceiro
- Validação de dados
- Salvamento no banco

### 3. Login

- Login de empresa
- Login de parceiro
- Verificação no banco
- Liberação de acesso

### 4. Área da empresa

- Cadastrar frete
- Listar fretes cadastrados
- Editar frete
- Acompanhar status

### 5. Área do parceiro

- Ver fretes disponíveis
- Ver detalhes do frete
- Aceitar frete
- Atualizar status do frete

### 6. Banco de dados

- Empresas
- Parceiros
- Fretes

### 7. Validações

- Validar CPF
- Validar CNPJ
- Evitar dados duplicados
- Verificar campos obrigatórios
- Validar status do frete

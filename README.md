# Trabalho 3 - Inteligência Artificial

Participantes: Matheus Alves e Pablo Sousa

## Parte 1 - Desafio: Árvore de Decisão com 10 Perguntas

Árvore de decisão que ajude uma pessoa a decidir entre diferentes hobbies ou carreiras, com base nas respostas a 10 perguntas.

### Funcionalidades

<ul>
  <li>Interatividade: O sistema faz 10 perguntas simples, respondidas com "sim" (1) ou "não" (0), que abordam preferências sobre trabalho em equipe, interesse por tecnologia, atividades ao ar livre, entre outros.</li>
  <li>Personalização: Com base nas respostas, o programa filtra dados de um dataset predefinido e sugere uma profissão compatível.</li>
  <li>Validação de Respostas: O código garante que apenas respostas válidas sejam aceitas, pedindo correção quando necessário.</li>
</ul>

### Resultados

<ul>
  <li>Após as respostas, o sistema retorna a profissão mais adequada para o perfil do usuário.
</li>
  <li>Caso nenhuma profissão corresponda às respostas, o programa informa que não foi possível encontrar uma recomendação.</li>
</ul>

## Parte 2 - Exploração de Datasets no Kaggle e UCI

 Uma árvore de decisão para resolver um problema baseado nesse dataset.

 ### Descrição do Problema
 Este dataset é originalmente do National Institute of Diabetes and Digestive and Kidney Diseases. O objetivo é prever, de forma diagnóstica, se um paciente possui diabetes com base em certas medições diagnósticas incluídas no conjunto de dados. Foram aplicadas várias restrições na seleção das instâncias, a partir de um banco de dados maior. Em particular, todas as pacientes neste dataset são mulheres com pelo menos 21 anos de idade e pertencentes à herança indígena Pima.

O conjunto de dados contém várias variáveis independentes (preditoras) relacionadas a fatores médicos e apenas uma variável dependente, a variável de saída (Outcome), que indica a presença ou ausência de diabetes.

### Dicionário de Dados

| Atributo                 | Descrição                          |
|--------------------------|------------------------------------|
| Pregnancies              | Número de gestações                |
| Glucose                  | Nível de glicose no sangue         |
| BloodPressure            | Medição da pressão arterial        |
| SkinThickness            | Espessura da pele                  |
| Insulin                  | Nível de insulina no sangue        |
| BMI                      | Índice de massa corporal           |
| DiabetesPedigreeFunction | Porcentagem de diabetes            |
| Age                      | Idade                              |
| Outcome                  | Resultado final. 1 é sim e 0 é não |

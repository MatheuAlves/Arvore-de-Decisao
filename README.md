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

Três modelos de aprendizado de máquina foram utilizados para resolver um problema baseado neste dataset:

<ul>
<li>K-Nearest Neighbors (KNN)</li>
<li>Árvore de Decisão (Decision Tree)</li>
<li>Máquinas de Vetores de Suporte (SVM - Support Vector Machine)</li>
</ul>

 ### Dataset

 [**Kaggle - Predict Diabetes**](https://www.kaggle.com/datasets/whenamancodes/predict-diabities)

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

Esses atributos são usados como entradas no modelo para prever se uma paciente tem diabetes, levando em consideração tanto fatores médicos quanto genéticos e de estilo de vida.

### Modelos Utilizados
Três algoritmos foram testados para realizar a classificação:
<ul>
<li*><strong>1. Árvore de Decisão (Decision Tree):</strong> Modelo baseado em divisões sequenciais dos dados, criando uma estrutura hierárquica de decisões.</li><br>
<li*><strong>2. K-Nearest Neighbors (KNN):</strong> Algoritmo baseado na proximidade entre pontos, classificando novos exemplos com base nos vizinhos mais próximos.</li*><br>
<li*><strong>3. Máquinas de Vetores de Suporte (SVM - Support Vector Machine):</strong> Modelo que encontra um hiperplano que melhor separa as classes, maximizando a margem entre os dados positivos e negativos.</li>
</ul>

### Acurácia dos Modelos
No código, a acurácia é calculada utilizando a função `accuracy_score` da biblioteca `scikit-learn`. Após o treinamento do modelo com os dados de treino, as previsões são feitas para o conjunto de teste (`y_pred`). A acurácia é obtida comparando essas previsões com os rótulos reais do conjunto de teste (`y_test`), calculando a proporção de predições corretas em relação ao total. O resultado final é exibido no console como uma porcentagem.

Ao final dos testes obtivemos os seguintes resultados:


| Modelo                   | Acurácia                           |
|--------------------------|------------------------------------|
| Decision Tree            | 72%                                |
| KNN                      | 69%                                |
| SVM                      | 74%                                |

### Comparação dos Resultados
Os modelos apresentaram desempenhos diferentes devido às suas características e suposições sobre os dados.
<ul>
<strong>1. SVM - Melhor desempenho (74%):</strong><br>
O SVM obteve a melhor acurácia, indicando que foi o mais eficiente para este conjunto de dados.Isso acontece porque SVM funciona bem em dados com múltiplas dimensões e distribuições não lineares, o que é o caso deste dataset. A principal força do SVM está na capacidade de maximizar a separação entre as classes, mesmo quando os dados não são perfeitamente separáveis.
</ul>
<ul>
<strong>2. Decision Tree - Segundo melhor desempenho (72%)</strong><br>
A Árvore de Decisão teve um desempenho um pouco inferior ao SVM.
Esse modelo divide os dados em regras de decisão, o que pode ser vantajoso para interpretar os resultados.
No entanto, as árvores de decisão podem sofrer com overfitting, especialmente se não forem bem podadas.
</ul>
<ul>
<strong>3. KNN - Pior desempenho (69%)</strong><br>
O KNN apresentou a menor acurácia dos três modelos.
Como esse algoritmo classifica um novo dado com base nos vizinhos mais próximos, ele pode ser muito sensível a distribuições desbalanceadas e ruídos no conjunto de dados.
Além disso, a escolha do número de vizinhos (k) pode afetar muito o desempenho, e um ajuste fino poderia melhorar a acurácia.
</ul>

### Conclusão
A análise comparativa revelou que o SVM foi o modelo mais eficaz (74%), devido à sua capacidade de separar classes de forma otimizada. A Árvore de Decisão (72%) mostrou-se interpretável, mas propensa a overfitting. O KNN (69%) teve o pior desempenho, possivelmente por sua sensibilidade à distribuição dos dados e à escolha de k.

A escolha do melhor modelo depende do contexto, balanceando precisão, interpretabilidade e custo computacional. Melhorias como tuning de hiperparâmetros, feature engineering e ensemble learning podem elevar o desempenho dos modelos, destacando a importância da experimentação para soluções mais robustas.

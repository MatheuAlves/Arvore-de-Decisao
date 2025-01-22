import pandas as pd
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Carregar o dataset (substitua ’seu_dataset .csv’ pelo arquivo baixado )
df = pd.read_csv("dataset_diabetes.csv")

# Inspecionar os dados
print(df.head())

# Pré-processar os dados (ajuste as colunas conforme necessário)
X = df [['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']] #Insira as colunas de entrada
y = df ['Outcome'] #Insira a coluna alvo

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Criar e treinar a árvore de decisão
clf = DecisionTreeClassifier(max_depth=3, random_state=21)
clf.fit(X_train, y_train)

# Fazer previsões e avaliar
y_pred = clf.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# Visualizar a árvore de decisão
plt.figure(figsize=(40, 55))
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=[str(cls) for cls in clf.classes_], 
    filled=True,
    rounded=True,
    fontsize=10
)

# Adicionando a legenda
legend_labels = ['0: Não Diabético', '1: Diabético'] 
handles = [mpatches.Patch(color='#1f77b4', label=legend_labels[1]), 
           mpatches.Patch(color='#ff7f0e', label=legend_labels[0])]  
plt.legend(handles=handles, loc='best', fontsize=12) 

plt.title("Árvore de Decisão para Classificação de Diabetes", fontsize=18)
plt.show()

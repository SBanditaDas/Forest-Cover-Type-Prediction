---

# 🧾 Forest Cover Type Prediction – Structured ML Classification

_Predicting forest cover types using topographic and environmental features from Roosevelt National Forest with Random Forests, data preprocessing, and modular ML pipeline._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#project-problem">Project Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project classifies forest cover types for 30m x 30m land patches using structured environmental data. It leverages a modular ML pipeline built in Python with Random Forests, feature scaling, and visual evaluation. The workflow includes data preprocessing, model training, evaluation, and visualization — all within a reproducible folder structure.

---

<h2><a class="anchor" id="project-problem"></a>Project Problem</h2>

Forest cover classification supports ecological planning, wildfire risk assessment, and land management. This project aims to:
- Automate forest type prediction using structured tabular data  
- Identify key environmental features influencing forest growth  
- Build a scalable ML pipeline for reproducible modeling  
- Enable visual interpretation of model performance  

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Tabular dataset uploaded to `data/raw/train.csv`  
- Includes 54 features: 10 numeric + 44 binary indicators  
- Target variable: `Cover_Type` (7 forest categories)  
- Source: Roosevelt National Forest (UCI ML Repository)  

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- Jupyter Notebook / Kaggle Notebook (EDA & modeling)  
- GitHub (version control and repo hosting)  
- Joblib (model saving)  

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
forest_cover_prediction/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── data/
│   ├── train.csv
│
├── notebooks/
│   └── fc_prediction.ipynb    # EDA and model training notebook
│
├── src/
│   ├── preprocessing.py          # Feature scaling
│   ├── train_model.py            # Model training and saving
│   └── evaluate_model.py         # Model evaluation
│
├── models/
│   └── random_forest_model.pkl   # Saved model
│
├── output_Visuals/
    ├── confusion_matrix.png      # Evaluation plot
    └── training_log.txt          # Optional logs
```

---

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Scaled numeric features using `StandardScaler`  
- Verified class distribution and feature correlation  
- Split dataset into train/test sets (80/20)  
- Encoded target labels and removed nulls (if any)  

---

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

- 📊 Confusion matrix for class-wise performance  
- 📋 Classification report with precision, recall, F1-score  
- 📈 Feature correlation heatmap  

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```
2. Place your dataset in data/raw/train.csv
3. Run the training script:
```
python src/train_model.py
```
4. Evaluate the saved model:
```
python src/evaluate_model.py
```
5. View outputs in the output_Visuals/ folder:
   >- confusion_matrix.png
   >- training_log.txt

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Sushree Bandita Das

 📧 Email: sushreebanditadas01@gmail.com  
🔗 [LinkedIn](http://www.linkedin.com/in/sushree-bandita-das-160651309)  
🔗 [Portfolio](http://datascienceportfol.io/sushreebanditadas01)

---

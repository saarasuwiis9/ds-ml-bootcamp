# Research Assignment1: Introduction to Machine Learning

## 1. Definition of Machine Learning with a Real-Life Example
Machine Learning (ML) is a discipline within artificial intelligence that focuses on enabling computers to learn from data and improve their performance on a task without being explicitly programmed with rules for that task. In ML, algorithms use historical data to build a model that can make decisions or predictions when presented with new, unseen data. This process involves identifying patterns and relationships from the data itself rather than manually encoding logic. (Source: Wikipedia)

**Real-life example:** Credit card fraud detection. Financial institutions use historical transaction data labeled either as “fraudulent” or “legitimate” to train a model. The ML algorithm learns patterns common in fraudulent transactions (such as unusual spending amounts at odd hours) and then applies this model to detect future fraud attempts in real time. Such systems help reduce financial losses and alert cardholders to suspicious activity. (Source: GeeksforGeeks)

---

## 2. Comparing Supervised and Unsupervised Learning

### Supervised Learning
Supervised learning is a paradigm where machine learning algorithms are trained using labeled data—datasets where each input example is paired with a correct output. The goal is to learn a mapping from inputs to outputs so that the model can accurately predict outcomes for new data. (Source: Wikipedia)

**Example:** Credit card fraud detection is a supervised learning task. The model is trained on past transactions labeled as “fraudulent” or “legitimate” and learns patterns to classify future transactions. (Source: GeeksforGeeks)

### Unsupervised Learning
Unsupervised learning uses unlabeled data. Instead of predicting known outputs, the algorithm seeks to uncover structure, patterns, or relationships in the data without guidance. (Source: Wikipedia)

**Example:** Customer segmentation in retail. Given purchasing histories without predefined categories, unsupervised learning algorithms (such as clustering) group customers into segments based on similar buying behaviors. This helps businesses tailor marketing strategies to distinct customer profiles. (Source: G2)

| Aspect              | Supervised Learning          | Unsupervised Learning       |
|--------------------|-----------------------------|----------------------------|
| Data               | Labeled                     | Unlabeled                  |
| Objective          | Predict known outputs       | Discover hidden structure  |
| Typical Tasks      | Classification, prediction  | Clustering, pattern discovery |
| Example            | Credit card fraud detection | Customer segmentation      |

---

## 3. What Causes Overfitting and How It Can Be Prevented

### Causes of Overfitting
Overfitting occurs when a model captures noise or specific peculiarities in the training data that do not generalize to new data. Main causes include:  
- Excessive model complexity compared to available data. (Source: Springer)  
- Insufficient training data, leading the model to memorize noise. (Source: ResearchGate)  
- Noise or irrelevant features that distract the learning algorithm. (Source: Wikipedia)

### Prevention Techniques
- **Cross-Validation:** Split training data into multiple parts to ensure the model performs well across subsets. (Source: ResearchGate)  
- **Regularization:** Techniques like L1 or L2 penalties reduce complexity. (Source: Wikipedia)  
- **Simpler Models:** Using fewer parameters reduces memorizing noise. (Source: Springer)  
- **More Training Data:** Increasing data size strengthens general patterns. (Source: ResearchGate)

---

## 4. Training Data and Test Data Split

### How Training/Test Splitting Works
The original dataset is partitioned into:
- **Training data:** used to fit and train the model  
- **Test data:** unseen examples used to evaluate performance  

A common split is 80% training and 20% test, though variations exist. Sometimes a validation set is used for parameter tuning. (Source: MDPI)

### Why Splitting Is Necessary
- Ensures the model generalizes to new data  
- Prevents overfitting evaluation bias  
- Provides realistic performance metrics on unseen data (Source: MDPI)

---

## 5. Case Study: Machine Learning in Transportation

**Application:** ML has been applied to intelligent transportation systems that improve traffic management and safety. Algorithms analyze large volumes of transportation data to enhance congestion control, optimize traffic light timing, and reduce accidents. (Source: ResearchGate)

**Findings:** A 2024 review identified that both supervised and unsupervised techniques manage traffic flow, predict vehicle demand, and monitor road conditions. ML improves urban mobility efficiency and infrastructure safety by learning patterns and automating real-time decisions. Challenges include data scarcity and computational demands. (Source: Springer)

---

## References
- Wikipedia. Machine Learning Overview.  
- GeeksforGeeks. Credit Card Fraud Detection using ML.  
- ResearchGate. Overfitting in Machine Learning.  
- Springer. Machine Learning Applications in Transportation.  
- MDPI. Train-Test Split in Machine Learning.  
- G2. Customer Segmentation Using ML.

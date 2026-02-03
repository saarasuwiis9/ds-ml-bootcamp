# Research Assignment: Introduction to Machine Learning

## 1. Machine Learning: Definition and Real-Life Example

### Definition
Machine Learning (ML) is a subfield of Artificial Intelligence (AI) that allows computers to learn from data and improve over time without being explicitly programmed. Instead of following fixed rules, ML algorithms find patterns and relationships in data. These patterns help systems make predictions, recognize patterns, and support decisions in real life.

### Real-Life Example: Face Recognition
Face recognition uses machine learning to identify people. The system is trained on many labeled photos and learns features like eye distance, nose shape, and face contours. Over time, it gets better and can correctly recognize people in new photos.

---

## 2. Supervised Learning and Unsupervised Learning

### Supervised Learning
The algorithm is trained on labeled data to learn the relationship between inputs and outputs.  
**Example:** Predicting house prices using features like size and location.

### Unsupervised Learning
The algorithm works on unlabeled data and tries to find patterns or groups within it.  
**Example:** Organizing library books into categories without predefined labels.

---

## 3. Causes of Overfitting

Overfitting occurs when a model learns the training data too well, including noise, resulting in poor performance on new data.

### Causes
- High model complexity for the dataset  
- Small or noisy datasets  
- Data leakage from test/validation sets  

### Prevention
- Regularization (L1/L2) to limit complexity  
- Cross-validation for reliable evaluation  
- More data and careful feature selection  
- Early stopping based on validation performance  

---

## 4. Training vs Test Data

When building an ML model, your dataset is divided into two parts:

- **Training set:** Data used to train the model  
- **Test set:** Data withheld during training, used to evaluate model performance on unseen examples  

### How Data is Split
- 80/20 split (80% training, 20% testing)  
- 70/30 split (70% training, 30% testing)  
- Sometimes a validation set is also used (e.g., 70% training, 15% validation, 15% testing)

### Why Splitting is Necessary
1. Avoid overfitting  
2. Evaluate generalization  
3. Tune hyperparameters safely (with validation set)

---

## 5. Case Study: Machine Learning in Business

### Predicting Online Store Purchases

**Case Study:**  
An online retailer wanted to predict which visitors would buy products.

**Data Used:**
- Time spent on site  
- Number of pages viewed  
- Past purchases  

**ML Model:** Logistic Regression  

**Findings:**  
Visitors who spent more time and viewed many pages were more likely to buy.

**Impact:**  
The store sent targeted offers to likely buyers, leading to increased sales.

---

## References

1. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill, New York.  
2. Dutt, S., Chandramouli, S., & Das, A. K. (2019). *Machine Learning*. Pearson Education, India.

# Research Assignment: Introduction to Machine Learning

## 1. Definition of Machine Learning with a Real-Life Example

**Machine Learning (ML)** is a field of Artificial Intelligence (AI) where computer systems learn patterns from data and make predictions or decisions without being explicitly programmed with rules. Instead of following fixed instructions, ML algorithms adjust themselves based on experience.

**Real-Life Example:**
Email spam detection. Instead of writing thousands of rules like “if the subject contains the word lottery, mark as spam,” a machine learning system is trained on thousands of emails labeled *spam* or *not spam.* Over time, the algorithm learns patterns — suspicious words, unusual sender addresses, or link structures — and can automatically classify new incoming emails correctly.

---

## 2. Supervised vs. Unsupervised Learning

**Supervised Learning:**

* Works with **labeled data** (input features X and known outputs y).
* The algorithm learns by comparing predictions against correct answers.
* Common tasks: **regression** (predicting numbers) and **classification** (predicting categories).

**Example:** Predicting house prices. Features like size, location, and number of rooms are inputs; the actual sale price is the label.

**Unsupervised Learning:**

* Works with **unlabeled data** (only features X, no known outputs).
* The algorithm looks for hidden patterns or groups in the data.
* Common tasks: **clustering** and **dimensionality reduction.**

**Example:** Customer segmentation in marketing. Based on purchase history and demographics, the model groups customers into clusters (e.g., frequent buyers, discount-seekers, occasional shoppers) without pre-labeled categories.

---

### Table: Comparison of Supervised vs Unsupervised Learning

| Aspect       | Supervised Learning                    | Unsupervised Learning        |
| ------------ | -------------------------------------- | ---------------------------- |
| Data type    | Labeled (X + y)                        | Unlabeled (X only)           |
| Goal         | Learn mapping from input to output     | Find hidden patterns in data |
| Example task | Spam detection, house price prediction | Customer segmentation        |
| Algorithms   | Linear Regression, Decision Trees      | K-Means, PCA                 |

---

## 3. Overfitting: Causes and Prevention

**Overfitting** occurs when a machine learning model memorizes the training data instead of learning general patterns. As a result, it performs very well on the training set but poorly on new, unseen data.

### Causes:

1. **Too complex models** with many parameters (e.g., deep trees, high-degree polynomials).
2. **Insufficient training data**, making the model latch onto noise instead of patterns.
3. **Too many irrelevant features** that add noise to the model.

### Prevention Strategies:

* **Simplify the model:** Use fewer parameters or simpler algorithms.
* **Regularization:** Apply L1/L2 penalties to reduce over-reliance on certain features.
* **Cross-validation:** Validate model performance on multiple folds of the dataset.
* **Collect more data:** More diverse examples improve generalization.
* **Early stopping:** Halt training before the model starts overfitting.

---

## 4. Training Data vs Test Data Split

Machine learning models must be evaluated on data they have **never seen before** to measure generalization. Therefore, datasets are split into:

* **Training data (70–80%)**: Used by the algorithm to learn the patterns.
* **Test data (20–30%)**: Used to evaluate performance on unseen data.

This prevents the model from being judged only on the data it was trained on (which could be misleading).

**Example:** If we train a model on 1,000 housing records, we may use 800 for training and 200 for testing. If the model performs well on both, it’s likely generalizing; if it only performs well on training data, it is overfitting.

Later, an additional **validation set** or **cross-validation** can be used for fine-tuning.

---

## 5. Case Study: Machine Learning in Healthcare

**Case Study Title:** “Predicting Diabetes Mellitus Using Machine Learning Techniques” (Source: *Scientific Reports, 2020*).

### Summary:

Researchers applied supervised learning algorithms to the **Pima Indian Diabetes Dataset**, which contains patient health measurements (e.g., BMI, glucose level, blood pressure). The goal was to predict whether a patient had diabetes.

* **Algorithms tested:** Logistic Regression, Decision Trees, Random Forests, and Support Vector Machines.
* **Best result:** Random Forest achieved the highest accuracy (\~80%).
* **Findings:** Features like glucose concentration and BMI were the most predictive of diabetes risk.

### Impact:

This study shows how ML can help healthcare professionals identify high-risk patients early, enabling preventive care and more effective treatment planning.

---

## References

1. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.
2. Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.
3. “Predicting Diabetes Mellitus Using Machine Learning Techniques.” *Scientific Reports*. Springer Nature, 2020.
4. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.

---
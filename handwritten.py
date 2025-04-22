from sklearn.datasets import load_digits
 from sklearn.model_selection import train_test_split
 from sklearn.linear_model import LogisticRegression
 from sklearn.metrics import accuracy_score
 import matplotlib.pyplot as plt
 X, y = load_digits(return_X_y=True)
 Xtr, Xte, Ytr, Yte = train_test_split(X, y, test_size=0.3)
 model = LogisticRegression(max_iter=10000).fit(Xtr, Ytr)
 Yp = model.predict(Xte)
 print(f"Accuracy: {accuracy_score(Yte, Yp)*100:.2f}%")
 fig, ax = plt.subplots(1, 6)
 for i in range(6):
 ax[i].imshow(Xte[i].reshape(8, 8), cmap='gray')
 ax[i].set_title(f"Pred: {Yp[i]}")
 ax[i].axis('off')
 plt.tight_layout()
 plt.show()

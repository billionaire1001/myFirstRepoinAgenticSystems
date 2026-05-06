import numpy 
from numpy.random import default_rng
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# --- DATASET GENERATION ---
rng = default_rng(seed=99)
n = 500

study_hours        = rng.uniform(1, 10, size=n)       # daily study hours
attendance_percent = rng.uniform(40, 100, size=n)     # class attendance %
assignments_done   = rng.uniform(0, 10, size=n)       # assignments submitted (out of 10)

scores = (
    20
    + 5.5  * study_hours
    + 0.4  * attendance_percent
    + 3.0  * assignments_done
    + rng.normal(0, 8, size=n)
)

# Label: 1 = Pass, 0 = Fail
y = (scores >= 70).astype(int)
X = numpy.column_stack([study_hours, attendance_percent, assignments_done])

# --- TASK 1: TRAIN A LOGISTIC REGRESSION MODEL ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)

model = LogisticRegression()
model.fit(X_train, y_train)

pass_count = numpy.sum(y == 1)
fail_count = numpy.sum(y == 0)

print("--- TASK 1: CLASS DISTRIBUTION ---")
print(f"Total Students: {n}")
print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}\n")

# --- TASK 2: PREDICT AND DISPLAY RESULTS ---
y_pred = model.predict(X_test)
probs = model.predict_proba(X_test)
p_pass = probs[:, 1]

print("--- TASK 2: PREDICTION RESULTS (FIRST 10) ---")
header = f"{'#':<3} | {'Study':<5} | {'Attnd%':<6} | {'Asgn':<4} | {'Act':<3} | {'Pred':<4} | {'P(Pass)':<7} | {'Correct?'}"
print(header)
print("-" * len(header))

for i in range(10):
    is_correct = "Yes" if y_test[i] == y_pred[i] else "No"
    print(f"{i:<3} | {X_test[i,0]:<5.1f} | {X_test[i,1]:<6.1f} | {X_test[i,2]:<4.1f} | {y_test[i]:<3} | {y_pred[i]:<4} | {p_pass[i]:<7.3f} | {is_correct}")

# --- TASK 3: EVALUATE WITH THE CONFUSION MATRIX ---
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
manual_accuracy = (tp + tn) / (tp + tn + fp + fn)

print("\n--- TASK 3: CONFUSION MATRIX ---")
print(f"TP (True Positives):  {tp}")
print(f"TN (True Negatives):  {tn}")
print(f"FP (False Positives): {fp}")
print(f"FN (False Negatives): {fn}")
print(f"Manual Accuracy:      {manual_accuracy:.4f}")

# --- TASK 4: COMPARE TWO DECISION THRESHOLDS ---
print("\n--- TASK 4: THRESHOLD COMPARISON ---")
thresholds = [0.5, 0.6]

for t in thresholds:
    t_preds = (p_pass >= t).astype(int)
    t_pass = numpy.sum(t_preds == 1)
    t_fail = numpy.sum(t_preds == 0)
    t_acc = numpy.mean(t_preds == y_test)
    
    print(f"Threshold: {t}")
    print(f"  Predicted Pass: {t_pass}")
    print(f"  Predicted Fail: {t_fail}")
    print(f"  Overall Accuracy: {t_acc:.4f}")

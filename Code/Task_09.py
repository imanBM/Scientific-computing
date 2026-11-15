import numpy as np

# Study group connection matrix (who studies/shares notes with whom)
# Order: Emmanuel, Sarah, Kevin, Faith, Brian
A = np.array([
    [0., 1., 1., 1., 0.],  # Emmanuel connects with Sarah, Kevin, Faith
    [1., 0., 1., 0., 0.],  # Sarah connects with Emmanuel, Kevin
    [1., 1., 0., 1., 1.],  # Kevin connects with Emmanuel, Sarah, Faith, Brian (Hub)
    [1., 0., 1., 0., 0.],  # Faith connects with Emmanuel, Kevin
    [0., 0., 1., 0., 0.]   # Brian only connects with Kevin
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant (largest) eigenvalue and its eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize so all influence scores add up to 1 (100%)
influence = dominant_vector / dominant_vector.sum()

students = ["Emmanuel", "Sarah", "Kevin", "Faith", "Brian"]
print(f"Dominant eigenvalue: {dominant_value:.4f}")
print("\nStudent Study-Group Influence Scores:")
for student, score in zip(students, influence):
    print(f"{student}: {score:.4f} ({score*100:.1f}%)")

# Verify Av = lambda * v
v = np.real(eigenvectors[:, index])
print("\nVerification error:", np.linalg.norm(A @ v - dominant_value * v))
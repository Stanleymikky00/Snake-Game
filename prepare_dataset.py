import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

#load the CSV

df = pd.read_csv("game_data.csv")
# Drop any rows with missing values (just in case)
df.dropna(inplace=True)

#1 Encode direction as categorical label (Up, Down → 0, 1, 2, 3)

label_encoder = LabelEncoder()
df['action_encoded'] = label_encoder.fit_transform(df['action'])

#2 Create input features X and output labels y
X = df[['head_x', 'head_y', 'food_x', 'food_y']]  # Input
y = df['action_encoded']                          # Output


#3️ Normalize X values for better neural network performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4️ Split into training and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 5️ Save all into .npy files for use in TensorFlow
np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

print("✅ Dataset prepared and saved!")
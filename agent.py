import numpy as np
import tensorflow as tf

#Loading the trained model
model = tf.keras.models.load_model("snake_model.keras")

# Same encoding as training: Up=0, Down=1, Left=2, Right=3
move_list = ["Up", "Down", "Left", "Right"]


def choose_action(state, scaler=None):
    input_data = np.array([[state["head_x"], state["head_y"], state["food_x"], state["food_y"]]])

    if scaler:
        input_data = scaler.transform(input_data)

    prediction = model.predict(input_data, verbose=0)
    action_index = np.argmax(prediction)

    return move_list[action_index]
def retrain_model(existing_model, new_data, new_labels):
    existing_model.fit(new_data, new_labels, epochs=5)
    existing_model.save('updated_model.h5')

# Assuming new_data and new_labels are available
if __name__ == "__main__":
    retrain_model(existing_model, new_data, new_labels)


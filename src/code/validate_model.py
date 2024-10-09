def validate_model(model):
    # Evaluate the model's performance on the validation set
    results = model.val()
    return results

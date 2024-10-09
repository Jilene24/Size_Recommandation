def run_inference(model, image_path=None, video_path=None):
    if image_path:
        results = model(image_path)
        # Check if results is a list or another type
        if isinstance(results, list):
            for result in results:
                if hasattr(result, 'show'):
                    result.show()
                else:
                    print("Result object has no 'show' method.")
        elif hasattr(results, 'show'):
            results.show()
        else:
            print("Results do not have a 'show' method.")

    if video_path:
        results = model(video_path)
        # Check if results is a list or another type
        if isinstance(results, list):
            for result in results:
                if hasattr(result, 'show'):
                    result.show()
                else:
                    print("Result object has no 'show' method.")
        elif hasattr(results, 'show'):
            results.show()
        else:
            print("Results do not have a 'show' method.")
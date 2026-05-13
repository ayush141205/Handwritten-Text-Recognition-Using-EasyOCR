import time
from difflib import SequenceMatcher

# Character similarity accuracy
def calculate_accuracy(actual_text, predicted_text):

    similarity = SequenceMatcher(
        None,
        actual_text.lower(),
        predicted_text.lower()
    ).ratio()

    accuracy = similarity * 100

    return round(accuracy, 2)


# Error rate
def calculate_error_rate(actual_text, predicted_text):

    accuracy = calculate_accuracy(
        actual_text,
        predicted_text
    )

    error_rate = 100 - accuracy

    return round(error_rate, 2)


# Word accuracy
def calculate_word_accuracy(actual_text, predicted_text):

    actual_words = actual_text.lower().split()
    predicted_words = predicted_text.lower().split()

    matched = 0

    for actual in actual_words:

        for predicted in predicted_words:

            similarity = SequenceMatcher(
                None,
                actual,
                predicted
            ).ratio()

            # 60% similarity threshold
            if similarity >= 0.6:
                matched += 1
                break

    total_words = len(actual_words)

    if total_words == 0:
        return 0

    accuracy = (matched / total_words) * 100

    return round(accuracy, 2)

# Processing time
def measure_processing_time(function, *args):

    start_time = time.time()

    result = function(*args)

    end_time = time.time()

    processing_time = end_time - start_time

    return result, round(processing_time, 2)
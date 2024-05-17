import Levenshtein

def calculate_cer(hypothesis, reference):
    # Convert both the hypothesis and reference to lowercase for case-insensitive comparison
    hypothesis = hypothesis.lower()
    reference = reference.lower()

    # Calculate CER using the Levenshtein distance
    cer = Levenshtein.distance(hypothesis, reference)

    # Normalize the CER score by dividing it by the length of the reference text
    cer /= len(reference)

    # Convert the CER to a percentage
    cer_percentage = cer * 100

    return cer_percentage

def calculate_wer(hypothesis, reference):
    # Convert both the hypothesis and reference to lowercase for case-insensitive comparison
    hypothesis = hypothesis.lower()
    reference = reference.lower()

    # Split the hypothesis and reference into words
    hypothesis_words = hypothesis.split()
    reference_words = reference.split()

    # Calculate WER using the Levenshtein distance on words
    wer = Levenshtein.distance(hypothesis_words, reference_words)

    # Normalize the WER score by dividing it by the number of words in the reference text
    wer /= len(reference_words)

    # Convert the WER to a percentage
    wer_percentage = wer * 100

    return wer_percentage

# Reference text
reference_text = 'my name is kenneth'

# Replace with the output of the first HTR tool
recognized_text = 'myy nime iz kenneth'

cer_recognized_text = calculate_cer(recognized_text, reference_text)
wer_recognized_text = calculate_wer(recognized_text, reference_text)
print(f"CER: {cer_recognized_text:.2f}%")
print(f"WER: {wer_recognized_text:.2f}%")

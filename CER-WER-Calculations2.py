import Levenshtein

def calculate_cer(hypothesis_path, reference_path):
    # Read contents from the hypothesis and reference files
    with open(hypothesis_path, 'r') as hyp_file:
        hypothesis = hyp_file.read().lower()
    with open(reference_path, 'r') as ref_file:
        reference = ref_file.read().lower()

    # Calculate CER using the Levenshtein distance
    cer = Levenshtein.distance(hypothesis, reference)

    # Normalize the CER score by dividing it by the length of the reference text
    cer /= len(reference)

    # Convert the CER to a percentage
    cer_percentage = cer * 100

    return cer_percentage

def calculate_wer(hypothesis_path, reference_path):
    # Read contents from the hypothesis and reference files
    with open(hypothesis_path, 'r') as hyp_file:
        hypothesis = hyp_file.read().lower()
    with open(reference_path, 'r') as ref_file:
        reference = ref_file.read().lower()

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

# File paths
reference_text_path = "/Users/timurmitrofanov/Desktop/Comparison/1.txt"
hypothesis_text_path = "/Users/timurmitrofanov/Desktop/Comparison/2.txt"

# Calculate CER
cer_score = calculate_cer(hypothesis_text_path, reference_text_path)
print("Character Error Rate (CER):", cer_score)

# Calculate WER
wer_score = calculate_wer(hypothesis_text_path, reference_text_path)
print("Word Error Rate (WER):", wer_score)




import Levenshtein

def calculate_cer(hypothesis_path, reference_path):
    with open(reference_path, 'r', encoding='utf-8', errors='replace') as ref_file:
        reference = ref_file.read().split()
    with open(hypothesis_path, 'r', encoding='utf-8', errors='replace') as hyp_file:
        hypothesis = hyp_file.read().split()
        
    # Convert both the hypothesis and reference to lowercase for case-insensitive comparison
    hypothesis = ' '.join(hypothesis).lower()
    reference = ' '.join(reference).lower()

    # Calculate CER using the Levenshtein distance
    cer = Levenshtein.distance(hypothesis, reference)

    # Normalize the CER score by dividing it by the length of the reference text
    cer /= len(reference)

    # Convert the CER to a percentage
    cer_percentage = cer * 100

    return cer_percentage

def calculate_wer(hypothesis_path, reference_path):
    with open(reference_path, 'r', encoding='utf-8', errors='replace') as ref_file:
        reference = ref_file.read().split()
    with open(hypothesis_path, 'r', encoding='utf-8', errors='replace') as hyp_file:
        hypothesis = hyp_file.read().split()

    # Convert both the hypothesis and reference to lowercase for case-insensitive comparison
    hypothesis = ' '.join(hypothesis).lower()
    reference = ' '.join(reference).lower()

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

reference_text = "/Users/path/file.txt"
recognized_text = "/Users/path/file.txt"

cer_recognized_text = calculate_cer(recognized_text, reference_text)
wer_recognized_text = calculate_wer(recognized_text, reference_text)
print(f"CER: {cer_recognized_text:.2f}%")
print(f"WER: {wer_recognized_text:.2f}%")

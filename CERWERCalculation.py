import Levenshtein

def calculate_cer(recognized_path, reference_path):
    with open(reference_path, 'r', encoding='utf-8', errors='replace') as ref_file:
        reference = ref_file.read().split()
    with open(recognized_path, 'r', encoding='utf-8', errors='replace') as hyp_file:
        recognized = hyp_file.read().split()
        
    # Converts both the recognized and reference texts to lowercase for case-insensitive comparison
    recognized = ' '.join(recognized).lower()
    reference = ' '.join(reference).lower()

    # Calculates CER using the Levenshtein distance
    cer = Levenshtein.distance(recognized, reference)

    # Normalizes the CER score by dividing it by the length of the reference text
    cer /= len(reference)

    # Converts the CER to a percentage
    cer_percentage = cer * 100

    return cer_percentage

def calculate_wer(recognized_path, reference_path):
    with open(reference_path, 'r', encoding='utf-8', errors='replace') as ref_file:
        reference = ref_file.read().split()
    with open(recognized_path, 'r', encoding='utf-8', errors='replace') as hyp_file:
        recognized = hyp_file.read().split()

    # Converts both the recognized and reference texts to lowercase for case-insensitive comparison
    recognized = ' '.join(recognized).lower()
    reference = ' '.join(reference).lower()

    # Splits the recognized and reference texts into words
    recognized_words = recognized.split()
    reference_words = reference.split()

    # Calculates WER using the Levenshtein distance on words
    wer = Levenshtein.distance(recognized_words, reference_words)

    # Normalizes the WER score by dividing it by the number of words in the reference text
    wer /= len(reference_words)

    # Converts the WER to a percentage
    wer_percentage = wer * 100

    return wer_percentage

reference_text = "/Users/path/1.txt"
recognized_text = "/Users/path/2.txt"

cer_recognized_text = calculate_cer(recognized_text, reference_text)
wer_recognized_text = calculate_wer(recognized_text, reference_text)
print(f"CER: {cer_recognized_text:.2f}%")
print(f"WER: {wer_recognized_text:.2f}%")

def calculate_wer(reference_path, hypothesis_path):
    with open(reference_path, 'r', encoding='utf-8', errors='replace') as ref_file:
        ref_words = ref_file.read().split()
    with open(hypothesis_path, 'r', encoding='utf-8', errors='replace') as hyp_file:
        hyp_words = hyp_file.read().split()
    # Counting the number of substitutions, deletions, and insertions
    substitutions = sum(1 for ref, hyp in zip(ref_words, hyp_words) if ref != hyp)
    deletions = len(ref_words) - len(hyp_words)
    insertions = len(hyp_words) - len(ref_words)
    # Total number of words in the reference text
    total_words = len(ref_words)
    # Calculating the Word Error Rate (WER)
    wer = (substitutions + deletions + insertions) / total_words
    return wer

reference_text_path = "/Users/timurmitrofanov/Desktop/1.txt"
hypothesis_text_path = "/Users/timurmitrofanov/Desktop/2.txt"

wer_score = calculate_wer(reference_text_path, hypothesis_text_path)
print("Word Error Rate (WER):", wer_score)


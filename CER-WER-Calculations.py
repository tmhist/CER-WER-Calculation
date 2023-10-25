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
reference_text = "There are a few editor men with whom I am privileged to come in contact. It has not been long since."  

# Replace with the output of the first HTR tool
hypothesis_tool_1 = "There ae a fw edito men wih whom I am privileged to come in conact. It has not been long since."  

cer_tool_1 = calculate_cer(hypothesis_tool_1, reference_text)
wer_tool_1 = calculate_wer(hypothesis_tool_1, reference_text)
print(f"CER for Tool 1: {cer_tool_1:.2f}%")
print(f"WER for Tool 1: {wer_tool_1:.2f}%")

# Replace with the output of the second HTR tool
hypothesis_tool_2 = "Three rae fwe editor mn with whom I prlilged to come in contact It has not beon long since"   
cer_tool_2 = calculate_cer(hypothesis_tool_2, reference_text)
wer_tool_2 = calculate_wer(hypothesis_tool_2, reference_text)
print(f"CER for Tool 2: {cer_tool_2:.2f}%")
print(f"WER for Tool 2: {wer_tool_2:.2f}%")

# Compare the CER and WER scores and make conclusions
if cer_tool_1 < cer_tool_2:
    print("Tool 1 performed better in terms of CER.")
elif cer_tool_2 < cer_tool_1:
    print("Tool 2 performed better in terms of CER.")
else:
    print("Both tools performed equally in terms of CER.")

if wer_tool_1 < wer_tool_2:
    print("Tool 1 performed better in terms of WER.")
elif wer_tool_2 < wer_tool_1:
    print("Tool 2 performed better in terms of WER.")
else:
    print("Both tools performed equally in terms of WER.")
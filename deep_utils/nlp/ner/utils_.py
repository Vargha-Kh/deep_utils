from typing import Union, List, Tuple


def check_bio_labels(input_labels: Union[str, List[str], Tuple[str]], query_label: str):
    """
    Checks whether the input-labels and queried labels are the same.
    :param input_labels:
    :param query_label:
    :return:
    >>> input_labels = ["B-Loc", "I-Loc"]
    >>> query_label = "Loc"
    >>> check_bio_labels(input_labels, query_label)
    >>> True
    """
    if isinstance(input_labels, str):
        input_labels = input_labels.replace("B-", "").replace("I-", "")
        if input_labels == query_label:
            return True
    elif isinstance(input_labels, list) or isinstance(input_labels, tuple):
        input_labels = [lbl.replace("B-", "").replace("I-", "") for lbl in input_labels]
        if len(set(input_labels)) == 1 and input_labels[0] == query_label:
            return True
    else:
        raise ValueError("Input_labels's type is not supported!")
    return False


def post_process_words_with_hashtag(input_words: List[str], input_labels: List[str]):
    """
    This function connects tokenized words with # to each other if they have the same labels
    :param input_words:
    :param input_labels:
    :return:
    >>> words =  ['تلفن', '98', '##21', '##55', '##87', '##14', '##42']
    >>> labels = [ 'B-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone']
    >>> post_process_words_with_hashtag(words, labels)
    (['تلفن', '982155871442'], ['B-phone', 'I-phone'])
    >>> words =  ['تلفن', '98', '##21', '##55', '##87', '##14', '##42'] + [","] + ['تلفن', '98', '##21', '##55', '##87', '##14', '##42']
    >>> labels = [ 'B-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone'] + ["o"] + [ 'B-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone', 'I-phone']
    >>> post_process_words_with_hashtag(words, labels)
    (['تلفن', '982155871442', ',', 'تلفن', '982155871442'], ['B-phone', 'I-phone', 'o', 'B-phone', 'I-phone'])
    """
    assert len(input_words) == len(input_labels), "[Error] Number of input_words and input_labels is not equal"
    res_words, res_labels = [], []
    sub_word = ""
    sub_label = None
    save_label = None
    for word, label in zip(input_words, input_labels):
        query_label = label.replace("I-", "").replace("B-", "")
        if "#" in word and (query_label == sub_label or not sub_label):
            sub_word += word.replace("#", "")
            sub_label = query_label
        else:
            if sub_word and save_label:
                res_words.append(sub_word)
                res_labels.append(save_label)
            sub_word = word
            sub_label = query_label
            save_label = label
    if sub_word and sub_label:
        res_words.append(sub_word)
        res_labels.append(save_label)
    return res_words, res_labels

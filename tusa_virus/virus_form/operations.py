from virus_form.models import States
from word2number import w2n


def data_update(state_name, victim_count):
    """ Functions that check and updates the data given"""

    get_state = States.objects.filter(state=state_name).first()
    try:
        if int(victim_count):
            victim_count = int(victim_count)
            get_state.victims = victim_count
            get_state.save()
            return
    except ValueError:
        sums = ""
        numbers = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
            'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
            'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
            'ninety': 90
        }
        bigger_numbers = {'billion': 1000000000, 'million': 1000000, 'hundred': 100,  'thousand': 1000}

    for key in numbers.keys():
        if key in victim_count:
            sums += key
            sums += " "
            for key2 in bigger_numbers.keys():
                if key2 in victim_count:
                    sums += key2
                    sums += " "
                    del bigger_numbers[key2]
                    break

    print(sums)
    number_real = w2n.word_to_num(sums)
    get_state.victims = number_real
    get_state.save()
    return


def total():
    """Get the total of all victims"""
    all_states = States.objects.all()
    total_sum = 0
    for state in all_states:
        total_sum += state.victims
    return total_sum






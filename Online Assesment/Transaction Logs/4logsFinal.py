from collections import defaultdict


def transactionThreashold(logs):
    threasholdMap = defaultdict(int)
    threashold = 2
    user_id = []

    for log in logs:
        transaction = log.split(' ')
        # PJ: 1. to get last element ignored in loop Plus the set concept to avoid duplicate
        for tran in set(transaction[:2]):
            threasholdMap[tran] += 1

    for key in threasholdMap:
        if threasholdMap[key] >= threashold:
            user_id.append(key)

    return sorted(user_id)
    # Alt way :
    # return sorted([key for key in threasholdMap if threasholdMap[key] >= threashold])


# Test
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = transactionThreashold(logs)
print(threshold)
def count_batteries_by_health(present_capacities):
    count_batteries={
    "healthy": 0,
    "exchange": 0,
    "failed": 0}
    for i in present_capacities:
        soh=100*i/120
        if(soh>80):
            count_batteries["healthy"]+=1
        elif(80>soh>=62):
            count_batteries["exchange"]+=1
        else:
            count_batteries["failed"]+=1
    return count_batteries


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '_main_':
  test_bucketing_by_health()

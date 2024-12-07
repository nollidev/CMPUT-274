# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864
# operating system: Fedora Linux 41 
# python version: 3.13.0 

def min_coins(coins, S):
    # Your implementation here
    coins_needed_for_sum = [999999] * (S + 1) # initialization, each value to be least coins needed 
    coins_needed_for_sum[0] = 0 # least coins needed for sum of 0 is 0

    for sum_of_debt in range(1, S + 1):
        for currency_value in coins:
            if currency_value <= sum_of_debt: # if the denomination's value can be subtracted from the sum
                coins_needed_for_sum[sum_of_debt] = min(coins_needed_for_sum[sum_of_debt], coins_needed_for_sum[sum_of_debt - currency_value] + 1) 

    return coins_needed_for_sum[S] if coins_needed_for_sum[S] < 999999 else -1

def main():
    coins = list(map(int, input().split()))
    S = int(input())
    print(min_coins(coins, S))

if __name__ == "__main__":
    main()

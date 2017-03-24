"""I have started to use define a main function for all my scripts is the correct?"""


def main():
    tariff_dict = {"tariff_11": "0.244618", "tariff_31": "0.136928", "tariff_51": "0.352415", "tariff_71": "0.144618",
                   "tariff_91": "0.123456"}
    print("Electicity bill estimator 2.0")
    tariff_choice = int(input("which tariff are you on 11, 31, 51, 71 or 91"))
    if tariff_choice == 11:
        tariff = tariff_dict["tariff_11"]
    elif tariff_choice == 31:
        tariff = tariff_dict["tariff_31"]
    elif tariff_choice == 51:
        tariff = tariff_dict["tariff_51"]
    elif tariff_choice == 71:
        tariff = tariff_dict["tariff_71"]
    else:
        tariff = tariff_dict["tariff_91"]

    total_daily_kwh = float(input("Please enter daily kWh usage"))
    billing_days = int(input("Please Enter total of billing days"))
    estimate_bill = float(tariff) * total_daily_kwh * float(billing_days)
    print(round(estimate_bill, 2))


main()

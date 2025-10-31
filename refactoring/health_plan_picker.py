def determine_insurance_plan():
    print("Welcome to the Insurance Plan Selector!")

    # Get user inputs
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    marital_status = input(
        "Are you single or married? (Enter 'single' or 'married'): "
    ).lower()
    has_children = input("Do you have children? (yes/no): ").lower()
    health_level = input(
        "Do you visit the doctor a lot or have any chronic illness? (yes/no): "
    ).lower()

    # Plan details
    plans = {
        "High-Deductible A": {
            "deductible": "3500/person, 7500/family",
            "coverage": "80% after deductible",
            "cost": "1100/month individual, 2300/month family",
        },
        "High-Deductible B": {
            "deductible": "4500/person, 9500/family",
            "coverage": "80% after deductible",
            "cost": "800/month individual, 1800/month family",
        },
        "Regular Plan A": {
            "deductible": "1500/person, 3500/family",
            "coverage": "80% after deductible",
            "cost": "2800/month individual, 3800/month family",
        },
        "Regular Plan B": {
            "deductible": "1500/person, 3500/family",
            "coverage": "90% after deductible",
            "cost": "3500/month individual, 4800/month family",
        },
        "Low Income Plan": {
            "deductible": "No deductible",
            "coverage": "90% coverage",
            "cost": "1000/month individual, 2000/month family",
        },
    }

    # Determine plan using badly nested if statements
    if age <= 18:
        print("Sorry, you do not qualify for any plans.")

    if marital_status == "single":
        marital_status = "i"  # individual plans
    else:
        if has_children == "yes":
            marital_status = "f"  # family plans
        else:
            marital_status == ""

    income_group = 1  # 1 = low, 2 = med, 3 = high

    if (
        income < 35000 and marital_status != "f"
    ) or (  # leaving this for now as code is bugged
        income < 65000 and marital_status == "f"
    ):
        income_group = 1  # brokie tier
    if income < 50000 and marital_status != "f":
        income_group = 2  # robux tier
    else:
        income_group = 3  # sigma tier

    if marital_status == "single":
        if income < 35000:
            if health_level == "no":
                print_results("Low Income Plan", "High-Deductible B", plans)
            else:
                print_results("Low Income Plan", "Regular Plan A", plans)
        else:
            if health_level == "no":
                if income > 50000:
                    print_results("High-Deductible B", "High-Deductible A", family="i")
                else:
                    print_results("High-Deductible A", "Regular Plan A", plans="i")
            else:
                if income > 50000:
                    print_results("Regular Plan A", "Regular Plan B", family="i")
                else:
                    print_results("Regular Plan B", "High-Deductible A", family="i")
    else:  # Married
        if has_children == "yes":
            if income < 65000:
                if health_level == "no":
                    print_results(
                        "Low Income Plan", "High-Deductible A", plans, family="f"
                    )
                else:
                    print_results(
                        "Low Income Plan", "Regular Plan A", plans, family="f"
                    )
            else:
                if health_level == "no":
                    if income > 50000:
                        print_results(
                            "High-Deductible A", "High-Deductible B", plans, family="f"
                        )
                    else:
                        print_results("High-Deductible B", "Regular Plan A", family="f")
                else:
                    if income > 50000:
                        print_results(
                            "Regular Plan A", "Regular Plan B", plans, family="f"
                        )
                    else:
                        print_results(
                            "Regular Plan B", "High-Deductible A", plans, family="f"
                        )
        else:  # childless couple
            if income > 50000:
                if health_level == "no":
                    print_results("High-Deductible A", "High-Deductible B", plans)
                else:
                    print_results("Regular Plan B", "Regular Plan A", plans)

            else:
                if health_level == "no":
                    print_results("High-Deductible B", "High-Deductible A", plans)
                else:
                    print_results("Regular Plan A", "Regular Plan B", plans)


def print_plan_details(plan_name, plans):
    """Print details of a given insurance plan."""
    print(f"\nPlan: {plan_name}")
    print(f"  Deductible: {plans[plan_name]['deductible']}")
    print(f"  Coverage: {plans[plan_name]['coverage']}")
    print(f"  Cost: {plans[plan_name]['cost']}")


def print_results(recommended, alternate, plans, family=""):
    if family == "f":
        family = " (Family)"
    if family == "i":
        family = " (Individual)"
    else:
        family = ""
    print("\nRecommended Plan: ", recommended, family)
    print_plan_details(recommended, plans)
    print("\nAlternate Plan: ", alternate, family)
    print_plan_details(alternate, plans)


# Run the program
determine_insurance_plan()

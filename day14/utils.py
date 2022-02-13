def load_data():
    """Read Day 14 puzzle input."""
    return load_template(), load_rules()


def load_template():
    """Load polymer template into string."""
    with open("input_template.txt") as f:
        template = f.read().splitlines()[0]
    return template


def load_rules():
    """Load pair insertion rules into dictionary."""
    with open("input_rules.txt") as f:
        rules = f.read().splitlines()
    # Split at and remove arrow
    rules = [rule.split(" -> ") for rule in rules]
    # Create rule map
    rules_map = {rule[0]: rule[1] for rule in rules}
    return rules_map

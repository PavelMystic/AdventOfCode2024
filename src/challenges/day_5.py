from pathlib import Path
import re


def check_update(
    update: list[int],
    following_pages: dict[int, list[int]],
    preceeding_pages: dict[int, list[int]],
) -> bool:

    rules_violated = False

    for page_idx in range(len(update) - 1):
        page_num = update[page_idx]
        if page_num in preceeding_pages:
            broken_rules = set(update[page_idx + 1 :]).intersection(
                set(preceeding_pages[page_num])
            )
            if broken_rules:
                rules_violated = True
                return rules_violated
        if page_idx > 0:
            if page_num in following_pages:
                broken_rules = set(update[: page_idx - 1]).intersection(
                    set(following_pages[page_num])
                )
                if broken_rules:
                    rules_violated = True
                    return rules_violated

    return rules_violated


def flag_bad_ordering(
    update: list[int],
    following_pages: dict[int, list[int]],
    preceeding_pages: dict[int, list[int]],
) -> list[bool]:

    bad_ordering = [False for _ in update]

    for page_idx in range(len(update) - 1):
        page_num = update[page_idx]
        if page_num in preceeding_pages:
            broken_rules = set(update[page_idx + 1 :]).intersection(
                set(preceeding_pages[page_num])
            )
            if broken_rules:
                bad_ordering[page_idx] = True
        if page_idx > 0:
            if page_num in following_pages:
                broken_rules = set(update[: page_idx - 1]).intersection(
                    set(following_pages[page_num])
                )
                if broken_rules:
                    bad_ordering[page_idx] = True
    return bad_ordering


if __name__ == "__main__":

    # input_orderings_path = Path() / "input_orderings_day_5.txt"
    input_orderings_path = Path() / "test_input_orderings_day_5.txt"

    PATTERN = r"(\d+) \| (\d+)"
    preceeding_orderings: dict[int, list[int]] = {}
    following_orderings: dict[int, list[int]] = {}

    with input_orderings_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            matches = re.finditer(PATTERN, line)

            for match in matches:
                preceeding_page = int(match.group(1))
                following_page = int(match.group(2))

                if preceeding_page in preceeding_orderings:
                    preceeding_orderings[preceeding_page].append(following_page)
                else:
                    preceeding_orderings[preceeding_page] = [following_page]

                if following_page in following_orderings:
                    following_orderings[following_page].append(preceeding_page)
                else:
                    following_orderings[following_page] = [preceeding_page]

    # input_updates_path = Path() / "input_updates_day_5.txt"
    input_updates_path = Path() / "test_input_updates_day_5.txt"

    PATTERN = r"(\d+(?:,\s*\d+)*)"

    updates: list[list[int]] = []

    with input_updates_path.open(mode="r", encoding="utf-8") as file:
        for line in file:
            update: list[int] = []
            matches = re.finditer(PATTERN, line)

            for match in matches:
                update += [int(num) for num in match.group(1).split(",")]
            updates.append(update)

    sum_middle = 0

    for update in updates:
        is_violated = check_update(update, preceeding_orderings, following_orderings)

        if not is_violated:
            if len(update) % 2 == 1:
                sum_middle += update[int((len(update) + 1) / 2) - 1]
        else:
            bad_ordering = flag_bad_ordering(
                update, preceeding_orderings, following_orderings
            )
            a = 3

    print(sum_middle)

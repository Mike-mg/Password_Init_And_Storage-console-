"""
Module views for the database
"""


class ViewBdd:
    """
    Views for the Bdd
    """

    def __init__(self) -> None:
        pass

    def choice_option_menu(self) -> int:
        """
        Select choice for action of database
        """

        choice_id = int(input("> Choice id at remove : "))
        return choice_id

    def show_formated_element_table(self, all_element_database):
        """
        Get and show all element formated of the table in the bdd
        """

        id_table = 'Id'.center(11)
        label = 'Label'.center(45)
        str_passaword = 'Password'.center(15)
        name_table = '<<< Table Sesame >>>'.center(79)

        texte_menu_table = f"{id_table} | {label} | {str_passaword} |"

        print(f"\n{name_table}\n{'=' * 79}\n{texte_menu_table}\n{'=' * 79}")

        for element in all_element_database:

            element_0 = str(element[0]).center(11)
            element_1 = str(element[1]).center(45)
            element_2 = str(element[2]).center(15)

            print(f"{element_0} | {element_1} | {element_2} |")

        print(f"{'=' * 79}\n")

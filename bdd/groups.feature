Scenario Outline: Add new group
  Given A group list
  Given A group with <name>, <header>, <footer>
  When Add a new group
  Then The new group list is equal to the old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |


Scenario: Delete a group
  Given A non-empty group list
  Given A random group
  When Delete a group
  Then The new group list is equal to the old list without deleted group


Scenario: Update a group
  Given A non-empty group list
  Given A random group
  Given A group data
  When Update a group
  Then The new group list is equal to the old list with updated group

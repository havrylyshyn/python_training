Scenario Outline: Add new contact
  Given A contact list
  Given A contact with <firstname>, <lastname>, <address>, <homephone>, <email>
  When Add a new contact
  Then The new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | lastname  | address  | homephone  | email  |
  | firstname1 | lastname1 | address1 | homephone1 | email1 |
  | firstname2 | lastname2 | address2 | homephone2 | email2 |
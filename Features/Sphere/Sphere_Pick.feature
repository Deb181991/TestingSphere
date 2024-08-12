Feature: Check the login functionality of sphereWMS application

  # Background:
  #   Given launch the browser

  @Pick1
  # Scenario Outline: The user should be able to login to the application successfully
  Scenario Outline: Parallel1
    Given launch the "<Url>"
    Then Enter the "<username>" in the username field
    Then Enter the "<password>" in the Password field
    Then click on login button
    And click on Allocation Menu
    Then click on Pick Submenu
    Then choose "<location>" from location dropdown box
    Then click on getNextPick button 
    # Then enter "<Lp>" in Scan License Plate field

    Examples:
      | Url                                        | username                 | password         |location|Lp                  |
      | https://sandbox.v2.nonprod.spherewms.com/  | umar.anwar@spherewms.com | Silentassasin123 |NRCC#1  |16020840593472106508|

  

 @Pick2
  # Scenario Outline: The user should be able to login to the application successfully
  Scenario Outline: Parallel2
    Given launch the "<Url>"
    Then Enter the "<username>" in the username field
    Then Enter the "<password>" in the Password field
    Then click on login button
    And click on Allocation Menu
    Then click on Pick Submenu
    Then choose "<location>" from location dropdown box
    Then click on getNextPick button 
    # Then enter "<Lp>" in Scan License Plate field

    Examples:
      | Url                                       | username                 | password         |location|Lp                  |
      | https://sandbox.v2.nonprod.spherewms.com/ | umar.anwar@spherewms.com | Silentassasin123 |NRCC#1  |16020840593472106508|

#  @Pick3
#   # Scenario Outline: The user should be able to login to the application successfully
#   Scenario Outline: Parallel3
#     Given launch the "<Url>"
#     Then Enter the "<username>" in the username field
#     Then Enter the "<password>" in the Password field
#     Then click on login button
#     And click on Allocation Menu
#     Then click on Pick Submenu
#     Then choose "<location>" from location dropdown box
#     Then click on getNextPick button 
#     Then enter "<Lp>" in Scan License Plate field

#     Examples:
#       | Url                                             | username                          | password   |location|Lp                  |
#       | https://jde-3373.v2.nonprod.spherewms.com/login | debadatta.pattanaik@spherewms.com | Test@1234  |NRCC#1  |16020840593472106508|
    
#  @Pick4
#   # Scenario Outline: The user should be able to login to the application successfully
#   Scenario Outline: Parallel4
#     Given launch the "<Url>"
#     Then Enter the "<username>" in the username field
#     Then Enter the "<password>" in the Password field
#     Then click on login button
#     And click on Allocation Menu
#     Then click on Pick Submenu
#     Then choose "<location>" from location dropdown box
#     Then click on getNextPick button 
#     Then enter "<Lp>" in Scan License Plate field

#     Examples:
#       | Url                                             | username                        | password   |location|Lp                  |
#       | https://jde-3373.v2.nonprod.spherewms.com/login | subhashis.palit@spherewms.com | #1SphereWMS |NRCC#1  |16020840593472106508|

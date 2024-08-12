Feature: Check the login functionality of sphereWMS application

  # Background:
  #   Given launch the browser

  @Login_Spherewms
  Scenario Outline: The user should be able to login to the application successfully
    Given launch the "<Url>"
    Then Enter the "<username>" in the username field
    Then Enter the "<password>" in the Password field
    Then click on login button
    

    Examples:
      | Url                                       | username                 | password         |
      | https://sandbox.v2.nonprod.spherewms.com/ | umar.anwar@spherewms.com | Silentassasin123 |

  @TruckRequest
  Scenario Outline: Verify User can able to create truck request
    And click on dashboard page
    Then click on target portal

    Examples:
      | SheetName   | Rowno | Path                     | PageTitle             |
      | Login_Creds | 0     | TestData\Testcase_CV.xls | CEVA Vision - Develop |

  @createTruck
  Scenario Outline: Verify User can able to create truck request
    And click on truck information
    Then click on truck schedule
    Then click on new request
    Then select Type from the "<SelectType>" dropdown
    Then select "<Service Provider>" from the dropdown
    Then select In Store Date from the calander
    Then select "<Origin>" from the Origin dropdown
    Then select "<Destination>" from the Destination dropdown
    Then enter request "<time>" in Pickup field
    Then enter request "<time>" in Delivery field
    Then select Requested Pickup Date from the calander
    Then select Requested Delivery Date from the calander
    Then click on submit
    Then confirm the details
    Examples:
      | SelectType | Service Provider | Origin          | Destination         |time |
      | PIPO       | CEVA             | BunzlKansasCity | NRCC #1-EAGAN MN-MSP|12:00|

